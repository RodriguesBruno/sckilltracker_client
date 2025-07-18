import calendar
import logging
from datetime import timedelta, datetime
from typing import Optional
import pandas as pd

from src.models.models import PlayerMonthStatistics


class StatisticsController:
    def __init__(self) -> None:
        self._df: Optional[pd.DataFrame] = None

    def _get_prepared_df(self) -> pd.DataFrame:
        df = self._df.copy()
        df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)

        return df

    def set_data(self, events: list[dict]) -> None:
        logging.info(f"[STATISTICS CONTROLLER] - SET DATA")
        self._df = pd.DataFrame(events)

    def top_victims(self, limit: int = 5, exclude_player: Optional[str] = None) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        df: pd.DataFrame = self._df.copy()

        filtered_df = df[df['damage'] != 'Suicide']

        if exclude_player:
            filtered_df = filtered_df[filtered_df['victim_name'] != exclude_player]

        top = (
            filtered_df['victim_name']
            .value_counts()
            .head(limit)
            .to_frame(name='count')
            .reset_index()
            .rename(columns={'index': 'name'})
        )

        return top.to_dict(orient='records')

    def kills_for_player_this_month(self, player_name: str) -> PlayerMonthStatistics:
        """Return the number of kills a pilot made in the current month."""
        if self._df is None or self._df.empty:
            return PlayerMonthStatistics(
                player_name=player_name,
                month=datetime.now().strftime("%B"),
                kills=0,
                deaths=0,
                suicides=0,
                kdr=0
            )

        df: pd.DataFrame = self._get_prepared_df()

        now = pd.Timestamp.utcnow()
        current_year = now.year
        current_month = now.month
        month_name = calendar.month_name[current_month]

        is_this_month = (df["date"].dt.year == current_year) & (df["date"].dt.month == current_month)

        monthly_kills = df[is_this_month & (df["killer_name"] == player_name)]
        monthly_deaths = df[is_this_month & (df["victim_name"] == player_name)]

        non_suicide_kills = monthly_kills[monthly_kills["damage"] != "Suicide"]
        suicide_kills = monthly_kills[monthly_kills["damage"] == "Suicide"]
        non_suicide_deaths = monthly_deaths[monthly_deaths["damage"] != "Suicide"]

        try:
            kdr = round(len(non_suicide_kills) / len(non_suicide_deaths), 2)

        except ZeroDivisionError:
            kdr = 0

        player_statistics: PlayerMonthStatistics = PlayerMonthStatistics(
            player_name=player_name,
            month=month_name,
            kills=len(non_suicide_kills),
            deaths=len(non_suicide_deaths),
            suicides=len(suicide_kills),
            kdr=kdr
        )
        return player_statistics

    def top_killers(self, limit: int = 5, exclude_player: Optional[str] = None) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        df: pd.DataFrame = self._df.copy()


        filtered_df = df[df['damage'] != 'Suicide']


        if exclude_player:
            filtered_df = filtered_df[filtered_df['killer_name'] != exclude_player]

        top = (
            filtered_df['killer_name']
            .value_counts()
            .head(limit)
            .to_frame(name='count')
            .reset_index()
            .rename(columns={'index': 'name'})
        )

        return top.to_dict(orient='records')

    def top_killers_old(self, limit: int = 5) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        df: pd.DataFrame = self._df.copy()

        filtered_df = df[df['damage'] != 'Suicide']

        top = filtered_df['killer_name'].value_counts().head(limit).to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)

        return top.to_dict(orient='records')

    def kills_by_game_mode(self) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        top = self._df['game_mode'].value_counts().to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)

        return top.to_dict(orient='records')

    def damage_type_distribution(self) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        top = self._df['damage'].value_counts().to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)

        return top.to_dict(orient='records')

    def _get_table(self, name: str, filter_by: str, limit: int, exclude_player: Optional[str] = None) -> pd.DataFrame:
        df: pd.DataFrame = self._get_prepared_df()
        now = pd.Timestamp.utcnow()

        if exclude_player:
            df = df[df[filter_by] != exclude_player]

        periods = {
            "day": now - timedelta(days=1),
            "week": now - timedelta(weeks=1),
            "month": now - pd.DateOffset(months=1),
            "all": None
        }

        counts: dict = {}

        for label, since in periods.items():
            if since:
                filtered = df[df["date"] >= since]
            else:
                filtered = df

            top = (
                filtered[filter_by]
                .value_counts()
                .head(limit)
                .to_frame(name=label)
            )

            counts[label] = top

        result = pd.concat(counts.values(), axis=1).fillna(0).astype(int)

        result.index.name = name
        result.reset_index(inplace=True)

        return result

    def get_top_killers_table(self, limit: int = 10, exclude_player: Optional[str] = None) -> list[dict[str, int]]:
        if self._df is None or self._df.empty:
            return []

        result = self._get_table(name="killer", filter_by="killer_name", limit=limit, exclude_player=exclude_player)

        return result.to_dict(orient="records")

    def get_top_victims_table(self, limit: int = 10, exclude_player: Optional[str] = None) -> list[dict[str, int]]:
        if self._df is None or self._df.empty:
            return []

        result = self._get_table(name="victim", filter_by="victim_name", limit=limit, exclude_player=exclude_player)

        return result.to_dict(orient="records")
    
    ##Add a new method to summarize kills/deaths by period for a specific player:
    def player_kills_deaths_by_period(self, player_name: str) -> dict:
        if self._df is None or self._df.empty:
            return {}

        df = self._get_prepared_df()
        now = pd.Timestamp.utcnow()

        periods = {
            "day": now - timedelta(days=1),
            "week": now - timedelta(weeks=1),
            "month": now - pd.DateOffset(months=1),
            "all": None
        }

        result = {}

        for period, since in periods.items():
            if since:
                df_period = df[df["date"] >= since]
            else:
                df_period = df

            kills = df_period[(df_period["killer_name"] == player_name) & (df_period["damage"] != "Suicide")]
            deaths = df_period[(df_period["victim_name"] == player_name) & (df_period["damage"] != "Suicide")]
            suicides = df_period[(df_period["killer_name"] == player_name) & (df_period["damage"] == "Suicide")]

            kdr = round(len(kills) / len(deaths), 2) if len(deaths) > 0 else len(kills)
            result[period] = {
                "kills": len(kills),
                "deaths": len(deaths),
                "suicides": len(suicides),
                "kdr": kdr
            }

        return result
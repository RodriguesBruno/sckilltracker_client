import calendar
import logging
from datetime import timedelta, datetime
from typing import Optional

import pandas as pd


class StatisticsController:
    def __init__(self) -> None:
        self._chart_template: str = 'plotly_dark'
        self._chart_width: int = 700
        self._chart_height: int = 350

        self._rsi_url: str = "https://robertsspaceindustries.com/en/citizens"

        self._df: Optional[pd.DataFrame] = None

    def _get_prepared_df(self) -> pd.DataFrame:
        df = self._df.copy()
        df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)

        return df

    def set_data(self, events: list[dict]) -> None:
        logging.info(f"[STATISTICS CONTROLLER] - SET DATA")
        self._df = pd.DataFrame(events)

    def top_victims(self, limit: int = 5) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        top = self._df['victim_player_name'].value_counts().head(limit).to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)
        
        return top.to_dict(orient='records')

    def kills_this_month_for_pilot(self, pilot_name: str) -> dict[str, None | int | str]:
        """Return the number of kills a pilot made in the current month."""
        if self._df is None or self._df.empty:
            return {
                "month": datetime.now().strftime("%B"),
                "kills": 0,
                "pilot": pilot_name
            }

        df: pd.DataFrame = self._get_prepared_df()

        now = pd.Timestamp.utcnow()
        current_year = now.year
        current_month = now.month
        month_name = calendar.month_name[current_month]

        monthly_kills = df[
            (df["killed_by"] == pilot_name) &
            (df["date"].dt.year == current_year) &
            (df["date"].dt.month == current_month)
            ]

        return {
            "month": month_name,
            "kills": len(monthly_kills),
            "pilot": pilot_name
        }

    def top_killers(self, limit: int = 5) -> list[dict[str, int]]:
        if self._df.empty:
            return []

        top = self._df['killed_by'].value_counts().head(limit).to_frame(name='count').reset_index()
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

    def _get_table(self, name: str, filter_by: str, limit: int):
        df: pd.DataFrame = self._get_prepared_df()
        now = pd.Timestamp.utcnow()

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

    def get_top_killers_table(self, limit: int = 10) -> list[dict[str, int]]:
        if self._df is None or self._df.empty:
            return []

        result = self._get_table(name="killer", filter_by="killed_by", limit=limit)

        return result.to_dict(orient="records")

    def get_top_victims_table(self, limit: int = 10) -> list[dict[str, int]]:
        if self._df is None or self._df.empty:
            return []

        result = self._get_table(name="victim", filter_by="victim_player_name", limit=limit)

        return result.to_dict(orient="records")

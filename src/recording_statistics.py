import pandas as pd
import plotly.express as px
from typing import List, Dict, Optional


class RecordingStatistics:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df: Optional[pd.DataFrame] = None
        self._load_csv()


    def _load_csv(self) -> None:
        try:
            self.df = pd.read_csv(self.csv_path, parse_dates=['date'])

        except FileNotFoundError:
            self.df = pd.DataFrame()

    def top_victims(self, limit: int = 5) -> List[Dict[str, int]]:
        if self.df.empty:
            return []

        top = self.df['victim_player_name'].value_counts().head(limit).to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)
        return top.to_dict(orient='records')

    def get_top_victims_chart_html(self) -> str:
        if self.df.empty:
            return ""

        data = self.df['victim_player_name'].value_counts().head(10).reset_index()
        data.columns = ['victim_player_name', 'count']
        data['url'] = data['victim_player_name'].apply(lambda name: f"https://robertsspaceindustries.com/en/citizens/{name}")
        fig = px.bar(data, x='victim_player_name', y='count', title='Top Victims', custom_data=['url'])

        fig.update_layout(
            template='plotly_dark',
            width=700,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )

        return fig.to_html(full_html=False, include_plotlyjs=False, div_id='top-victims-chart')

    def top_killers(self, limit: int = 5) -> List[Dict[str, int]]:
        if self.df.empty:
            return []

        top = self.df['killed_by'].value_counts().head(limit).to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)
        return top.to_dict(orient='records')

    def get_top_killers_chart_html(self) -> str:
        if self.df.empty:
            return ""

        data = self.df['killed_by'].value_counts().head(10).reset_index()
        data.columns = ['killed_by', 'count']

        data['url'] = data['killed_by'].apply(lambda name: f"https://robertsspaceindustries.com/en/citizens/{name}")
        fig = px.bar(data, x='killed_by', y='count', title='Top Killers', custom_data=['url'])

        # fig = px.bar(data, x='killed_by', y='count', title='Top Killers')
        fig.update_layout(
            template='plotly_dark',
            width=700,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        return fig.to_html(full_html=False, include_plotlyjs=False, div_id='top-killers-chart')

    def kills_by_game_mode(self) -> List[Dict[str, int]]:
        if self.df.empty:
            return []

        top = self.df['game_mode'].value_counts().to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)
        return top.to_dict(orient='records')

    def get_game_mode_pie_chart_html(self) -> str:
        if self.df.empty:
            return ""

        data = self.df['game_mode'].value_counts().reset_index()
        data.columns = ['game_mode', 'count']
        fig = px.pie(data, names='game_mode', values='count', title='Kills by Game Mode')
        fig.update_layout(
            template='plotly_dark',
            width=700,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        return fig.to_html(full_html=False)

    def damage_type_distribution(self) -> List[Dict[str, int]]:
        if self.df.empty:
            return []

        top = self.df['damage'].value_counts().to_frame(name='count').reset_index()
        top.rename(columns={'index': 'name'}, inplace=True)
        return top.to_dict(orient='records')

    def get_damage_type_distribution_chart_html(self) -> str:
        if self.df.empty:
            return ""

        data = self.df['damage'].value_counts().reset_index()
        data.columns = ['damage', 'count']
        print(data)
        fig = px.pie(data, names='damage', values='count', title='Damage Type Distribution')
        fig.update_layout(
            template='plotly_dark',
            width=700,
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        )
        return fig.to_html(full_html=False)

    def recent_events(self, limit: int = 10) -> List[Dict[str, str]]:
        if self.df.empty:
            return []

        recent = self.df.sort_values(by='date', ascending=False).head(limit)
        return recent.to_dict(orient='records')

    def refresh(self) -> None:
        self._load_csv()

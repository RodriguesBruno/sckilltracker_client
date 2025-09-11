from datetime import datetime, timezone

import pytest

from src.models.models import PlayerMonthStatistics
from src.statistics_controller import StatisticsController


@pytest.fixture
def sample_data():
    # Mock events
    return [
        {
            "date": datetime.now(tz=timezone.utc).isoformat(),
            "victim_name": "victim1",
            "killer_name": "killer1",
            "game_mode": "PU",
            "damage": "Laser"
        },
        {
            "date": datetime.now(tz=timezone.utc).isoformat(),
            "victim_name": "victim2",
            "killer_name": "killer1",
            "game_mode": "PU",
            "damage": "Missile"
        },
        {
            "date": datetime.now(tz=timezone.utc).isoformat(),
            "victim_name": "victim1",
            "killer_name": "killer2",
            "game_mode": "Arena",
            "damage": "Laser"
        },
    ]


def test_set_data_creates_dataframe(sample_data):
    controller = StatisticsController()
    controller.set_data(sample_data)

    assert not controller._df.empty
    assert len(controller._df) == 3


def test_top_killers(sample_data):
    controller = StatisticsController()
    controller.set_data(sample_data)
    killers = controller.top_killers(limit=2)

    assert len(killers) == 2
    assert killers[0]["killer_name"] == "killer1"
    assert killers[0]["count"] == 2


def test_top_victims(sample_data):
    controller = StatisticsController()
    controller.set_data(sample_data)
    victims = controller.top_victims(limit=2)

    assert len(victims) == 2
    assert victims[0]["victim_name"] == "victim1"
    assert victims[0]["count"] == 2


def test_kills_this_month_for_pilot(sample_data):
    controller = StatisticsController()
    controller.set_data(sample_data)
    result = controller.kills_for_player_this_month("killer1")

    assert isinstance(result, PlayerMonthStatistics)

    assert result.kills == 2
    assert result.player_name == "killer1"


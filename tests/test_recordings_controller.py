from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from src.models.models import PlayerEvent, PlayerProfile
from src.recordings_controller import RecordingsController


@pytest.fixture
def config(tmp_path):
    return {
        "path": str(tmp_path),
        "record_suicide": True,
        "record_own_death": False,
        "record_pu": True,
        "record_gun_rush": False,
        "record_squadron_battle": True,
        "record_arena_commander": False,
        "record_classic_race": True,
        "record_battle_royale": False,
        "record_free_flight": True,
        "record_pirate_swarm": False,
        "record_vanduul_swarm": True,
        "record_other": True
    }



def test_initialization(config):
    rc = RecordingsController(config)

    assert rc.is_record_suicide
    assert not rc.is_record_own_death
    assert rc.path == Path(config["path"])


def test_enable_disable_modes(config):
    rc = RecordingsController(config)
    assert not rc.is_record_own_death

    rc.record_own_death_enable()
    assert rc.is_record_own_death

    rc.record_own_death_disable()
    assert not rc.is_record_own_death


@pytest.mark.asyncio
async def test_must_record_video_suicide_enabled(config):
    rc = RecordingsController(config)
    event = PlayerEvent(
        damage="Suicide",
        victim_profile=PlayerProfile(name="Player1"),
        killer_profile=PlayerProfile(),
        game_mode="PU",
        date="2024-01-01T12:00:00",
        ship_name="Ship",
        using="Weapon",
        victim_zone_name="Zone",
        uuid="1234567890abcdef"
    )
    result, reason = await rc.must_record_video("Player1", event)
    assert result is True
    assert "Suicide Death is enabled" in reason


@pytest.mark.asyncio
async def test_must_record_video_other_mode(config):
    rc = RecordingsController(config)
    event = PlayerEvent(
        damage="Laser",
        game_mode="Unknown Mode",
        victim_profile=PlayerProfile(),
        killer_profile=PlayerProfile(),
        date="2024-01-01T12:00:00",
        ship_name="Ship",
        using="Weapon",
        victim_zone_name="Zone",
        uuid="1234567890abcdef"
    )
    result, reason = await rc.must_record_video("Player1", event)

    assert result is True
    assert "Other modes is enabled" in reason


@pytest.mark.asyncio
@patch("os.stat")
@patch("pathlib.Path.glob")
async def test_scan_video_files(mock_glob, mock_stat, config):
    rc = RecordingsController(config)
    fake_file = MagicMock()
    fake_file.name = "test.mp4"
    fake_file.is_file.return_value = True
    mock_stat.return_value.st_ctime = 100
    mock_glob.return_value = [fake_file]

    await rc.scan_video_files()

    assert rc.video_files_quantity() == 1
    assert "test.mp4" in rc.video_files()


def test_get_config_returns_expected_keys(config):
    rc = RecordingsController(config)
    cfg = rc.get_config()

    assert cfg["record_suicide"] is True
    assert cfg["record_pu"] is True
    assert cfg["path"] == config["path"]

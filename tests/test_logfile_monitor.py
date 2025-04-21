import pytest
from unittest.mock import mock_open, patch, MagicMock

from src.logfile_monitor import LogFileMonitor


@pytest.fixture
def config():
    return {
        "logfile_with_path": "/fake/path/log.txt",
        "frequency": 5
    }

@pytest.fixture
def monitor(config):
    return LogFileMonitor(config)

def test_initial_config(monitor):
    assert monitor.logfile_with_path == "/fake/path/log.txt"
    assert monitor.frequency == 5
    assert monitor.lines == 0
    assert not monitor.log_is_validated
    assert monitor.last_read_date == 'Never'

def test_setters(monitor):
    monitor.logfile_with_path = "/new/path.txt"
    monitor.frequency = 10
    monitor.log_is_validated = True

    assert monitor.logfile_with_path == "/new/path.txt"
    assert monitor.frequency == 10
    assert monitor.log_is_validated

def test_reset(monitor):
    monitor.log_is_validated = True
    monitor._file_position = 123
    monitor.reset()
    assert monitor._file_position == 0
    assert not monitor.log_is_validated

def test_get_config(monitor):
    config = monitor.get_config()
    assert config["logfile_with_path"] == "/fake/path/log.txt"
    assert config["frequency"] == 5

@pytest.mark.asyncio
async def test_validate_logfile(monitor):
    fake_content = [
        "<2025-04-07T15:59:37.784Z> [Notice] <OnClientConnected> Player[RedPanda] has connected. [Team_ActorFeatures][Inventory]",
        "<2025-04-08T22:01:11.249Z> [VEHICLE SPAWN] CPlayerShipRespawnManager::OnVehicleSpawned 200000001483 (RSI_Aurora_MR_200000001483) by player 2542505084000",
        "<2025-04-20T07:47:51.680Z> Loading screen for pu : SC_Frontend closed after 43.41 seconds"
    ]
    m = mock_open(read_data='\n'.join(fake_content))

    with patch("builtins.open", m), patch("src.logfile_monitor.get_date", return_value="2025-01-01"):
        pilot, ship, mode = await monitor.validate_logfile(
            pilot_name_keyword='<OnClientConnected> Player',
            ship_name_keywords=['[VEHICLE SPAWN] CPlayerShipRespawnManager:', '<Jump Drive Requesting State Change>'],
            game_mode_keywords=['> Loading screen for ', '> Mode[EA']
        )

    assert monitor.log_is_validated
    assert monitor.last_read_date == "2025-01-01"
    assert monitor.lines == len(fake_content)

@pytest.mark.asyncio
async def test_get_new_lines(monitor):
    initial_data = "line1\nline2\n"
    new_data = "line3\nline4\n"
    combined_data = initial_data + new_data

    mock_file_obj = MagicMock()
    mock_file_obj.readlines.return_value = new_data.splitlines(keepends=True)
    mock_file_obj.tell.return_value = len(combined_data)


    mock_open_obj = mock_open(read_data=combined_data)
    mock_open_obj.return_value.__enter__.return_value = mock_file_obj

    with patch("builtins.open", mock_open_obj), patch("src.logfile_monitor.get_date", return_value="2025-01-01"):

        monitor._file_position = len(initial_data)

        new_lines = await monitor.get_new_lines()

    assert new_lines == ["line3\n", "line4\n"]
    assert monitor._file_position == len(combined_data)
    assert monitor.last_read_date == "2025-01-01"
    assert monitor.lines == len(new_lines)

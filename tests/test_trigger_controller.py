import pytest
from unittest.mock import patch

from src.trigger_controller import TriggerController


@pytest.fixture
def config():
    return {
        "enabled": False,
        "selected_vendor": "nvidia",
        "vendors": [
            {"name": "nvidia", "hotkey": "alt+f10"},
            {"name": "amd", "hotkey": "ctrl+shift+s"},
            {"name": "other", "hotkey": ""}
        ]
    }

def test_initialization(config):
    vendor = 'nvidia'

    rt = TriggerController(config)

    assert rt.is_disabled
    assert rt.get_config()['selected_vendor'] == vendor
    assert len(rt.get_config()['vendors']) == 3

def test_enable_disable(config):
    rt = TriggerController(config)

    rt.enable()
    assert rt.is_enabled

    rt.disable()
    assert rt.is_disabled

def test_set_overlay_other_with_hotkey(config):
    vendor = 'other'

    rt = TriggerController(config)
    rt.set_overlay(vendor, "ctrl+shift+x")

    assert rt.get_config()['selected_vendor'] == vendor
    assert any(v["hotkey"] == "ctrl+shift+x" for v in rt.get_config()['vendors'] if v["name"] == vendor)

def test_set_overlay_other_without_hotkey(config):
    vendor = 'other'

    rt = TriggerController(config)
    rt.set_overlay("other")

    assert any(v["hotkey"] == "" for v in rt.get_config()['vendors'] if v["name"] == vendor)

def test_get_hotkey_returns_correct_value(config):
    rt = TriggerController(config)

    assert rt.get_hotkey() == "alt+f10"

@pytest.mark.asyncio
@patch("pyautogui.hotkey")
async def test_trigger_hotkey_combination(mock_hotkey, config):
    config['enabled'] = True
    config['selected_vendor'] = 'amd'

    rt = TriggerController(config)
    await rt.trigger_hotkey()

    mock_hotkey.assert_called_once_with('ctrl', 'shift', 's')

@pytest.mark.asyncio
@patch("pyautogui.hotkey")
async def test_trigger_hotkey_single_key(mock_hotkey, config):
    config['enabled'] = True
    config['selected_vendor'] = 'other'
    config['vendors'][2]['hotkey'] = 'f12'

    rt = TriggerController(config)
    await rt.trigger_hotkey()

    mock_hotkey.assert_called_once_with('f12')

@patch("pyautogui.hotkey")
def test_trigger_hotkey_disabled_does_nothing(mock_hotkey, config):
    config["enabled"] = False

    rt = TriggerController(config)
    rt.trigger_hotkey()

    mock_hotkey.assert_not_called()
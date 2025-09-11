import logging
import asyncio
from typing import Optional, List, Dict

import pyautogui


class TriggerController:
    """
    Controls Instant Replay triggering by simulating a hotkey.
    - Supports vendor presets (NVIDIA/AMD/OTHER) with configured hotkeys.
    - Allows a custom hotkey when vendor is "other".
    - Can be enabled/disabled.
    - Supports an optional trigger delay (0-10 seconds) before sending the hotkey.
    """
    def __init__(self, config: dict) -> None:
        self._enabled: bool = bool(config.get('enabled', True))
        self._selected_vendor: str = config.get('selected_vendor', 'nvidia')
        self._vendors: List[Dict] = list(config.get('vendors', []))

        self._custom_hotkey: Optional[str] = None

        try:
            self._delay_sec: int = max(0, min(10, int(config.get('delay_seconds', 0))))

        except (TypeError, ValueError):
               self._delay_sec = 0


    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def is_disabled(self) -> bool:
        return not self._enabled

    @property
    def selected_vendor(self) -> str:
        return self._selected_vendor

    # ---------------------- Controls ------------------------
    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def set_delay(self, seconds: int) -> None:
        """Clamp and set delay in seconds (0-10)."""
        try:
            self._delay_sec = max(0, min(10, int(seconds)))

        except (TypeError, ValueError):
            self._delay_sec = 0

    def set_overlay(self, gpu_vendor: str, hotkey: Optional[str] = None) -> None:
        """
        Update vendor and optional hotkey. When vendor is "other", a custom hotkey can be provided.
        If a preset vendor is chosen, its hotkey comes from the vendors list.
        """
        if gpu_vendor:
            self._selected_vendor = gpu_vendor.lower()

        # Store custom hotkey only for "other"
        if self._selected_vendor == "other":
            self._custom_hotkey = (hotkey or "").strip() or self._custom_hotkey
        else:
            self._custom_hotkey = None  # ignore custom when using presets

        # If a custom hotkey is provided for "other", also reflect it into vendors list for consistency
        if self._selected_vendor == "other" and self._custom_hotkey:
            replaced = False
            for v in self._vendors:
                if v.get("name") == "other":
                    v["hotkey"] = self._custom_hotkey
                    replaced = True
                    break

            if not replaced:
                self._vendors.append({"name": "other", "hotkey": self._custom_hotkey})

    def _vendor_hotkey(self) -> str:
        """Get hotkey from vendors list for the selected vendor; empty string if missing."""
        for vendor in self._vendors:
            if vendor.get("name") == self._selected_vendor:
                return str(vendor.get("hotkey", "")).strip()
        return ""

    def get_hotkey(self) -> str:
        """Resolve the effective hotkey based on selected vendor and custom override."""
        if self._selected_vendor == "other" and self._custom_hotkey:
            return self._custom_hotkey
        return self._vendor_hotkey()

    async def trigger_hotkey(self) -> None:
        """
        Trigger the instant replay hotkey.
        - Waits _delay_sec seconds before sending, if configured.
        - Splits combination like 'alt+f10' into pyautogui.hotkey('alt','f10').
        """
        if not self._enabled:
            logging.info("[TRIGGER CONTROLLER] Skipped trigger: controller disabled")
            return

        # optional delay
        if self._delay_sec > 0:
            await asyncio.sleep(self._delay_sec)

        hotkey: str = self.get_hotkey()
        if not hotkey:
            logging.warning("[TRIGGER CONTROLLER] No hotkey configured for vendor '%s'", self._selected_vendor)
            return

        # Send hotkey
        if '+' in hotkey:
            hotkey_combinations: List[str] = [key.strip() for key in hotkey.split('+') if key.strip()]
            pyautogui.hotkey(*hotkey_combinations)
        else:
            pyautogui.hotkey(hotkey)

        logging.info("[TRIGGER CONTROLLER] Triggered Hotkey: %s, Vendor: %s, Delay: %ss",
                     hotkey, self._selected_vendor, self._delay_sec)

    def get_config(self) -> dict:
        return {
            "enabled": self._enabled,
            "selected_vendor": self._selected_vendor,
            "vendors": self._vendors,
            "delay_seconds": self._delay_sec
        }

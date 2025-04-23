import logging
import pyautogui

class TriggerController:
    def __init__(self, config: dict) -> None:
        self._enabled: bool = config.get('enabled')
        self._selected_vendor: str = config.get('selected_vendor')
        self._vendors: list[dict] = config.get('vendors')

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    @property
    def selected_vendor(self) -> str:
        return self._selected_vendor

    @property
    def is_disabled(self) -> bool:
        return not self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def set_overlay(self, gpu_vendor: str, hotkey: str = None) -> None:

        for vendor in self._vendors:
            vendor_name = vendor.get('name')

            if vendor_name == gpu_vendor:
                if hotkey and vendor_name == 'other':
                    if vendor.get('hotkey') != hotkey:
                        vendor['hotkey'] = hotkey

            if not hotkey and vendor_name == 'other':
                vendor['hotkey'] = ''

        self._selected_vendor = gpu_vendor

    def get_hotkey(self):
        for vendor in self._vendors:
            if vendor.get('name') == self._selected_vendor:
                return vendor.get('hotkey')



    async def trigger_hotkey(self) -> None:
        if self._enabled:
            hotkey: str = self.get_hotkey()
            if '+' in hotkey:
                hotkey_combinations: list[str] = [key for key in hotkey.split('+')]
                pyautogui.hotkey(*hotkey_combinations)

            else:
                pyautogui.hotkey(hotkey)

            logging.info(f'[TRIGGER CONTROLLER] Triggered Hotkey: {hotkey}, Vendor: {self._selected_vendor}')

    def get_config(self) -> dict:
        return {
            "enabled": self._enabled,
            "selected_vendor": self._selected_vendor,
            "vendors": self._vendors
        }

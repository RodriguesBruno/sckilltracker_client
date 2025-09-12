import os
import ctypes
import threading
from pathlib import Path

import psutil
import pystray
import webbrowser
from PIL import Image

from src.utils import resource_path


def load_tray_icon():
    icon_path: Path = Path(resource_path("static/sckticon.ico"))  # Update the path as needed
    if not icon_path.exists():
        raise FileNotFoundError(f"Tray icon not found at: {icon_path}")

    return Image.open(icon_path)

def hide_system_tray_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def show_system_tray_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def setup_system_tray(app_url: str):
    def on_open_ui(icon, item):
        webbrowser.open(app_url)

    def on_hide_console(icon, item):
        hide_system_tray_console()

    def on_show_console(icon, item):
        show_system_tray_console()

    def on_exit(icon, item):
        show_system_tray_console()
        icon.stop()
        parent = psutil.Process(os.getpid())
        for child in parent.children(recursive=True):
            child.kill()

        parent.kill()

    icon = pystray.Icon("app")
    icon.icon = load_tray_icon()
    icon.menu = pystray.Menu(
        pystray.MenuItem("Open UI", on_open_ui),
        pystray.MenuItem("Hide Console", on_hide_console),
        pystray.MenuItem("Show Console", on_show_console),
        pystray.MenuItem("Exit", on_exit)
    )

    threading.Thread(target=icon.run, daemon=True).start()
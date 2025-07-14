import logging
from enum import Enum
import requests
import sys
import json
import os
from multiprocessing import Queue
from multiprocessing.managers import ValueProxy
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGraphicsOpacityEffect,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import (
    Qt,
    QTimer,
    QSize,
    QPropertyAnimation,
    QRect
)

CONFIG_PATH = "config.json"

class OverlayPosition(str, Enum):
    TOP_LEFT = "top-left"
    TOP_RIGHT = "top-right"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_RIGHT = "bottom-right"


class OverlayColor(str, Enum):
    BLACK = "black"
    WHITE = "white"
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    CYAN = "cyan"
    MAGENTA = "magenta"
    GRAY = "gray"
    DARK_GRAY = "darkgray"
    LIGHT_GRAY = "lightgray"
    ORANGE = "orange"
    PURPLE = "purple"
    PINK = "pink"
    LIME = "lime"
    TEAL = "teal"
    NAVY = "navy"
    MAROON = "maroon"
    OLIVE = "olive"
    SILVER = "silver"


class Overlay(QWidget):
    def __init__(self, position_value, color_value, font_size_value, overlay_enabled,
                 overlay_on_suicide, overlay_on_own_death, overlay_on_pu,
                 overlay_on_gun_rush, overlay_on_squadron_battle, overlay_on_arena_commander,
                 overlay_on_classic_race, overlay_on_battle_royale, overlay_on_free_flight,
                 overlay_on_pirate_swarm, overlay_on_vanduul_swarm, overlay_on_other,
                 queue: Queue) -> None:
        super().__init__()

        self.position_value = position_value
        self.color_value = color_value
        self.font_size_value = font_size_value
        self._enabled = overlay_enabled
        self._on_suicide = overlay_on_suicide
        self._on_own_death = overlay_on_own_death
        self._on_pu = overlay_on_pu
        self._on_gun_rush = overlay_on_gun_rush
        self._on_squadron_battle = overlay_on_squadron_battle
        self._on_arena_commander = overlay_on_arena_commander
        self._on_classic_race = overlay_on_classic_race
        self._on_battle_royale = overlay_on_battle_royale
        self._on_free_flight = overlay_on_free_flight
        self._on_pirate_swarm = overlay_on_pirate_swarm
        self._on_vanduul_swarm = overlay_on_vanduul_swarm
        self._on_other = overlay_on_other
        self.queue = queue

        self.current_position = OverlayPosition(self.position_value.value)
        self.current_color = OverlayColor(self.color_value.value)
        self.current_font_size = int(self.font_size_value.value)

        self.entries = []
        self.kill_streak_entry = None

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: transparent;")

        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1.0)

        self.fade_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(1000)
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.finished.connect(self.hide)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        self.kill_streak_hide_timer = QTimer()
        self.kill_streak_hide_timer.setSingleShot(True)
        self.kill_streak_hide_timer.timeout.connect(self.hide_kill_streak_entry)

        self.default_width = 700
        self.default_height = 200
        self.resize(self.default_width, self.default_height)

        self.poll_timer = QTimer()
        self.poll_timer.timeout.connect(self.poll_queue)
        self.poll_timer.start(100)

        self.position_check_timer = QTimer()
        self.position_check_timer.timeout.connect(self.check_position)
        self.position_check_timer.start(1000)

        self.color_check_timer = QTimer()
        self.color_check_timer.timeout.connect(self.check_color)
        self.color_check_timer.start(1000)

        self.font_size_check_timer = QTimer()
        self.font_size_check_timer.timeout.connect(self.check_font_size)
        self.font_size_check_timer.start(1000)

        self.animations = []
        QTimer.singleShot(100, self.move_to_position)

    def reload_config(self) -> None:
        if not os.path.exists(CONFIG_PATH):
            return
        try:
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)

            overlay_cfg = config.get("overlay", {})

            self._enabled.value = overlay_cfg.get("enabled", True)
            self.color_value.value = overlay_cfg.get("font_color", "white")
            self.font_size_value.value = overlay_cfg.get("font_size", 18)
            self.position_value.value = overlay_cfg.get("position", "top-right")

            self._on_suicide.value = overlay_cfg.get("on_suicide", True)
            self._on_own_death.value = overlay_cfg.get("on_own_death", True)
            self._on_pu.value = overlay_cfg.get("on_pu", True)
            self._on_gun_rush.value = overlay_cfg.get("on_gun_rush", True)
            self._on_squadron_battle.value = overlay_cfg.get("on_squadron_battle", True)
            self._on_arena_commander.value = overlay_cfg.get("on_arena_commander", True)
            self._on_classic_race.value = overlay_cfg.get("on_classic_race", True)
            self._on_battle_royale.value = overlay_cfg.get("on_battle_royale", True)
            self._on_free_flight.value = overlay_cfg.get("on_free_flight", True)
            self._on_pirate_swarm.value = overlay_cfg.get("on_pirate_swarm", True)
            self._on_vanduul_swarm.value = overlay_cfg.get("on_vanduul_swarm", True)
            self._on_other.value = overlay_cfg.get("on_other", True)

        except Exception as e:
            logging.error(f"Error loading config.json: {e}")

    def poll_queue(self) -> None:
        while not self.queue.empty():
            data = self.queue.get()
            if isinstance(data, dict) and 'uuid' in data:
                self.display_notification(data)
            elif isinstance(data, dict) and 'kill_streak' in data:
                self.update_kill_streak(data['kill_streak'])

    def update_kill_streak(self, count: int) -> None:
        if count <= 0:
            self.hide_kill_streak_entry()
            return

        text = f"<b>Kill Streak: {count}</b>"

        if self.kill_streak_entry:
            self.layout.removeWidget(self.kill_streak_entry)
            self.kill_streak_entry.setParent(None)

        entry_widget = QWidget()
        entry_layout = QHBoxLayout()
        entry_layout.setContentsMargins(0, 0, 0, 0)
        entry_layout.setSpacing(5)

        image_label = QLabel()
        image_label.setFixedSize(125, 125)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        pixmap = QPixmap(125, 125)
        pixmap.fill(Qt.transparent)
        image_label.setPixmap(pixmap)

        text_label = QLabel(text)
        text_label.setStyleSheet(f"color: {self.current_color.value}; background-color: transparent;")
        text_label.setFont(QFont("Consolas", self.current_font_size + 4))
        text_label.setWordWrap(True)
        text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        entry_layout.addWidget(image_label)
        entry_layout.addWidget(text_label)
        entry_widget.setLayout(entry_layout)
        entry_widget.label_ref = text_label

        self.layout.insertWidget(0, entry_widget)
        self.kill_streak_entry = entry_widget
        self.kill_streak_hide_timer.start(5000)

    def hide_kill_streak_entry(self) -> None:
        if self.kill_streak_entry:
            self.layout.removeWidget(self.kill_streak_entry)
            self.kill_streak_entry.setParent(None)
            self.kill_streak_entry = None

    def check_position(self) -> None:
        if self.position_value.value != self.current_position.value:
            self.current_position = OverlayPosition(self.position_value.value)
            self.move_to_position()

    def check_color(self) -> None:
        if self.color_value.value != self.current_color.value:
            self.current_color = OverlayColor(self.color_value.value)
            if self.kill_streak_entry:
                self.kill_streak_entry.label_ref.setStyleSheet(f"color: {self.current_color.value}; background-color: transparent;")
            for entry in self.entries:
                entry.label_ref.setStyleSheet(f"color: {self.current_color.value}; background-color: transparent;")

    def check_font_size(self) -> None:
        new_size = int(self.font_size_value.value)
        if new_size != self.current_font_size:
            self.current_font_size = new_size
            if self.kill_streak_entry:
                self.kill_streak_entry.label_ref.setFont(QFont("Consolas", new_size + 4))
            for entry in self.entries:
                entry.label_ref.setFont(QFont("Consolas", new_size))

    def move_to_position(self) -> None:
        screen: QRect = QApplication.primaryScreen().geometry()
        margin: int = 20
        is_right: bool = "right" in self.current_position.value
        is_bottom: bool = "bottom" in self.current_position.value
        x: int = screen.width() - self.width() - margin if is_right else margin
        y: int = screen.height() - self.height() - margin if is_bottom else margin
        self.setGeometry(x, y, self.width(), self.height())

    def display_notification(self, data: dict) -> None:
        self.reload_config()
        if 'uuid' in data and self._enabled.value:
            try:
                killer = data.get('killer_profile', {})
                victim = data.get('victim_profile', {})
                org = victim.get('org', {})
                damage = data.get('damage', '')

                if 'Suicide' in damage:
                    return

                killer_name = f"<b>{killer.get('name', '')}</b>"
                victim_name = f"<b>{victim.get('name', '')}</b>"
                org_name = f"<b>{org.get('name', '')}</b>"
                enlisted_date = f"<b>{victim.get('enlisted_date')}</b>"

                if '-R-' in org_name or org_name == '-':
                    text = f"{killer_name} killed {victim_name}, enlisted {enlisted_date}"
                else:
                    text = f"{killer_name} killed {victim_name} from {org_name}, enlisted {enlisted_date}"

                entry_widget = QWidget()
                entry_layout = QHBoxLayout()
                entry_layout.setContentsMargins(0, 0, 0, 0)
                entry_layout.setSpacing(5)

                image_label = QLabel()
                image_label.setFixedSize(125, 125)
                image_label.setAlignment(Qt.AlignCenter)
                image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                img_url = victim.get("icon_url")
                if img_url:
                    try:
                        response = requests.get(img_url)
                        pixmap = QPixmap()
                        pixmap.loadFromData(response.content)
                        scaled = pixmap.scaled(QSize(125, 125), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        image_label.setPixmap(scaled)
                    except Exception:
                        pass

                text_label = QLabel(text)
                text_label.setStyleSheet(f"color: {self.current_color.value}; background-color: transparent;")
                text_label.setFont(QFont("Consolas", self.current_font_size))
                text_label.setWordWrap(True)
                text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

                entry_layout.addWidget(image_label)
                entry_layout.addWidget(text_label)
                entry_widget.setLayout(entry_layout)
                entry_widget.label_ref = text_label

                self.layout.insertWidget(0, entry_widget)
                self.entries.insert(0, entry_widget)
                self.show()
                self.raise_()
                self.move_to_position()

                if len(self.entries) > 5:
                    oldest = self.entries.pop()
                    self.remove_entry(oldest)

                QTimer.singleShot(8000, lambda: self.remove_entry(entry_widget))

            except Exception as e:
                logging.error(f"Overlay error: {e}")

    def remove_entry(self, entry_widget: QWidget) -> None:
        fade_effect = QGraphicsOpacityEffect(entry_widget)
        entry_widget.setGraphicsEffect(fade_effect)

        fade_anim = QPropertyAnimation(fade_effect, b"opacity")
        fade_anim.setDuration(500)
        fade_anim.setStartValue(1.0)
        fade_anim.setEndValue(0.0)

        start_rect: QRect = entry_widget.geometry()
        end_rect: QRect = start_rect.translated(0, -20)

        slide_anim = QPropertyAnimation(entry_widget, b"geometry")
        slide_anim.setDuration(500)
        slide_anim.setStartValue(start_rect)
        slide_anim.setEndValue(end_rect)

        self.animations.append(fade_anim)
        self.animations.append(slide_anim)

        def finalize_removal() -> None:
            self.layout.removeWidget(entry_widget)
            entry_widget.setParent(None)
            if entry_widget in self.entries:
                self.entries.remove(entry_widget)
            self.animations.remove(fade_anim)
            self.animations.remove(slide_anim)

        fade_anim.finished.connect(finalize_removal)
        fade_anim.start()
        slide_anim.start()

    def fade_out(self) -> None:
        if self.fade_animation.state() == QPropertyAnimation.Running:
            self.fade_animation.stop()
        self.fade_animation.start()


def run_overlay(position_value: ValueProxy, color_value: ValueProxy, font_size_value: ValueProxy,
                overlay_enabled: ValueProxy, overlay_on_suicide: ValueProxy, overlay_on_own_death: ValueProxy,
                overlay_on_pu: ValueProxy, overlay_on_gun_rush: ValueProxy, overlay_on_squadron_battle: ValueProxy,
                overlay_on_arena_commander: ValueProxy, overlay_on_classic_race: ValueProxy,
                overlay_on_battle_royale: ValueProxy, overlay_on_free_flight: ValueProxy,
                overlay_on_pirate_swarm: ValueProxy, overlay_on_vanduul_swarm: ValueProxy,
                overlay_on_other: ValueProxy, queue: Queue) -> None:
    app = QApplication(sys.argv)
    overlay = Overlay(position_value, color_value, font_size_value, overlay_enabled,
                      overlay_on_suicide, overlay_on_own_death, overlay_on_pu, overlay_on_gun_rush,
                      overlay_on_squadron_battle, overlay_on_arena_commander, overlay_on_classic_race,
                      overlay_on_battle_royale, overlay_on_free_flight, overlay_on_pirate_swarm,
                      overlay_on_vanduul_swarm, overlay_on_other, queue)
    overlay.show()
    sys.exit(app.exec_())

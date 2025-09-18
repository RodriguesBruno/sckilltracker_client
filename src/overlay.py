import sys
import logging
import requests
from enum import Enum
from typing import Optional
from multiprocessing import Queue
from multiprocessing.managers import ValueProxy
from requests.exceptions import RequestException
from PyQt5.QtCore import (
    Qt,
    QTimer,
    QSize,
    QPropertyAnimation,
    QRect
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGraphicsOpacityEffect,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy
)


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


def get_player_event_overlay_text(killer: dict, victim: dict, org: dict) -> str:
    killer_name = f"<b>{killer.get('name', '')}</b>"
    victim_name = f"<b>{victim.get('name', '')}</b>"
    org_name = f"<b>{org.get('name', '')}</b>"
    enlisted_date = f"<b>{victim.get('enlisted_date')}</b>"

    if '-R-' in org_name or org_name == '-':
        return f"{killer_name} killed {victim_name}, enlisted {enlisted_date}"

    return  f"{killer_name} killed {victim_name} from {org_name}, enlisted {enlisted_date}"


def get_layout() -> QHBoxLayout:
    entry_layout: QHBoxLayout = QHBoxLayout()
    entry_layout.setContentsMargins(0, 0, 0, 0)
    entry_layout.setSpacing(5)

    return entry_layout

def get_image_label() -> QLabel:
    image_label: QLabel = QLabel()
    image_label.setFixedSize(125, 125)
    image_label.setAlignment(Qt.AlignCenter) # type: ignore
    image_label.setSizePolicy(QSizePolicy.Policy(QSizePolicy.Fixed), QSizePolicy.Policy(QSizePolicy.Fixed))

    return image_label

def get_text_label(text: str, color: str, size: int) -> QLabel:
    text_label: QLabel = QLabel(text)
    text_label.setStyleSheet(f"color: {color}; background-color: transparent;")
    text_label.setFont(QFont("Consolas", size))
    text_label.setWordWrap(True)
    text_label.setSizePolicy(QSizePolicy.Policy(QSizePolicy.Expanding), QSizePolicy.Policy(QSizePolicy.Preferred))

    return text_label


class Overlay(QWidget):
    def __init__(self, position_value, color_value, font_size_value, queue: Queue) -> None:
        super().__init__()

        self.position_value = position_value
        self.color_value = color_value
        self.font_size_value = font_size_value
        self.queue = queue

        self.current_position = OverlayPosition(self.position_value.value)
        self.current_color = OverlayColor(self.color_value.value)
        self.current_font_size = int(self.font_size_value.value)

        self.entries = []

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool) # type: ignore
        self.setAttribute(Qt.WidgetAttribute(Qt.WA_TranslucentBackground))
        self.setStyleSheet("background-color: transparent;")

        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1.0)

        self.fade_animation: QPropertyAnimation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_animation.setDuration(1000)
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.finished.connect(self.hide)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        self.default_width = 700
        self.default_height = 200
        self.resize(self.default_width, self.default_height)

        self.poll_timer: QTimer = QTimer()
        self.poll_timer.timeout.connect(self.poll_queue)
        self.poll_timer.start(100)

        self.position_check_timer: QTimer = QTimer()
        self.position_check_timer.timeout.connect(self.check_position)
        self.position_check_timer.start(1000)

        self.color_check_timer: QTimer = QTimer()
        self.color_check_timer.timeout.connect(self.check_color)
        self.color_check_timer.start(1000)

        self.font_size_check_timer: QTimer = QTimer()
        self.font_size_check_timer.timeout.connect(self.check_font_size)
        self.font_size_check_timer.start(1000)

        self.animations = []
        QTimer.singleShot(100, self.move_to_position)

    def poll_queue(self) -> None:

        while not self.queue.empty():
            data = self.queue.get()
            if isinstance(data, dict):
                widget: Optional[QWidget] = None

                if 'kill_streak' in data:
                    widget: QWidget = self.get_kill_streak_widget(data=data)

                elif 'uuid' in data:
                    widget: Optional[QWidget] = self.get_player_event_widget(data=data)

                if widget:
                    self.display_widget(widget)


    def check_position(self) -> None:
        if self.position_value.value != self.current_position.value:
            self.current_position = OverlayPosition(self.position_value.value)
            self.move_to_position()

    def check_color(self) -> None:
        if self.color_value.value != self.current_color.value:
            self.current_color = OverlayColor(self.color_value.value)
            for entry in self.entries:
                entry.label_ref.setStyleSheet(f"color: {self.current_color.value}; background-color: transparent;")

    def check_font_size(self) -> None:
        new_size = int(self.font_size_value.value)
        if new_size != self.current_font_size:
            self.current_font_size = new_size

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

    def display_widget(self, widget: QWidget) -> None:
        try:
            self.layout.insertWidget(0, widget)
            self.entries.insert(0, widget)
            self.show()
            self.raise_()
            self.move_to_position()

            if len(self.entries) > 5:
                oldest = self.entries.pop()
                self.remove_entry(oldest)

            QTimer.singleShot(8000, lambda: self.remove_entry(widget))

        except Exception as e:
            logging.error(f"Overlay error: {e}")

    def remove_entry(self, entry_widget: QWidget) -> None:
        fade_effect = QGraphicsOpacityEffect(entry_widget)
        entry_widget.setGraphicsEffect(fade_effect)

        fade_anim: QPropertyAnimation  = QPropertyAnimation(fade_effect, b"opacity")
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

    def get_kill_streak_widget(self, data: dict) -> QWidget:
        count = data['kill_streak']
        text = f"<b>Kill Streak: {count}</b>"

        widget: QWidget = QWidget()
        layout: QHBoxLayout = get_layout()
        image_label: QLabel = get_image_label()

        pixmap = QPixmap(125, 125)
        pixmap.fill(Qt.transparent)
        image_label.setPixmap(pixmap)

        text_label: QLabel = get_text_label(
            text=text,
            color=self.current_color.value,
            size=self.current_font_size + 4
        )

        layout.addWidget(image_label)
        layout.addWidget(text_label)
        widget.setLayout(layout)
        widget.label_ref = text_label

        return widget

    def get_player_event_widget(self, data: dict) -> Optional[QWidget]:
        killer = data.get('killer_profile', {})
        victim = data.get('victim_profile', {})
        org = victim.get('org', {})
        damage = data.get('damage', '')

        if 'Suicide' in damage:
            return None

        text: str = get_player_event_overlay_text(killer=killer, victim=victim, org=org)

        widget: QWidget = QWidget()
        layout: QHBoxLayout = get_layout()
        image_label: QLabel = get_image_label()

        img_url = victim.get("icon_url")
        if img_url:
            try:
                response = requests.get(img_url, timeout=5)
                response.raise_for_status()

                pixmap = QPixmap()
                if pixmap.loadFromData(response.content):
                    scaled = pixmap.scaled(QSize(125, 125), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    image_label.setPixmap(scaled)
                else:
                    image_label.clear()

            except RequestException as e:
                logging.error(f"Request failed: {e}")

            except Exception as e:
                logging.error(f"Unexpected error loading image: {e}")

        text_label: QLabel = get_text_label(
            text=text,
            color=self.current_color.value,
            size=self.current_font_size
        )

        layout.addWidget(image_label)
        layout.addWidget(text_label)
        widget.setLayout(layout)
        widget.label_ref = text_label

        return widget

def run_overlay(position_value: ValueProxy, color_value: ValueProxy, font_size_value: ValueProxy, queue: Queue) -> None:
    app = QApplication(sys.argv)
    overlay = Overlay(position_value, color_value, font_size_value, queue)
    overlay.show()
    sys.exit(app.exec_())

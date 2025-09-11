from pydantic import BaseModel, HttpUrl, field_validator

from src.overlay import OverlayPosition, OverlayColor


class SettingsForm(BaseModel):
    local_api_ip_address: str
    local_api_port: int
    api_url: HttpUrl
    logfile: str
    frequency: int
    overlay_position: str
    overlay_font_color: str
    overlay_font_size: int
    trigger_delay: int


    @field_validator("local_api_port", mode='before')
    @classmethod
    def port_must_be_valid(cls, value):
        try:
            value = int(value)

        except Exception:
            raise ValueError('Port must be Integer between 1 and 65535')

        if not (1 <= value <= 65535):
            raise ValueError("Port must be between 1 and 65535")

        return value


    @field_validator("frequency", mode='before')
    @classmethod
    def frequency_must_be_positive(cls, value):
        try:
            value = int(value)

        except Exception:
            raise ValueError('Frequency must be Integer between 5 and 120')

        if not (5 <= value <= 120):
            raise ValueError("Frequency must be between 5 and 120 seconds")

        return value


    @field_validator("overlay_position", mode='before')
    @classmethod
    def position_must_be_from_value_overlay_position(cls, value):
        allowed_values = [entry.value for entry in OverlayPosition]

        if value not in allowed_values:
            raise ValueError(f'Allowed positions are: {allowed_values}')

        return value


    @field_validator("overlay_font_color", mode='before')
    @classmethod
    def font_color_must_be_from_value_overlay_color(cls, value):
        allowed_values = [entry.value for entry in OverlayColor]

        if value not in allowed_values:
            raise ValueError(f'Allowed colors are: {allowed_values}')

        return value


    @field_validator("overlay_font_size", mode="before")
    @classmethod
    def font_size_must_be_valid(cls, value):
        allowed_values = list(range(5, 31))
        try:
            value = int(value)

        except (TypeError, ValueError):
            raise ValueError("Font size must be an integer")

        if value not in allowed_values:
            raise ValueError(f"Allowed sizes are: {allowed_values}")

        return value

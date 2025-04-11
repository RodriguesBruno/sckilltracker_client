from pydantic import BaseModel, HttpUrl, field_validator


class SettingsForm(BaseModel):
    local_api_ip_address: str
    local_api_port: int
    api_url: HttpUrl
    logfile: str
    frequency: int

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

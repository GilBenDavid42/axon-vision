from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    video_path: Path = Field(validation_alias="VIDEO_PATH")

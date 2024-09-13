from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    video_path: Field(Path, validation_alias="VIDEO_PATH")

import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

base_path = pathlib.Path(__file__).parent.parent.resolve()


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.app_name}}"
    app_domain: str = os.environ.get('APP_DOMAIN')
    app_env: str = os.environ.get('APP_ENV')
    app_port: int = int(os.environ.get('APP_PORT'))
    dev_mode: bool = os.environ.get('DEV_MODE')

@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
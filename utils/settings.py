from pydantic.tools import lru_cache

from utils import config


@lru_cache()
def get_settings():
    return config.Settings()


settings = get_settings()

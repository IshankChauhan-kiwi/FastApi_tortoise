"""
Database connection
"""
from utils.settings import settings


TORTOISE_ORM = {
    "connections": {
          # Dict format for connection
          "default": {
              "engine": "tortoise.backends.asyncpg",
              "credentials": {
                  "host": settings.DB_HOST,
                  "port": settings.DB_PORT,
                  "user": settings.DB_USERNAME,
                  "password": settings.DB_PASSWORD,
                  "database": settings.DB_NAME,
              },
          },
      },
    "apps": {
        "apps": {
            "models": [
                "apps.app.models",
                "apps.accounts.models",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}


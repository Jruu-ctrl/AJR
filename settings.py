import pathlib
import os
from dotenv import load_dotenv
import logging
from logging.config import dictConfig
import discord

load_dotenv()

DISCORD_API_SECRET=os.getenv("DISCORD_API_TOKEN")

BASE_DIR=pathlib.Path(__file__).parent

CMDS_DIR=BASE_DIR / "cmds"

GUILDS_ID=discord.Object(id=int(os.getenv("GUILD")))

ELEVEN_CLIENT=os.getenv("ELEVEN_API_KEY")

LOGGING_CONFIG= {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s: %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        },
        "file": {  # Saves logs to a file
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": "logs/infos.log",
            "encoding": "utf8"
        }
    },
    "loggers": {
        "discord": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "bot": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)
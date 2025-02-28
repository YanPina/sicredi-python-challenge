import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(filename)s - %(funcName)s - "
            "%(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(filename)s - %(funcName)s - "
            "%(levelname)s - %(lineno)d - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "detailed",
            "level": "INFO",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


def setup_logging() -> None:
    dictConfig(LOGGING_CONFIG)


setup_logging()

logger = logging.getLogger("app")

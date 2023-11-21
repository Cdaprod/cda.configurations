# logging_config.py

import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'CredKeeper': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}

class LoggingConfig:
    def __init__(self):
        # Apply the initial logging configuration
        logging.config.dictConfig(LOGGING_CONFIG)

    def set_log_level(self, logger_name, level):
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

    def add_file_handler(self, logger_name, file_path, level=None):
        handler = logging.FileHandler(file_path)
        handler.setFormatter(logging.Formatter(LOGGING_CONFIG['formatters']['standard']['format']))
        if level:
            handler.setLevel(level)
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)

# Usage example
config = LoggingConfig()
config.set_log_level('CredKeeper', 'DEBUG')
config.add_file_handler('CredKeeper', './logs/logfile.log', 'WARNING')

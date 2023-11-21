import os

class EnvironmentConfig:
    def __init__(self):
        self.env = os.getenv('ENVIRONMENT', 'dev').lower()
        self.config = self.load_environment_config()

    def load_environment_config(self):
        if self.env == 'prod':
            from .environment_config.config_prod import ProdConfig
            return ProdConfig()
        elif self.env == 'test':
            from .environment_config.config_test import TestConfig
            return TestConfig()
        else:
            # Default to development config
            from .environment_config.config_dev import DevConfig
            return DevConfig()

    def get_config(self):
        return self.config

# Usage Example:
# config = EnvironmentConfig().get_config()
# database_uri = config.DATABASE_URI

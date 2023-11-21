from environment_config import EnvironmentConfig
from data_sources import DataSourceConfig
from etl_config import ETLConfig
from security_config import SecurityConfig
from performance_config import PerformanceConfig
from monitoring_config import MonitoringConfig
from logging_config import LoggingConfig

class ConfigurationEngine:
    def __init__(self):
        # Load the environment-specific configuration
        self.environment_config = EnvironmentConfig().get_config()
        
        # Initialize configuration objects
        self.config_objects = {
            'data_source': DataSourceConfig(),
            'etl': ETLConfig(),
            'security': SecurityConfig(),
            'performance': PerformanceConfig(),
            'monitoring': MonitoringConfig(),
            'logging': LoggingConfig()
        }

    def get_config(self, config_name):
        """Generic method to return a specific configuration."""
        return self.config_objects.get(config_name)

    # Individual getters for specific configurations
    def get_data_source_config(self):
        return self.get_config('data_source')

    def get_etl_config(self):
        return self.get_config('etl')

    def get_security_config(self):
        return self.get_config('security')

    def get_performance_config(self):
        return self.get_config('performance')

    def get_monitoring_config(self):
        return self.get_config('monitoring')

    def get_logging_config(self):
        return self.get_config('logging')

    # Additional utility methods as needed
    # Example: Method to reload a specific config
    def reload_config(self, config_name):
        """Reloads the specified configuration."""
        if config_name in self.config_objects:
            # Assuming each config class has a reload or similar method
            self.config_objects[config_name].reload()

# Usage
config_engine = ConfigurationEngine()
data_source_config = config_engine.get_data_source_config()
# Use data_source_config as needed

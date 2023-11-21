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
        
        # Load other configurations
        self.data_source_config = DataSourceConfig()
        self.etl_config = ETLConfig()
        self.security_config = SecurityConfig()
        self.performance_config = PerformanceConfig()
        self.monitoring_config = MonitoringConfig()
        self.logging_config = LoggingConfig()

    def get_data_source_config(self):
        # Return data source configuration
        return self.data_source_config

    def get_etl_config(self):
        # Return ETL configuration
        return self.etl_config

    # Similarly, add getters for other configurations

# Usage
config_engine = ConfigurationEngine()
data_source_config = config_engine.get_data_source_config()
# Use data_source_config as needed
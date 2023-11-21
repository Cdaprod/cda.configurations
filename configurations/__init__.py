from abc import ABC, abstractmethod

# Base abstract class for configurations
class BaseConfig(ABC):
    @abstractmethod
    def load_config(self):
        pass

    @abstractmethod
    def validate_config(self):
        pass

# Importing configuration classes
from .data_sources import DataSourceConfig
from .etl_config import ETLConfig
from .security_config import SecurityConfig
from .performance_config import PerformanceConfig
from .monitoring_config import MonitoringConfig
from .logging_config import LoggingConfig

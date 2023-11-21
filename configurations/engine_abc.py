from abc import ABC, abstractmethod

class ConfigurationEngineABC(ABC):
    @abstractmethod
    def load_environment_config(self):
        """Load the environment-specific configuration"""
        pass

    @abstractmethod
    def get_data_source_config(self):
        """Return data source configuration"""
        pass

    @abstractmethod
    def get_etl_config(self):
        """Return ETL configuration"""
        pass

    @abstractmethod
    def get_security_config(self):
        """Return security configuration"""
        pass

    @abstractmethod
    def get_performance_config(self):
        """Return performance configuration"""
        pass

    @abstractmethod
    def get_monitoring_config(self):
        """Return monitoring configuration"""
        pass

    @abstractmethod
    def get_logging_config(self):
        """Return logging configuration"""
        pass

    # Add other abstract methods as necessary for your configuration needs

from configurations import DataSourceConfig, ETLConfig, ...

def setup_environment(env="dev"):
    # Instantiate configuration objects and call their methods
    data_source_config = DataSourceConfig()
    data_source_config.load_config()
    data_source_config.validate_config()

    # Repeat for other configuration types

if __name__ == "__main__":
    setup_environment()

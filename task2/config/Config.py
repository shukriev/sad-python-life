import os
import typing
import confuse

from task2.exception.ConfigException import ConfigException, ConfigNotExisting
from task2.helper.DictHelper import DictHelper


class Loader(object):
    CONFIG_FILE: typing.Optional[str] = None

    @staticmethod
    def load(config_file=None):
        """Static Configuration Loader"""

        print(f'Configuration file is going go be loaded {config_file}')

        if config_file is None:
            config_file = Loader.get_required_env_var("CONFIG_FILE")
            print(f'Environment specified file being loaded {config_file}')

        assert os.path.exists(config_file)
        with open(config_file, 'r') as f:
            try:
                yml_configuration = confuse.yaml.safe_load(f)
                print(yml_configuration)
                return config_file, yml_configuration
            except confuse.yaml.YAMLError as exc:
                print(exc)
            finally:
                f.close()

    @staticmethod
    def get_config_file() -> str:
        return Loader.CONFIG_FILE

    @staticmethod
    def get_required_env_var(environment_variable: str) -> str:
        if environment_variable not in os.environ:
            raise ConfigException(f"Please set the {environment_variable} environment variable")
        return os.environ[environment_variable]


class Config(object):
    _CONFIG: typing.Optional[dict] = Loader().load()[1]

    @staticmethod
    def get_configuration(keyword: str):
        """Return configuration from given key"""
        assert Config._CONFIG

        configuration_value = DictHelper.recursive_search(Config._CONFIG, keyword)

        if configuration_value is None:
            raise ConfigNotExisting(f"Configuration: {keyword} not found")

        return configuration_value

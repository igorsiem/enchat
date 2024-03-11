from urllib.parse import urlparse
from toga.validators import BooleanValidator
from pathlib import Path
import json
import logging

class SystemConfiguration:
    """A data structure for holding system config information
    """

    CONFIG_FILE_NAME = 'enchat_config.json'

    SERVER_ADDRESS_TAGNAME = 'server_address'
    DEFAULT_SERVER_ADDRESS = "http://localhost:1234"
        
    class ServerAddressValidator(BooleanValidator):
        """Validator for the server address

        This validator checks that the given scheme is http or https.

        TODO Tests for this validator
        """

        def is_valid(self, input_string : str) -> bool:            
            return SystemConfiguration.ServerAddressValidator.validate(input_string)
        
        @staticmethod
        def validate(input_string : str) -> bool:
            return (urlparse(input_string, scheme='http').scheme in ['http', 'https'])
        
        ERROR_MESSAGE="must be a valid http(s) URL"

    @property
    def server_address(self) -> str:
        """The address of the server, including optional port number
        """
        return self._server_address
    
    @server_address.setter
    def server_address(self, value : str):
        # Do validation with throw
        if SystemConfiguration.ServerAddressValidator.validate(value) is False:
            raise RuntimeError(f"invalid URL \"{value}\" - {SystemConfiguration.ServerAddressValidator.ERROR_MESSAGE}")
        
        self._server_address = value

    def load(self):
        """Load the configuration data from the config file if it is available, or use defaults
        """
        config_file_path = self._configuration_dir_path / SystemConfiguration.CONFIG_FILE_NAME

        config_data = {}
        try:
            with open(config_file_path, 'r') as f:
                config_data = json.load(f)
                f.close()

        except Exception as e:
            logging.warn(f"could not read config file \"{config_file_path}\" - error ]\"{e}\" - using default configuration")

        if SystemConfiguration.SERVER_ADDRESS_TAGNAME in config_data.keys():
            self._server_address = config_data[SystemConfiguration.SERVER_ADDRESS_TAGNAME]
        else:
            self._server_address = SystemConfiguration.DEFAULT_SERVER_ADDRESS

    def store(self):
        """Store the config data as a json config file
        """
        config_data = {
            SystemConfiguration.SERVER_ADDRESS_TAGNAME: self._server_address
        }

        self._configuration_dir_path.mkdir(parents=True, exist_ok=True)
        config_file_path = self._configuration_dir_path / SystemConfiguration.CONFIG_FILE_NAME
        with open(config_file_path, 'w+') as f:
            json.dump(config_data, f)
            f.close()

    def __init__(self, configuration_dir_path : Path):
        """Set up the system configuration object

        Args:
            configuration_dir_path (Path): The path to the folder to use for storing config data
        """
        self._configuration_dir_path = configuration_dir_path
        self.load()

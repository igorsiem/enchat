from urllib.parse import urlparse
from toga.validators import BooleanValidator

class SystemConfiguration:
    """A data structure for holding system config information
    """

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

    def __init__(self, server_address : str):
        self.server_address = server_address

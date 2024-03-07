from toga import Box, Label, TextInput, Widget, Button
from toga.validators import BooleanValidator
from toga.style.pack import COLUMN, ROW
from urllib.parse import urlparse

class SystemConfigurationBox(Box):
    """A box containing control for configuring the system

    Attributes:
        self._server_address_txi (TextInput): Text Input control for editing the server address
    """

    class ServerAddressValidator(BooleanValidator):
        """Validator for the server address

        This validator checks that the given scheme is http or https.

        TODO Tests for this validator
        """

        def is_valid(self, input_string : str) -> bool:            
            result = urlparse(input_string, scheme='http')

            if result.scheme not in ['http', 'https']:
                print(f"*** scheme: {result.scheme}")
                return False
            
            return True

    
    def __init__(self, server_address : str, on_ok : (Widget), on_cancel : (Widget)):
        server_address_lb = Label("Server address")
        self._server_address_txi = TextInput(value=server_address,
                                             validators=[SystemConfigurationBox.ServerAddressValidator(
                                                 error_message="must be a valid http(s) URL")])
        self._server_address_txi.style.width = 200

        server_address_bx = Box(children=[server_address_lb, self._server_address_txi])
        server_address_bx.style.direction = ROW

        # OK and cancel buttons
        ok_btn = Button(text="OK", on_press=on_ok)
        cancel_btn = Button(text="Cancel", on_press=on_cancel)
        button_bx = Box(children=[ok_btn, cancel_btn])
        button_bx.style.direction=(ROW)

        super(SystemConfigurationBox, self).__init__(children=[server_address_bx, button_bx])
        self.style.direction=COLUMN

    @property
    def server_address(self) -> str:
        """The address of the server, including optional port number

        Returns:
            str: The server address
        """
        return self._server_address_txi.value
    
    @server_address.setter
    def server_address(self, value : str):
        self._server_address_txi.value = value

from toga import Box, Label, TextInput, Widget, Button
from toga.style.pack import COLUMN, ROW
from enchat.system_configuration import SystemConfiguration
import logging

class SystemConfigurationBox(Box):
    """A box containing UI controls for configuring the system

    Attributes:
        self._server_address_txi (TextInput): Text Input control for editing the server address
        self._external_on_ok (Callable or None): An external function to call when the `OK` button is pressed
    """
    
    def __init__(self, system_configuration : SystemConfiguration, on_ok : (Widget), on_cancel : (Widget)):
        """Initialise the UI

        Args:
            system_configuration (SystemConfiguration): The System Configuration object to manage
            on_ok (Callable): External function to call when OK button is pressed
            on_cancel (Callable): External function to call when Cancel button is pressed
        """

        self._system_configuration = system_configuration
        self._external_on_ok = on_ok
        self._external_on_cancel = on_cancel

        server_address_lb = Label("Server address")
        self._server_address_txi = TextInput(validators=[SystemConfiguration.ServerAddressValidator(
                                                 error_message=SystemConfiguration.ServerAddressValidator.ERROR_MESSAGE)])
        self._server_address_txi.style.width = 200

        server_address_bx = Box(children=[server_address_lb, self._server_address_txi])
        server_address_bx.style.direction = ROW
        server_address_bx.style.alignment = "center"

        # OK and cancel buttons
        ok_btn = Button(text="OK", on_press=self.on_ok)
        cancel_btn = Button(text="Cancel", on_press=self.on_cancel)
        button_bx = Box(children=[ok_btn, cancel_btn])
        button_bx.style.direction=(ROW)

        super(SystemConfigurationBox, self).__init__(children=[server_address_bx, button_bx])
        self.style.direction=COLUMN

    def on_ok(self, widget : Widget):
        """Update the managed System Configuration object when OK is pressed, and write it to a file

        Note that the `self._external_on_ok` function (passed to the `__init__` method is called after the update).

        Args:
            widget (Widget): The widget that triggered the call
        """
        self.store_ui_to_config()
        self.system_configuration.store()

        if self._external_on_ok is not None:
            self._external_on_ok(widget)

    def on_cancel(self, widget : Widget):
        if self._external_on_cancel is not None:
            self._external_on_cancel(widget)

    def load_ui_from_config(self):
        """Load the system config from the config file AND the UI controls from the server config object
        """
        self.system_configuration.load()
        logging.debug(f"SystemConfigurationBox.load called - server address: {self.system_configuration.server_address}")
        self._server_address_txi.value = self.system_configuration.server_address

    def store_ui_to_config(self):
        """Store the information from the UI controls into the server config object
        """
        self.system_configuration.server_address = self._server_address_txi.value

    @property
    def system_configuration(self) -> SystemConfiguration:
        """The system configuration object being managed by this UI box
        """
        return self._system_configuration
    
    @system_configuration.setter
    def system_configuration(self, value : SystemConfiguration):
        self._system_configuration = value
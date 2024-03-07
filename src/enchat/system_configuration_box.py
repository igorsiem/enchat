from toga import Box, Label, TextInput, Widget, Button
from toga.style.pack import COLUMN, ROW

class SystemConfigurationBox(Box):

    def __init__(self, server_address : str, on_ok : (Widget), on_cancel : (Widget)):
        server_address_lb = Label("Server address")
        self._servier_address_ti = TextInput(value=server_address)

        server_address_bx = Box(children=[server_address_lb, self._servier_address_ti])
        server_address_bx.style.direction = ROW

        # OK and cancel buttons
        ok_btn = Button(text="OK", on_press=on_ok)
        cancel_btn = Button(text="Cancel", on_press=on_cancel)
        button_bx = Box(children=[ok_btn, cancel_btn])
        button_bx.style.direction=(ROW)

        super(SystemConfigurationBox, self).__init__(children=[server_address_bx, button_bx])
        self.style.direction=COLUMN

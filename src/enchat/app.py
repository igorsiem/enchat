import toga
from toga.style.pack import COLUMN, ROW, Pack
from enchat.message_box import MessageBox
from enchat.chat_configuration_box import ChatConfigurationBox

class EnChat(toga.App):
    """The main application class
    
    Attributes:
        _chat_bx (toga.Box): Box containing the chat messages
        _next_user_message_ti (toga.TextInput): The edit box for the next user message
        _next_user_message_bn (toga.Button): The button for sending the next user message
        _main_content_temp (toga.Box or None): Temporary storage for the main window content when it is not being used
        _configure_chat_cd (toga.Command): The command object for beginning configuration for the chat
        _configuration_bx (ChatConfigurationBox or None): Configuration box for chat parameters
    """

    def startup(self):
        """Build the GUI elements of the application, including the main window

        This method is called to start the application.
        """

        self.build_main_window()
        self.main_window.show()
    
    def build_main_window(self):
        """Build the main window of the application
        
        Creates the `self.main_window` attribute, and all its child objects.
        """

        self._configure_chat_cd = toga.Command(
            self.configure_chat,
            text="Configure Chat",
            tooltip="Set up the current chat",
            order=1
        )

        self.commands.add(self._configure_chat_cd)

        self.main_window = toga.MainWindow()
        self.main_window.toolbar.add(self._configure_chat_cd)
        self.main_window.content = self.create_main_box()

        self._configuration_bx = None
        self._main_content_temp = None

    def create_main_box(self) -> toga.Box:
        """Create the main content box for the application

        This method builds the `self._chat_bx`, `self._next_user_message_ti`, and `self._next_user_message_bn` attributes.

        Returns:
            toga.Box: The main content box object
        """

        # Create a Box for the chat message history, inside a scroll container
        self._chat_bx = toga.Box(style=Pack(direction=COLUMN))
        self._chat_bx.add(MessageBox("assistant", "Hello, there. What can I do for you today?"))

        chat_sc = toga.ScrollContainer(horizontal=False)
        chat_sc.style.flex = 1
        chat_sc.content = self._chat_bx

        # Create the main box with the scroll container and a box for the next user message
        return toga.Box(style=Pack(direction=COLUMN), children=[chat_sc, self.create_next_user_message_box()])
    
    def create_next_user_message_box(self) -> toga.Box:
        """Create the box for the user to enter the next new message

        This method builds the `_next_user_message_ti` and `_next_user_message_bn` attributes.

        Returns:
            toga.Box: The box containing the user controls for entering a new message
        """
        self._next_user_message_ti = toga.MultilineTextInput()
        self._next_user_message_ti.style.flex = 1
        self._next_user_message_bn = toga.Button(text=">", on_press=self.send_next_user_message)

        return toga.Box(style=Pack(direction=ROW), children=[self._next_user_message_ti, self._next_user_message_bn])

    def send_next_user_message(self, widget):
        """This method is invoked by the `self.send_next_user_message_cd` command object.

        TODO This is just a placeholder right now - it needs to be implemented

        Args:
            widget: The widget object that invoked the action.
        """
        self._chat_bx.add(MessageBox("user", self._next_user_message_ti.value))

    def configure_chat(self, widget):
        """Display the Chat Configuration window for displaying the chat parameters.

        Args:
            widget (toga.Widget): The widget that invoked the method
        """
        if self._configuration_bx is None:
            self._main_content_temp = self.main_window.content
            self._configuration_bx = ChatConfigurationBox(
                system_content="This is where the system content goes", on_ok=self.on_configure_ok, on_cancel=self.on_configure_cancel)
            self.main_window.content = self._configuration_bx
            self._configure_chat_cd.enabled = False

    def on_configure_ok(self, widget):
        """Update the configuration for the chat and hide the Chat Configuration window.

        This methos is called when the User presses the OK button to confirm the data in the Chat Configuration window

        Args:
            widget (Widget): The widget that invoked this method
        """
        if self._main_content_temp is not None:
            self.main_window.content = self._main_content_temp
            self._main_content_temp = None
            self._configuration_bx = None
            self._configure_chat_cd.enabled = True
            print("*** OK pressed")

    def on_configure_cancel(self, widget):
        """Close the Chat Configuration window without updating any chat parameters.

        Args:
            widget (Widget): The widget that invoked this method
        """
        if self._main_content_temp is not None:
            self.main_window.content = self._main_content_temp
            self._main_content_temp = None
            self._configuration_bx = None
            self._configure_chat_cd.enabled = True
            print("*** Cancel pressed")
    
def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EnChat("enChat", "com.technopraxia.enchat", description="Interaction with OpenAI LLMs")

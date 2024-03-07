import toga
from toga.style.pack import COLUMN, ROW, Pack
from enchat.message_box import MessageBox
from enchat.chat_configuration_box import ChatConfigurationBox
from enchat.system_configuration_box import SystemConfigurationBox

class EnChat(toga.App):
    """The main application class

    This class manages all UI elements at the top level. The GUI has the following main elements:

    * The main chat screen content
    * The Chat Configuration UI for manipipulating the parameters of the chat
    * The System Configuration UI for manipulating the system parameters

    These UIs are all instantiated 'up front', and the self.main_window.content attribute is switched between them.
    
    Attributes:
        self._configure_chat_cmd (toga.Command): User command for configurating the current chat
        self._configure_system_cmd (toga.Command): User command for configuring the chat system
        self._main_content_box (toga.Box): The box containing the main chat content
        self._chat_configuration_box (toga.Box): The box containing the chat configuration UI
        self._system_configuration_box (toga.Box): The box containing the system configuration UI
        self._next_user_message_mti (toga.MulilineTextInput) Text input control for the next user message
        self._next_user_message_btn (toga.Button) Button for sending the next user message
    """

    def startup(self):
        """Build the GUI elements of the application, including the main window

        This method is called to start the application.
        """

        self.build_main_window()
        self.main_window.show()
    
    def build_main_window(self):
        """Build the main window of the application

        This method initialises the following attributes:        
        * self._configure_chat_cmd
        * self._configure_system_cmd
        * self._main_content_box
        * self._chat_configuration_box
        * self._system_configuration_box
        """

        self._configure_chat_cmd = toga.Command(
            self.configure_chat,
            text="Configure chat",
            tooltip="Set up the current chat",
            order=1
        )

        self._configure_system_cmd = toga.Command(
            self.configure_system,
            text="Configure system",
            tooltip="System configuration options",
            order=2
        )

        self.build_main_content_box()
        self._chat_configuration_box = ChatConfigurationBox(
                system_content="This is where the system content goes",
                on_ok=self.on_chat_configuration_ok,
                on_cancel=self.on_chat_configuration_cancel)
        self._system_configuration_box = SystemConfigurationBox("", on_ok=self.on_system_configuration_ok, 
                                                               on_cancel=self.on_system_configuration_cancel)

        # Set up the main window, initially containing the main content box        
        self.main_window = toga.MainWindow()
        self.main_window.toolbar.add(self._configure_chat_cmd)
        self.main_window.toolbar.add(self._configure_system_cmd)
        self.main_window.content = self._main_content_box


    def build_main_content_box(self) -> toga.Box:
        """Build the main content box for the application

        This method initialises the self._main_content_box and self.chat_box attributes.
        """

        # Create a Box for the chat message history, inside a scroll container
        self._chat_box = toga.Box(style=Pack(direction=COLUMN))
        self._chat_box.add(MessageBox("assistant", "Hello, there. What can I do for you today?"))

        chat_scr = toga.ScrollContainer(horizontal=False)
        chat_scr.style.flex = 1
        chat_scr.content = self._chat_box

        # Create the main box with the scroll container and a box for the next user message
        self._main_content_box = toga.Box(style=Pack(direction=COLUMN), children=[chat_scr, self.create_next_user_message_box()])
    
    def create_next_user_message_box(self) -> toga.Box:
        """Create the box for the user to enter the next new message

        This method builds the `_next_user_message_mti` and `_next_user_message_btn` attributes, and returns the box containing them, which
        is inserted into a parent without being retained as an object attribute.

        Returns:
            toga.Box: The box containing the user controls for entering a new message
        """
        self._next_user_message_mti = toga.MultilineTextInput()
        self._next_user_message_mti.style.flex = 1
        self._next_user_message_btn = toga.Button(text=">", on_press=self.send_next_user_message)

        return toga.Box(style=Pack(direction=ROW), children=[self._next_user_message_mti, self._next_user_message_btn])

    def send_next_user_message(self, widget):
        """Send the next user message

        TODO This is just a placeholder right now - it needs to be implemented

        Args:
            widget: The widget object that invoked the action.
        """
        self._chat_box.add(MessageBox("user", self._next_user_message_mti.value))
        print("TODO Implement send next user message")

    def configure_chat(self, widget):
        """Display the Chat Configuration window for displaying the chat parameters.

        TODO Implement chat configuration initialisation

        Args:
            widget (toga.Widget): The widget that invoked the method
        """
        self.switch_to_chat_configuration()
        print("TODO Implement chat configuration initialisation")

    def on_chat_configuration_ok(self, widget):
        """Update the configuration for the chat and hide the Chat Configuration window.

        This method is called when the User presses the OK button to confirm the data in the Chat Configuration window.

        TODO Implement chat configuration confirmation

        Args:
            widget (Widget): The widget that invoked this method
        """
        self.switch_to_main_content()
        print("TODO Implement chat configuration")

    def on_chat_configuration_cancel(self, widget):
        """Close the Chat Configuration window without updating any chat parameters.

        TODO implement chat config cancellation

        Args:
            widget (Widget): The widget that invoked this method
        """
        self.switch_to_main_content()        
        print("TODO implement chat config cancel")

    def configure_system(self, widget):
        self.switch_to_system_configuration()
        print("TODO implement system config initialisation")

    def on_system_configuration_ok(self, widget):
        self.switch_to_main_content()
        print("TODO implement system config confirmation")

    def on_system_configuration_cancel(self, widget):
        self.switch_to_main_content()
        print("TODO implement system config cancellation")

    def switch_to_main_content(self):
        self.main_window.content = self._main_content_box
        self._configure_chat_cmd.enabled = True
        self._configure_system_cmd.enabled = True

    def switch_to_chat_configuration(self):
        self.main_window.content = self._chat_configuration_box
        self._configure_chat_cmd.enabled = False
        self._configure_system_cmd.enabled = False

    def switch_to_system_configuration(self):
        self.main_window.content = self._system_configuration_box
        self._configure_chat_cmd.enabled = True
        self._configure_system_cmd.enabled = False

def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EnChat("enChat", "com.technopraxia.enchat", description="Interaction with OpenAI LLMs")

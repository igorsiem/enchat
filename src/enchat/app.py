import toga
from toga.style.pack import COLUMN, ROW, Pack
from enchat.message_box import MessageBox

class EnChat(toga.App):
    """The main application class
    
    Attributes:
        main_window (toga.MainWindow): The main window of the application
        chat_bx (toga.Box): Box containing the chat messages
        next_user_message_ti (toga.TextInput): The edit box for the next user message
        self.next_user_message_bn (toga.Button): The button for sending the next user message
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
        self.main_window = toga.MainWindow()
        self.main_window.content = self.create_main_box()

    def create_main_box(self) -> toga.Box:
        """Create the main content box for the application

        This method builds the `self.chat_bx`, `self.next_user_message_ti`, and `self.next_user_message_bn` attributes.

        Returns:
            toga.Box: The main content box object
        """

        # Create a Box for the chat messages.
        self.chat_bx = toga.Box(style=Pack(direction=COLUMN))
        self.chat_bx.add(MessageBox("assistant", "Hello, there. What can I do for you today?"))

        # Create a scroll container for the chat messages box.
        chat_sc = toga.ScrollContainer(horizontal=False)
        chat_sc.style.flex = 1
        chat_sc.content = self.chat_bx

        # Text input for the user
        self.next_user_message_ti = toga.MultilineTextInput()
        self.next_user_message_ti.style.flex = 1
        self.next_user_message_bn = toga.Button(text=">", on_press=self.send_next_user_message)

        next_user_message_box = toga.Box(style=Pack(direction=ROW), children=[self.next_user_message_ti, self.next_user_message_bn])

        main_box = toga.Box(style=Pack(direction=COLUMN), children=[chat_sc, next_user_message_box])

        return main_box
    
    def send_next_user_message(self, widget):
        """This method is invoked by the `self.send_next_user_message_cd` command object.

        TODO This is just a placeholder right now - it needs to be implemented

        Args:
            widget: The widget object that invoked the action.
        """
        self.chat_bx.add(MessageBox("user", self.next_user_message_ti.value))
    
def main():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EnChat("enChat", "com.technopraxia.enchat", description="Interaction with OpenAI LLMs")

import toga
from toga import Box, Label
from toga.style.pack import ROW, Pack

class MessageBox(Box):
    """A box containing all the info for a single message from either the User or the Assistant

    The MessageBox displays the role of the message. This is usually one of the following:

    * "System" - A initial message describing the role of the system / assistant in the conversation
    * "Assistant" - The message comes from the AI agent
    * "User" - The message comes from the human user

    Note:
        This class should not be confused with the "Message Box" for alerting users with a simple message that is an artefact of many GUIs.

    Attributes:
        _role_lb: Label for the 'role' string
        _message_lb: Label for the message text
    """

    COLOURS = {
        'user': {
            'role': {
                'foreground': '#99f',
                'background': '#111'
            },
            'message': {
                'foreground': '#aaa',
                'background': '#111'
            }
        },
        "assistant": {
            'role': {
                'foreground': '#f99',
                'background': '#333'
            },
            'message': {
                'foreground': '#ddd',
                'background': '#333'
            }
        }
    }

    def __init__(self, role : str, message : str):
        """Set up the MessageBox object

        Args:
            role (str): The sender role for the message
            message (str): The entire text of the message
        """

        rl = 'user'

        if role == "assistant":
            rl = 'assistant'

        self._role_lb = Label(
            text=role,
            style=Pack(
                color=MessageBox.COLOURS[rl]['role']['foreground'],
                background_color=MessageBox.COLOURS[rl]['role']['background']
            ))
        self._message_lb = Label(
            text=message,
            style=Pack(
                flex=1,
                color=MessageBox.COLOURS[rl]['message']['foreground'],
                background_color=MessageBox.COLOURS[rl]['message']['background']))

        super(MessageBox, self).__init__(style=Pack(direction=ROW), children=[self._role_lb, self._message_lb])

    @property
    def role(self) -> str:
        """The role of the sender of the message (usually either "system", "user" or "assistant", but could be anything)

        Returns:
            str: The role as a human-readable string
        """
        return self._role_lb.text
    
    @role.setter
    def role(self, value : str):
        self._role_lb.text = value

    @property
    def message(self) -> str:
        """The message text

        Returns:
            str: The text of the message
        """
        return self._message_lb.text
    
    @message.setter
    def message(self, value : str):
        self._message_lb.text = value

from toga import Box, Label, MultilineTextInput, TextInput, Widget, Button
from toga.style.pack import COLUMN, ROW
from toga.validators import Number
from enchat.validators import FloatRange, IntegerRange

class ChatConfigurationBox(Box):
    """A box containing controls for configuring the current chat

    These parameters are sent to the server.

    Attributes:
        _system_content_mti (MultiLineTextInput): Input for the system content at the beginning of the chat
        _temp_txi (TextInput): Input for the temperature attribute
        _n_predict_txi (TextInput): Input for the `n_predict` parameter
        _top_k_txi (TextInput): Input for the `top_k` parameter
        _repeat_penalty_txi (TextInput): Input for the repeat penality model parameter
        _min_p_txi (TextInput): Input for the min_p parameter for the model
        _top_p_txi (TextInput): Inpyt for the top_p parameter for the model
        LABEL_WIDTH (int): Consistent width for all labels in a column of parameters
    """

    LABEL_WIDTH = 100

    def __init__(self, system_content : str, on_ok : (Widget), on_cancel : (Widget), temp : float = 0.8, n_predict : int = -1,
                 top_k : int = 40, repeat_penalty : float = 1.1, min_p : float = 0.95, top_p : float = 0.95):        
        
        # System content
        system_content_lbl = Label("System content")

        self._system_content_mti = MultilineTextInput(value=system_content)
        self._system_content_mti.style.flex=1

        system_content_bx = Box(children=[system_content_lbl, self._system_content_mti])
        system_content_bx.style.direction=COLUMN

        # Temp
        temp_lbl = Label("Temperature")
        temp_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._temp_txi = TextInput(
            value=temp, 
            validators=[Number(error_message="must be a number", allow_empty=False),
                        FloatRange("must be in the range [0,1]", allow_empty=False, min=0.0, max=1.0)])
        temp_box = Box(children=[temp_lbl, self._temp_txi])
        temp_box.style.direction=ROW

        # n_predict
        n_predict_lbl = Label("n_predict")
        n_predict_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._n_predict_txi = TextInput(
            value=n_predict,
            validators=[Number(error_message="must be a number", allow_empty=False),
                        IntegerRange(error_message="must be an integer greater than -1", allow_empty=False, min=-1)])
        n_predict_box = Box(children=[n_predict_lbl, self._n_predict_txi])
        n_predict_box.style.direction=ROW

        # top_k
        top_k_lbl = Label("top_k")
        top_k_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._top_k_txi = TextInput(
            value=top_k,
            validators=[Number(error_message="must be a number", allow_empty=False),
                        IntegerRange(error_message="must be an integer greater than 0", allow_empty=False, min=0)])
        top_k_box = Box(children=[top_k_lbl, self._top_k_txi])
        top_k_box.style.direction=ROW

        # Repeat penalty
        repeat_penalty_lbl = Label("Repeat penalty")
        repeat_penalty_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._repeat_penalty_txi = TextInput(
            value = repeat_penalty,
            validators=[Number(error_message="must be a number", allow_empty=False),
                        FloatRange(error_message="must be greater than or equal to 0", allow_empty=False, min=0.0)])
        
        repeat_penalty_box = Box(children=[repeat_penalty_lbl, self._repeat_penalty_txi])
        repeat_penalty_box.style.direction = ROW

        # min_p
        min_p_lbl = Label("min_p")
        min_p_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._min_p_txi = TextInput(
            value = min_p,
            validators=[Number(error_message="must be a number", allow_empty=False),
                        FloatRange(error_message="must be in the range [0,1]", allow_empty=False, min=0, max=1)])
        
        min_p_bx = Box(children=[min_p_lbl, self._min_p_txi])
        min_p_bx.style.direction=ROW

        # top_p
        top_p_lbl = Label("top_p")
        top_p_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH

        self._top_p_txi = TextInput(
            value = top_p,
            validators=[Number(error_message="must be a number", allow_empty=False),
                        FloatRange(error_message="must be in the range [0,1]", allow_empty=False, min=0, max=1)])
        
        top_p_box = Box(children=[top_p_lbl, self._top_p_txi])
        top_p_box.style.direction = ROW

        # OK and cancel buttons
        ok_btn = Button(text="OK", on_press=on_ok)
        cancel_btn = Button(text="Cancel", on_press=on_cancel)
        button_box = Box(children=[ok_btn, cancel_btn])
        button_box.style.direction=(ROW)

        super(ChatConfigurationBox, self).__init__(
            children=[system_content_bx, temp_box, n_predict_box, top_k_box, repeat_penalty_box, min_p_bx, top_p_box, button_box])
        self.style.direction=COLUMN

    @property
    def system_content(self) -> str:
        """The system content for starting the chat

        Returns:
            str: The string used for the system content at the beginning of the chat
        """
        return self._system_content_mti.value
    
    @system_content.setter
    def system_content(self, value : str):
        self._system_content_mti.value = value

    @property
    def temp(self) -> float:
        """The temperature (randomness) parameter, default=0.8

        Note that temporary value is trimmed.

        Returns:
            float: The temperature, range [0,1]
        """
        return float(self._temp_txi.value)
    
    @temp.setter
    def temp(self, value : float):
        self._temp_txi.value = str(value)

    @property
    def n_predict(self) -> int:
        """ The number of tokens to generate; set to -1 (default) to let the model stop on its own

        Returns:
            int [-1,]: The `n_predict` parameter for the model
        """
        return int(float(self._n_predict_txi.value))

    @n_predict.setter
    def n_predict(self, value : int):
        self._n_predict_txi.value = value

    @property
    def top_k(self) -> int:
        """ Top-k sampling parameter; higher values generate more diverse text, default=40

        Returns:
            int [0,]: The top_k value for the model
        """
        return int(float(self._top_k_txi.value))
    
    @top_k.setter
    def top_k(self, value : int):
        self._top_k_txi.value = value

    @property
    def repeat_penalty(self) -> float:
        """Penalty for repetition; higher value means less probability of repeats, default=1.1

        Returns:
            float [0,]: The repeat penalty parameter for the model
        """
        return float(self._repeat_penalty_txi.value)
    
    @repeat_penalty.setter
    def repeat_penalty(self, value : float):
        self._repeat_penalty_txi.value = value
    
    @property
    def min_p(self) -> float:
        """Minimum probability for token to be considered; default=0.05

        Returns:
            float [0,1]: The min_p parameter for the model
        """
        return float(self._min_p_txi.value)
    
    @min_p.setter
    def min_p(self, value : float):
        self._min_p_txi.value = value
    
    @property
    def top_p(self) -> float:
        """Top-p sampling parameter; balancing number and diversity of tokens; default=0.95

        Returns:
            float [0,1]: The top_p parameter for the model
        """
        return float(self._top_p_txi.value)
    
    @top_p.setter
    def top_p(self, value : float):
        self._top_p_txi.value = value

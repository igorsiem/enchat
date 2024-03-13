from toga.validators import Number
from enchat.validators import FloatRange, IntegerRange, validate_all_using

class ChatConfiguration:
    """Configuration items for a chat

    There can be multiple chat configurations for a system, and a single configuration may be used for multiple chats.

    Attributes:
        SYSTEM_CONTENT_DEFAULT (str): The default string for the system content
        TEMP_MIN (float): The minimum value for the temp parameter
        TEMP_MAX (float): The maximum value for the temp parameters
    """

    SYSTEM_CONTENT_DEFAULT = "You are an AI assistant."

    TEMP_MIN = 0.0
    TEMP_MAX = 1.0
    TEMP_DEFAULT = 0.8
    TEMP_VALIDATORS = [Number("must be a number", allow_empty=False),
                       FloatRange("must be in the range [0,1]", allow_empty=False, min=TEMP_MIN, max=TEMP_MAX)]

    N_PREDICT_MIN = -1
    N_PREDICT_DEFAULT = -1
    N_PREDICT_VALIDATORS = [Number(error_message="must be a number", allow_empty=False),
                            IntegerRange(error_message="must be an integer greater than -1", allow_empty=False, min=N_PREDICT_MIN)]

    TOP_K_MIN = 0
    TOP_K_DEFAULT = 40
    TOP_K_VALIDATORS = [Number(error_message="must be a number", allow_empty=False),
                        IntegerRange(error_message="must be an integer greater than 0", allow_empty=False, min=TOP_K_MIN)]

    REPEAT_PENALTY_MIN = 0.0
    REPEAT_PENALTY_DEFAULT = 1.1
    REPEAT_PENALTY_VALIDATORS = [Number(error_message="must be a number", allow_empty=False),
                                 FloatRange(error_message="must be greater than or equal to 0", allow_empty=False, min=REPEAT_PENALTY_MIN)]

    MIN_P_MIN = 0.0
    MIN_P_MAX = 1.0
    MIN_P_DEFAULT = 0.05
    MIN_P_VALIDATORS = [Number(error_message="must be a number", allow_empty=False),
                        FloatRange(error_message="must be in the range [0,1]", allow_empty=False, min=MIN_P_MIN, max=MIN_P_MAX)]

    TOP_P_MIN = 0.0
    TOP_P_MAX = 1.0
    TOP_P_DEFAULT = 0.95
    TOP_P_VALIDATORS = [Number(error_message="must be a number", allow_empty=False),
                        FloatRange(error_message="must be in the range [0,1]", allow_empty=False, min=TOP_P_MIN, max=TOP_P_MAX)]

    def __init__(self, system_content : str = SYSTEM_CONTENT_DEFAULT, temp : float = TEMP_DEFAULT, n_predict : int = N_PREDICT_DEFAULT,
                 top_k : int = TOP_K_DEFAULT, repeat_penalty : float = REPEAT_PENALTY_DEFAULT, min_p : float = MIN_P_DEFAULT,
                 top_p : float = TOP_P_DEFAULT):

        self.system_content = system_content
        self.temp = temp
        self.n_predict = n_predict
        self.top_k = top_k
        self.repeat_penalty = repeat_penalty
        self.min_p = min_p
        self.top_p = top_p

    @property
    def system_content(self) -> str:
        """The system content entry for setting the context of a chat

        Returns:
            str: The system content string
        """
        return self._system_content
    
    @system_content.setter
    def system_content(self, value : str):
        self._system_content = value

    @property
    def temp(self) -> float:
        """The temperature (randomness) parameter (default=0.8)

        Returns:
            float: The temperature parameter, rante [0.0,1.0]
        """
        return self._temp
    
    @temp.setter
    def temp(self, value : float):
        if validate_all_using(value, ChatConfiguration.TEMP_VALIDATORS) is False:
            raise RuntimeError(f"temp value '{value}' failed validation")
        
        self._temp = value

    @property
    def n_predict(self) -> int:
        """ The number of tokens to generate; set to -1 (default) to let the model stop on its own

        Returns:
            int [-1,]: The `n_predict` parameter for the model
        """
        return self._n_predict
    
    @n_predict.setter
    def n_predict(self, value : int):
        if validate_all_using(value, ChatConfiguration.N_PREDICT_VALIDATORS) is False:
            raise RuntimeError(f"n_predict value '{value}' failed validation")
        
        self._n_predict = value

    @property
    def top_k(self) -> int:
        """ Top-k sampling parameter; higher values generate more diverse text, default=40

        Returns:
            int [0,]: The top_k value for the model
        """
        return self._top_k
    
    @top_k.setter
    def top_k(self, value : int):
        if validate_all_using(value, ChatConfiguration.TOP_K_VALIDATORS) is False:
            raise RuntimeError(f"top_k value '{value} failed validation")
        
        self._top_k = value
    
    @property
    def repeat_penalty(self) -> float:
        """Penalty for repetition; higher value means less probability of repeats, default=1.1

        Returns:
            float [0,]: The repeat penalty parameter for the model
        """
        return self._repeat_penalty
    
    @repeat_penalty.setter
    def repeat_penalty(self, value : float):
        if validate_all_using(value, ChatConfiguration.REPEAT_PENALTY_VALIDATORS) is False:
            raise RuntimeError(f"repeat_penalty value '{value}' failed validation")
        
        self._repeat_penalty = value

    @property
    def min_p(self) -> float:
        """Minimum probability for token to be considered; default=0.05

        Returns:
            float [0,1]: The min_p parameter for the model
        """
        return self._min_p
    
    @min_p.setter
    def min_p(self, value : float):
        if validate_all_using(value, ChatConfiguration.MIN_P_VALIDATORS) is False:
            raise RuntimeError(f"min_p value '{value}' failed validation")
        
        self._min_p = value

    @property
    def top_p(self) -> float:
        """Top-p sampling parameter; balancing number and diversity of tokens; default=0.95

        Returns:
            float [0,1]: The top_p parameter for the model
        """
        return self._top_p
    
    @top_p.setter
    def top_p(self, value : float):
        if validate_all_using(value, ChatConfiguration.TOP_P_VALIDATORS) is False:
            raise RuntimeError(f"top_p value '{value} failed validation")
        
        self._top_p = value

    
class ChatConfiguration:
    """Configuration items for a chat

    There can be multiple chat configurations for a system, and a single configuration may be used for multiple chats.
    """
    
    def __init__(self, system_content : str = "You are an AI assistant.", temp : float = 0.8, n_predict : int = -1, top_k : int = 40,
                 repeat_penalty : float = 1.1, min_p : float = 0.95, top_p : float = 0.95):
        self.system_content = system_content
        self.temp = temp
        self.n_predict = n_predict
        self.top_k = top_k
        self.repeat_penalty = repeat_penalty
        self.min_p = min_p
        self.top_p = top_p

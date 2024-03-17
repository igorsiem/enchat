import toga
from toga import Box, Label, MultilineTextInput, TextInput, Widget, Button, Selection
from toga.style.pack import COLUMN, ROW
from toga.validators import Number
from enchat.chat_configuration import ChatConfiguration
from pathlib import Path

class ChatConfigurationBox(Box):
    """A box containing controls for configuring the current chat

    These parameters are sent to the server.

    Attributes:
        _load_filename_sel
        _save_filename_txi
        _save_btn
        _system_content_mti (MultiLineTextInput): Input for the system content at the beginning of the chat
        _temp_txi (TextInput): Input for the temperature attribute
        _n_predict_txi (TextInput): Input for the `n_predict` parameter
        _top_k_txi (TextInput): Input for the `top_k` parameter
        _repeat_penalty_txi (TextInput): Input for the repeat penality model parameter
        _min_p_txi (TextInput): Input for the min_p parameter for the model
        _top_p_txi (TextInput): Input for the top_p parameter for the model
        LABEL_WIDTH (int): Consistent width for all labels in a column of parameters
    """

    LABEL_WIDTH = 100

    def load_ui_from_config(self):
        self._system_content_mti.value = self.chat_configuration.system_content
        self._temp_txi.value = self.chat_configuration.temp
        self._n_predict_txi.value = self.chat_configuration.n_predict
        self._top_k_txi.value = self.chat_configuration.top_k
        self._repeat_penalty_txi.value = self.chat_configuration.repeat_penalty
        self._min_p_txi.value = self.chat_configuration.min_p
        self._top_p_txi.value = self.chat_configuration.top_p

    def store_ui_to_to_config(self):
        self.chat_configuration.system_content = self._system_content_mti.value
        self.chat_configuration.temp = self._temp_txi.value
        self.chat_configuration.n_predict = self._n_predict_txi.value
        self.chat_configuration.top_k = self._top_k_txi.value
        self.chat_configuration.repeat_penalty = self._repeat_penalty_txi.value
        self.chat_configuration.min_p = self._min_p_txi.value
        self.chat_configuration.top_p = self._top_p_txi.value

    def __init__(self, chat_configuration : ChatConfiguration, on_ok : (Widget), on_cancel : (Widget), data_dir_path : Path):

        self.chat_configuration = chat_configuration

        self._external_on_ok = on_ok
        self._external_on_cancel = on_cancel
        self._data_dir_path = data_dir_path

        # Top control bar
        new_btn = Button("New", on_press=self.on_new_btn_pressed)

        self._load_filename_sel = Selection()
        load_btn = Button("Load")
        load_box = Box(children=[self._load_filename_sel, load_btn])
        load_box.style.direction=COLUMN

        self._save_filename_txi = TextInput(on_change=self.on_save_filename_changed)
        self._save_btn = Button("Save", on_press=self.on_save_btn_pressed)
        save_box = Box(children=[self._save_filename_txi, self._save_btn])
        save_box.style.direction=COLUMN
        self.on_save_filename_changed(None)

        control_bar_box = Box(children=[new_btn,
                                       load_box,
                                       save_box])
        control_bar_box.style.direction = ROW
        
        # System content
        system_content_lbl = Label("System content")

        self._system_content_mti = MultilineTextInput()
        self._system_content_mti.style.flex=1

        system_content_bx = Box(children=[system_content_lbl, self._system_content_mti])
        system_content_bx.style.direction=COLUMN

        # Temp
        temp_lbl = Label("Temperature")
        temp_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._temp_txi = TextInput(validators=ChatConfiguration.TEMP_VALIDATORS)
        temp_box = Box(children=[temp_lbl, self._temp_txi])
        temp_box.style.direction=ROW
        temp_box.style.alignment="center"

        # n_predict
        n_predict_lbl = Label("n_predict")
        n_predict_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._n_predict_txi = TextInput(validators=ChatConfiguration.N_PREDICT_VALIDATORS)
        n_predict_box = Box(children=[n_predict_lbl, self._n_predict_txi])
        n_predict_box.style.direction=ROW
        n_predict_box.style.alignment="center"

        # top_k
        top_k_lbl = Label("top_k")
        top_k_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._top_k_txi = TextInput(validators=ChatConfiguration.TOP_K_VALIDATORS)
        top_k_box = Box(children=[top_k_lbl, self._top_k_txi])
        top_k_box.style.direction=ROW
        top_k_box.style.alignment="center"

        # Repeat penalty
        repeat_penalty_lbl = Label("Repeat penalty")
        repeat_penalty_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._repeat_penalty_txi = TextInput(validators=ChatConfiguration.REPEAT_PENALTY_VALIDATORS)        
        repeat_penalty_box = Box(children=[repeat_penalty_lbl, self._repeat_penalty_txi])
        repeat_penalty_box.style.direction = ROW
        repeat_penalty_box.style.alignment="center"

        # min_p
        min_p_lbl = Label("min_p")
        min_p_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._min_p_txi = TextInput(validators=ChatConfiguration.MIN_P_VALIDATORS)        
        min_p_bx = Box(children=[min_p_lbl, self._min_p_txi])
        min_p_bx.style.direction=ROW
        min_p_bx.style.alignment="center"

        # top_p
        top_p_lbl = Label("top_p")
        top_p_lbl.style.width = ChatConfigurationBox.LABEL_WIDTH
        self._top_p_txi = TextInput(validators=ChatConfiguration.TOP_P_VALIDATORS)        
        top_p_box = Box(children=[top_p_lbl, self._top_p_txi])
        top_p_box.style.direction = ROW
        top_p_box.style.alignment="center"

        # OK and cancel buttons
        ok_btn = Button(text="OK", on_press=on_ok)
        cancel_btn = Button(text="Cancel", on_press=on_cancel)
        button_box = Box(children=[ok_btn, cancel_btn])
        button_box.style.direction=(ROW)

        super(ChatConfigurationBox, self).__init__(
            children=[control_bar_box,
                      system_content_bx,
                      temp_box,
                      n_predict_box,
                      top_k_box,
                      repeat_penalty_box,
                      min_p_bx,
                      top_p_box,
                      button_box])
        self.style.direction=COLUMN

        self.load_ui_from_config()

    def on_new_btn_pressed(self, widget):
        self.chat_configuration = ChatConfiguration()
        self.load_ui_from_config()

    def on_save_filename_changed(self, widget):
        if self._save_filename_txi.value == "":
            self._save_btn.enabled = False
        else:
            self._save_btn.enabled = True
            
    def on_save_btn_pressed(self, widget):
        if self._save_filename_txi.value == "":
            raise RuntimeError("filename not specified")
        
        file_path = (self._data_dir_path / self._save_filename_txi.value).with_suffix(ChatConfiguration.FILE_EXTENSION)        
        
        self.chat_configuration.write_to_file(file_path)

        self._load_filename_sel.items.append(self._save_filename_txi.value)
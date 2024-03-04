import toga

class EnChat(toga.App):
    """The main application class
    
    Attributes:
        main_window (toga.MainWindow): The main window of the application
    """

    def startup(self) -> None:
        """Build the GUI elements of the application, in including the main winddow

        This method is called to start the application.
        """

        self.main_window = toga.MainWindow()
        self.main_window.show()

        return super().startup()
    
def main():
    return EnChat("enChat", "com.technopraxia.enchat", description="Interaction with OpenAI LLMs")

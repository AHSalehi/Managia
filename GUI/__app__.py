'''
This file contains GUI codes
'''
import customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Managia")
        self.geometry("800x600")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        

app = App()
app.mainloop()
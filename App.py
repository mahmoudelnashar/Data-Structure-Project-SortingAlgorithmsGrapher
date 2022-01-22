import tkinter as tk
from mainFrame import MFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x782")
        self.configure(bg="#a6cff5")
        self.title("Sorting Algo")
        self.mainFrame = MFrame(self)
        self.mainFrame.pack(fill=tk.BOTH, expand=1)
        self.resizable(False, False)
        self.mainloop()

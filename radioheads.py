import tkinter as tk

COLORS = [("Red", "red"), ("Green", "green"), ("Yellow", "yellow")]


class App(tk.Tk):
    """This is a simple app that creates radiohead options"""
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("red")

        self.buttons = [self.create_radiohead(c) for c in COLORS]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)

    def create_radiohead(self, c):
        text, value = c
        return tk.Radiobutton(self, text=text, value=value,
                              command=self.print_option, variable=self.var)
    
    def print_option(self):
        print(self.var.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    


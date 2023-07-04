import tkinter as tk

class App(tk.Tk):
    """A simple app that tracing text changes"""
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.show_message)
        self.Entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(self, text="Clear",
                             command=lambda: self.var.set(""))
        self.label = tk.Label(self)
        self.Entry.pack()
        self.btn.pack()
        self.label.pack()

    def show_message(self, *args):
        value = self.var.get()
        text = f"Hello, {value}" if value else ""
        self.label.config(text=text)


if __name__ == "__main__":
    app = App()
    app.mainloop()

        
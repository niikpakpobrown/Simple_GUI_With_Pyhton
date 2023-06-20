import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="click me!",
                             command=self.say_hello)
        self.btn.pack(padx=130, pady=30)

    def say_hello(self):
        print("hello")

if __name__ == "__main__":
    app = App()
    app.title("MY APP")
    app.mainloop()
# #!/usr/bin/python

# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()


# from tkinter import Tk, Label, Button
from tkinter import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

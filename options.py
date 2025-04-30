import tkinter
from tkinter import ttk

useGUI = False

root = tkinter.Tk();
root.title("Window Named Finger") # Name the Window
root.geometry("400x300") # window size as width * height


def runGUI():

    frm = ttk.Frame(root, padding=10) # Set the Frame & Grid for buttons
    frm.grid()

    ttk.Label(frm, text="Hello USER!").grid(column=0, row=0)
    ttk.Label(frm, text="Would you like the demo to have its GUI or not?").grid(column=0, row=1) # Prompt the User before continuing

    ttk.Button(frm, text="WHY YES!!!!!!", command=trueGUI).grid(column=0, row=2)
    ttk.Button(frm, text="aww HELL naw man wtf man", command=falseGUI).grid(column=1, row=2) # Answer the Prompt

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    root.mainloop() # Quit if No Decision

    return useGUI

def trueGUI():
    global useGUI 
    useGUI = True
    root.destroy()

def falseGUI():
    global useGUI
    useGUI = False
    root.destroy()

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
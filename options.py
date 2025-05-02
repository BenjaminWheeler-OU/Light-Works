import tkinter
from tkinter import ttk
import yaml

options = {
    'generations': 2,
    'population-size': 10,
    'survival-rate': 0.1,
    'mutate-factor': 0.2
}

root = tkinter.Tk()
root.title("GUI Options") # Name the Window
root.geometry("500x350") # window size as width * height

def get(i):
    global options
    return options[i]

def load():
    global options

    try:
        with open('options.yml', 'r') as file:
            options.update(yaml.safe_load(file))
    except FileNotFoundError:
        pass
    except yaml.scanner.ScannerError:
        print('The options file is formatted incorrectly. Regenerating...')

    if 'GUI' not in options:
        runGUI()

    with open('options.yml', 'w') as file:
        yaml.dump(options, file)
    print(options)


def runGUI():

    frm = ttk.Frame(root, padding=10) # Set the Frame & Grid for buttons
    frm.grid()

    ttk.Label(frm, text="Hello User!").grid(column=0, row=0)
    ttk.Label(frm, text="Would you like the demo to use a GUI?").grid(column=0, row=1) # Prompt the User before continuing

    ttk.Button(frm, text="Yes!", command=trueGUI).grid(column=0, row=2)
    ttk.Button(frm, text="No!", command=falseGUI).grid(column=1, row=2) # Answer the Prompt

    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
    root.mainloop() # Quit if No Decision

def trueGUI():
    global options
    options['GUI'] = True
    root.destroy()

def falseGUI():
    global options
    options['GUI'] = False
    root.destroy()

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
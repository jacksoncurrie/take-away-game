#=========================== LIBRARYS =================================

from tkinter import *

from ConsoleGame import Run
from GUIGame import GetInputs

#======================== MAIN GAME FUNTIONS ==========================

def Visual():
    root.destroy()
    GetInputs()
    OpenGUI()

def Console():
    root.destroy()
    try:
        Run()
    except KeyboardInterrupt:
        OpenGUI()

#======================= INITIALIZING WINDOW ==========================

def OpenGUI():
    
    global root
    root = Tk()
    root.geometry("600x300+350+100")
    root.title("Take-Away Game")

#========================== CREATING WDGETS ============================
    
    consoleGameButton = Button(text="Play Console Game", height='3', width='20', command=Console)
    visualGameButton = Button(text="Play Visual Game", height='3', width='20', command=Visual)
    visualGameButton.pack(side='right',expand=True)
    consoleGameButton.pack(side='left',expand=True)
    
    root.mainloop()

#============================= START GAME ==============================

OpenGUI()

#================================ END ==================================

# Author       :  Jackson Currie
# Date         :  2015-08-04
# Description  :  Startup GUI for console and GUI

# GUI library
import tkinter

# Console game
import ConsoleGame

# GUI game
import GUIGame

# Opens visual game
def Visual():
    
    # Close GUI
    root.destroy()
    
    # Run visual game
    GUIGame.GetInputs()
    OpenGUI()

# Runs console game
def Console():
    
    # Close GUI
    root.destroy()
    
    # Run console game
    try:
        ConsoleGame.Run()
    except KeyboardInterrupt:
        OpenGUI()

# Run program
def OpenGUI():
    
    # Creating GUI
    global root
    root = tkinter.Tk()
    root.geometry("600x300+350+100")
    root.title("Take-Away Game")

    # Creating GUI widgets
    consoleGameButton = tkinter.Button(text="Play Console Game", height='3', width='20', command=Console)
    visualGameButton = tkinter.Button(text="Play Visual Game", height='3', width='20', command=Visual)
    # Setting GUI widgets
    visualGameButton.pack(side='right',expand=True)
    consoleGameButton.pack(side='left',expand=True)

    # GUI mainloop
    root.mainloop()

# Run program
OpenGUI()

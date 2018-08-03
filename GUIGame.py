# Author       :  Jackson Currie
# Date         :  2015-08-04
# Description  :  GUI game

# GUI library
import tkinter
from tkinter import messagebox

# New game
def OpenGame():

    # Variables
    global game
    global pileOfChips
    global whichPlayer
    global turns
    global removedChips
    global player1_score
    global player2_score
    global roundNumber
    global chipArea
    global numberOfChips
    global endTurn
    global numberOfTurns
    global whichPlayerLabel
    global p1_score
    global p2_score

    # Create GUI
    game = tkinter.Tk()
    game.title('Take-Away Game')
    game.geometry('900x450+200+100')

    # Create Frames
    player1_side = tkinter.Frame(bg='blue', height='450', width='200')
    player1_side.pack(side='left')
    centre = tkinter.Frame(height='450', width='500')
    centre.pack(side='left')
    topRow = tkinter.Frame(centre)
    topRow.pack(side='top')
    bottomRow = tkinter.Frame(centre)
    bottomRow.pack(side='bottom')
    secondBottomRow = tkinter.Frame(centre)
    secondBottomRow.pack(side='bottom')
    player2_side = tkinter.Frame(bg='blue', height='450', width='200')
    player2_side.pack(side='left')

    # Set images
    chip = tkinter.PhotoImage(file='images/squareChip.gif')
    bag = tkinter.PhotoImage(file='images/squareBag.gif')

    # Starting variables
    pileOfChips = 21
    whichPlayer = 1
    turns = 1
    removedChips = 0
    player1_score = 0
    player2_score = 0
    roundNumber = 0

    # Create widgets
    whichPlayerLabel = tkinter.Label(topRow, text=player1_name, font=('veranda', '14'))
    whichPlayerLabel.pack(side='left')
    playersTurn = tkinter.Label(topRow, text="'s turn.", font=('veranda', '14'))
    playersTurn.pack(side='left')
    endTurn = tkinter.Button(centre, text='End Turn', width='12', font=('veranda','10','bold'), command=SwitchTurn, state=tkinter.DISABLED)
    endTurn.pack(pady='20')
    chipArea = tkinter.Label(image=chip, bg='red')
    bagArea = tkinter.Label(centre, image=bag)
    bagArea.pack(padx='100')
    chipsRemaining = tkinter.Label(secondBottomRow, text='Chips remaining: ', font=('veranda', '11'))
    chipsRemaining.pack(side='left')
    numberOfChips = tkinter.Label(secondBottomRow, text=pileOfChips, font=('veranda', '11', 'bold'))
    numberOfChips.pack(side='left', pady=20)
    numberOfTurnsLabel = tkinter.Label(bottomRow, text='Turn: ', font=('veranda', '9'))
    numberOfTurnsLabel.pack(side='left')
    numberOfTurns = tkinter.Label(bottomRow, text=turns, font=('veranda', '9'))
    numberOfTurns.pack(side='left')
    player1 = tkinter.Label(player1_side, text=player1_name, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    player1.place(x='10', y='15')
    p1_scoreLabel = tkinter.Label(player1_side, text='Score: ', font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p1_scoreLabel.place(x='10', y='400')
    p1_score = tkinter.Label(player1_side, text=player1_score, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p1_score.place(x='70', y='400')
    player2 = tkinter.Label(player2_side, text=player2_name, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    player2.place(x='10', y='15')
    p2_scoreLabel = tkinter.Label(player2_side, text='Score: ', font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p2_scoreLabel.place(x='10' ,y='400')
    p2_score = tkinter.Label(player2_side, text=player2_score, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p2_score.place(x='70', y='400')

    # Bind click to chip pile
    bagArea.bind('<B1-Motion>', Motion)
    game.bind('<ButtonRelease-1>', MotionStop)

    # GUI mainloop
    game.mainloop()

# When holding chip
def Motion(event):
    global chipArea
    chipArea.place(x = (event.x+270), y = (event.y+110))

# When chip is released
def MotionStop(event):

    # Variables
    global removedChips
    global pileOfChips

    # Release chip
    chipArea.place_forget()

    # Check for player
    if whichPlayer % 2 == 1:
        if event.x+300 < 200:

            # Take a chip away
            removedChips += 1
            pileOfChips -= 1
            numberOfChips.configure(text=pileOfChips)

    # Check for player 
    elif whichPlayer % 2 == 0:
        if event.x+300 > 700:

            # Take a chip away
            removedChips += 1
            pileOfChips -= 1
            numberOfChips.configure(text=pileOfChips)

    # When out of chips
    if pileOfChips == 0:
        RoundOver()

    # If maximum chips are taken
    if removedChips == 3:
        SwitchTurn()
        endTurn.configure(state=tkinter.DISABLED)

    # Don't allow switch turn button
    elif removedChips == 0:
        endTurn.configure(state=tkinter.DISABLED)
        
    # Allow button
    else:
        endTurn.configure(state=tkinter.NORMAL)

# Change players turn
def SwitchTurn():

    # Variables
    global removedChips
    global whichPlayer
    global turns

    # Reset chips
    removedChips = 0

    # Add a turn
    turns += 1
    numberOfTurns.configure(text=turns)
    whichPlayer += 1

    # Check for next player
    if whichPlayer % 2 == 1:
        whichPlayerLabel.configure(text=player1_name)
    elif whichPlayer % 2 == 0:
        whichPlayerLabel.configure(text=player2_name)

# When game is finished
def Leave():
    global game
    game.destroy()

# End of round
def RoundOver():

    # Display end
    messagebox.showinfo('Rounds', 'Round Over!')

    # Variables
    global numberOfRounds
    global roundNumber
    global pileOfChips
    global turns
    global whichPlayer
    global player1_score
    global player2_score
    global game

    # Reset game data
    turns = 0
    numberOfTurns.configure(text=turns)
    pileOfChips = 21
    numberOfChips.configure(text=pileOfChips)
    roundNumber += 1

    # Check for winner
    if whichPlayer % 2 == 1:
        player1_score += 1
        p1_score.configure(text=player1_score)
    elif whichPlayer % 2 == 0:
        player2_score += 1
        p2_score.configure(text=player2_score)

    # Reset player
    whichPlayer = 0
    SwitchTurn()

    # Check if end
    if roundNumber == numberOfRounds:

        # Check winner
        if player1_score > player2_score:
            winnerName = player1_name
            winnerScoreDifference = player1_score-player2_score
        elif player2_score > player1_score:
            winnerName = player2_name
            winnerScoreDifference = player2_score-player1_score

        # Draw
        else:
            winnerName = 'a draw!'
            winnerScoreDifference = 0

        # End game
        endTurn.configure(state=tkinter.DISABLED)

        # Create winner dispay box
        winnerBox = tkinter.Frame(bg='grey')
        winnerBox.place(x='150',y='80')
        winnerTitleName = tkinter.Frame(winnerBox)
        winnerTitleName.pack(padx='150', pady='20')
        winnerTitleScore = tkinter.Frame(winnerBox)
        winnerTitleScore.pack(pady='50')
        winnerNameLabel = tkinter.Label(winnerTitleName, text='The winner is: ', font=('veranda', '20'), bg='grey')
        winnerNameLabel.pack(side='left')
        winnerActualName = tkinter.Label(winnerTitleName, text=winnerName, font=('veranda', '20', 'bold'), bg='grey')
        winnerActualName.pack(side='left')
        winnerScoreLabel = tkinter.Label(winnerTitleScore, text='Score difference: ', font=('veranda', '14'), bg='grey')
        winnerScoreLabel.pack(side='left')
        winnerActualScore = tkinter.Label(winnerTitleScore, text=winnerScoreDifference, font=('veranda', '14', 'bold'), bg='grey')
        winnerActualScore.pack(side='left')
        returnHome = tkinter.Button(winnerBox, text='Return Home', bg='grey', command=Leave)
        returnHome.pack(pady='20')

        # Unbind click
        game.unbind('<ButtonRelease-1>')

# Getting intital variables    
def GetVariables(event):

    # Variables
    global player1_name
    global player2_name
    global numberOfRounds

    # Input data
    player1_name = player1_input.get()
    player2_name = player2_input.get()
    roundsCheck = roundNumberInput.get()

    # Check data
    try:
        numberOfRounds = int(roundsCheck)

    # Not a number
    except ValueError:
        messagebox.showerror('Rounds', "Sorry the number of rounds must be an integer")
        numberOfRounds = 0

    # Names are the same
    if player1_name == player2_name:
        messagebox.showerror('Names', "Sorry names can't be the same")

    # Names are empty
    elif player1_name == '' or player2_name == '':
        messagebox.showerror('Names', "Sorry your name can't be blank")

    # Names are too long
    elif len(player1_name) > 20 or len(player2_name) > 20:
        messagebox.showerror('Names', "Sorry please enter a name shroter than 20 characters")

    # Names correct
    else:

        # Number of rounds too small
        if numberOfRounds < 1:
            messagebox.showerror('Rounds', "Sorry the number of rounds must be greater than 0")

        # All correct, start game
        else:
            startInputs.destroy()
            OpenGame()


# Starting Screen for inputs                
def GetInputs():

    # Variables
    global player1_input
    global player2_input
    global roundNumberInput
    global startInputs

    # Create GUI
    startInputs = tkinter.Tk()
    startInputs.title("")
    startInputs.geometry("500x200+400+200")

    # On screen widgets
    player1_input = tkinter.Entry()
    p1_inputLabel = tkinter.Label(text="Enter first players name: ", font=('veranda', '9'))
    p1_inputLabel.grid(row='0', column='0', sticky='e', pady='10', padx='10')
    player1_input.grid(row='0', column='1')
    player2_input = tkinter.Entry()
    p2_inputLabel = tkinter.Label(text="Enter second players name: ", font=('veranda', '9'))
    p2_inputLabel.grid(row='1', column='0', sticky='e', pady='10', padx='10')
    player2_input.grid(row='1', column='1')
    roundInputLabel = tkinter.Label(text="Enter the number of rounds you wish to play: ", font=('veranda', '9'))
    roundNumberInput = tkinter.Entry()
    roundInputLabel.grid(row='2', column='0', sticky='e', pady='10', padx='10')
    roundNumberInput.grid(row='2', column='1')
    getInputs = tkinter.Label(text='Press [Enter] to continue', font=('veranda', '9', 'bold'))
    getInputs.grid(row='3', sticky='e', pady='30')

    # Bind Enter key to check variables
    startInputs.bind('<Return>', GetVariables)

    # GUI mainloop
    startInputs.mainloop()

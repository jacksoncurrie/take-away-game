#=============================== LIBRARIES ====================================

from tkinter import *
from tkinter import messagebox

#=========================== INITIALIZING WINDOW ==============================

def OpenGame():
    global game
    game = Tk()
    game.title('Take-Away Game')
    game.geometry('900x450+200+100')
    player1_side = Frame(bg='blue', height='450', width='200')
    player1_side.pack(side='left')
    centre = Frame(height='450', width='500')
    centre.pack(side='left')
    topRow = Frame(centre)
    topRow.pack(side='top')
    bottomRow = Frame(centre)
    bottomRow.pack(side='bottom')
    secondBottomRow = Frame(centre)
    secondBottomRow.pack(side='bottom')
    player2_side = Frame(bg='blue', height='450', width='200')
    player2_side.pack(side='left')

#============================ WIDGET VARIABLES ================================

    chip = PhotoImage(file='images/squareChip.gif')
    bag = PhotoImage(file='images/squareBag.gif')
    global pileOfChips
    pileOfChips = 21
    global whichPlayer
    whichPlayer = 1
    global turns
    turns = 1
    global removedChips
    removedChips = 0
    global player1_score
    player1_score = 0
    global player2_score
    player2_score = 0
    global roundNumber
    roundNumber = 0

#============================ CREATING WIDGETS ================================

    global chipArea
    global numberOfChips
    global endTurn
    global numberOfTurns
    global whichPlayerLabel
    global p1_score
    global p2_score
    
    whichPlayerLabel = Label(topRow, text=player1_name, font=('veranda', '14'))
    whichPlayerLabel.pack(side='left')
    playersTurn = Label(topRow, text="'s turn.", font=('veranda', '14'))
    playersTurn.pack(side='left')
    endTurn = Button(centre, text='End Turn', width='12', font=('veranda','10','bold'), command=SwitchTurn, state=DISABLED)
    endTurn.pack(pady='20')
    chipArea = Label(image=chip, bg='red')
    bagArea = Label(centre, image=bag)
    bagArea.pack(padx='100')
    bagArea.bind('<B1-Motion>', Motion)
    game.bind('<ButtonRelease-1>', MotionStop)
    chipsRemaining = Label(secondBottomRow, text='Chips remaining: ', font=('veranda', '11'))
    chipsRemaining.pack(side='left')
    numberOfChips = Label(secondBottomRow, text=pileOfChips, font=('veranda', '11', 'bold'))
    numberOfChips.pack(side='left', pady=20)
    numberOfTurnsLabel = Label(bottomRow, text='Turn: ', font=('veranda', '9'))
    numberOfTurnsLabel.pack(side='left')
    numberOfTurns = Label(bottomRow, text=turns, font=('veranda', '9'))
    numberOfTurns.pack(side='left')
    player1 = Label(player1_side, text=player1_name, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    player1.place(x='10', y='15')
    p1_scoreLabel = Label(player1_side, text='Score: ', font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p1_scoreLabel.place(x='10', y='400')
    p1_score = Label(player1_side, text=player1_score, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p1_score.place(x='70', y='400')
    player2 = Label(player2_side, text=player2_name, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    player2.place(x='10', y='15')
    p2_scoreLabel = Label(player2_side, text='Score: ', font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p2_scoreLabel.place(x='10' ,y='400')
    p2_score = Label(player2_side, text=player2_score, font=('veranda', '12', 'bold'), fg='white', bg='blue')
    p2_score.place(x='70', y='400')
    
    game.mainloop()

#============================ MAIN GAME FUNTIONS ================================

def Motion(event):
    global chipArea
    chipArea.place(x = (event.x+270), y = (event.y+110))

def MotionStop(event):
    global removedChips
    global pileOfChips
    chipArea.place_forget()
    if whichPlayer % 2 == 1:
        if event.x+300 < 200:
            removedChips += 1
            pileOfChips -= 1
            numberOfChips.configure(text=pileOfChips)
    elif whichPlayer % 2 == 0:
        if event.x+300 > 700:
            removedChips += 1
            pileOfChips -= 1
            numberOfChips.configure(text=pileOfChips)
    if pileOfChips == 0:
                RoundOver()
    if removedChips == 3:
        SwitchTurn()
        endTurn.configure(state=DISABLED)
    elif removedChips == 0:
        endTurn.configure(state=DISABLED)
    else:
        endTurn.configure(state=NORMAL)
    return

def SwitchTurn():
    global removedChips
    global whichPlayer
    removedChips = 0
    global turns
    turns += 1
    numberOfTurns.configure(text=turns)
    whichPlayer += 1
    if whichPlayer % 2 == 1:
        whichPlayerLabel.configure(text=player1_name)
    elif whichPlayer % 2 == 0:
        whichPlayerLabel.configure(text=player2_name)
    return

def Leave():
    global game
    game.destroy()

def RoundOver():
    messagebox.showinfo('Rounds', 'Round Over!')
    global numberOfRounds
    global roundNumber
    global pileOfChips
    global turns
    turns = 0
    numberOfTurns.configure(text=turns)
    pileOfChips = 21
    numberOfChips.configure(text=pileOfChips)
    roundNumber += 1
    global whichPlayer
    if whichPlayer % 2 == 1:
        global player1_score
        player1_score += 1
        p1_score.configure(text=player1_score)
    elif whichPlayer % 2 == 0:
        global player2_score
        player2_score += 1
        p2_score.configure(text=player2_score)
    whichPlayer = 0
    SwitchTurn()
    if roundNumber == numberOfRounds:
        if player1_score > player2_score:
            winnerName = player1_name
            winnerScoreDifference = player1_score-player2_score
        elif player2_score > player1_score:
            winnerName = player2_name
            winnerScoreDifference = player2_score-player1_score
        else:
            winnerName = 'a draw!'
            winnerScoreDifference = 0
        endTurn.configure(state=DISABLED)
        winnerBox = Frame(bg='grey')
        winnerBox.place(x='150',y='80')
        winnerTitleName = Frame(winnerBox)
        winnerTitleName.pack(padx='150', pady='20')
        winnerTitleScore = Frame(winnerBox)
        winnerTitleScore.pack(pady='50')
        winnerNameLabel = Label(winnerTitleName, text='The winner is: ', font=('veranda', '20'), bg='grey')
        winnerNameLabel.pack(side='left')
        winnerActualName = Label(winnerTitleName, text=winnerName, font=('veranda', '20', 'bold'), bg='grey')
        winnerActualName.pack(side='left')
        winnerScoreLabel = Label(winnerTitleScore, text='Score difference: ', font=('veranda', '14'), bg='grey')
        winnerScoreLabel.pack(side='left')
        winnerActualScore = Label(winnerTitleScore, text=winnerScoreDifference, font=('veranda', '14', 'bold'), bg='grey')
        winnerActualScore.pack(side='left')
        returnHome = Button(winnerBox, text='Return Home', bg='grey', command=Leave)
        returnHome.pack(pady='20')

#===================== NAMES AND ROUNDS INPUT WINDOW ==========================
    
def GetVariables(event):
    global player1_name
    player1_name = player1_input.get()
    global player2_name
    player2_name = player2_input.get()
    roundsCheck = roundNumberInput.get()
    try:
        global numberOfRounds
        numberOfRounds = int(roundsCheck)
    except ValueError:
        messagebox.showerror('Rounds', "Sorry the number of rounds must be an integer")
        numberOfRounds = 0
    if player1_name == player2_name:
        messagebox.showerror('Names', "Sorry names can't be the same")
    elif player1_name == '' or player2_name == '':
        messagebox.showerror('Names', "Sorry your name can't be blank")
    elif len(player1_name) > 20 or len(player2_name) > 20:
        messagebox.showerror('Names', "Sorry please enter a name shroter than 20 characters")
    else:
        if numberOfRounds < 1:
            messagebox.showerror('Rounds', "Sorry the number of rounds must be greater than 0")
        else:
            startInputs.destroy()
            OpenGame()
                
def GetInputs():
    global player1_input
    global player2_input
    global roundNumberInput
    global startInputs
    startInputs = Tk()
    startInputs.title("")
    startInputs.geometry("500x200+400+200")
    player1_input = Entry()
    p1_inputLabel = Label(text="Enter first players name: ", font=('veranda', '9'))
    p1_inputLabel.grid(row='0', column='0', sticky='e', pady='10', padx='10')
    player1_input.grid(row='0', column='1')
    player2_input = Entry()
    p2_inputLabel = Label(text="Enter second players name: ", font=('veranda', '9'))
    p2_inputLabel.grid(row='1', column='0', sticky='e', pady='10', padx='10')
    player2_input.grid(row='1', column='1')
    roundInputLabel = Label(text="Enter the number of rounds you wish to play: ", font=('veranda', '9'))
    roundNumberInput = Entry()
    roundInputLabel.grid(row='2', column='0', sticky='e', pady='10', padx='10')
    roundNumberInput.grid(row='2', column='1')
    getInputs = Label(text='Press Return to continue', font=('veranda', '9', 'bold'))
    getInputs.grid(row='3', sticky='e', pady='30')
    startInputs.bind('<Return>', GetVariables)
    startInputs.mainloop()

#================================== END ========================================

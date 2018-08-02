#============================= MAIN FUNCTION ===================================

def Run():

#============================== CONSTANTS ======================================
    
    NUMBER_OF_PLAYERS = 2
    STARTING_CHIPS = 21
    MIN_CHIPS = 1
    SCORES = 1
    NAMES = 0
    FIRST_PLAYER = 0

#============================== VARIABLES ======================================

    max_chips = 3
    playersJoined = 0
    players = ([],[])
    draw = []
    roundNumber = 1
    numberOfRounds = 0
    pileOfChips = 0
    turns = 0
    whichPlayer = 0
    winnerCheck = 1
    chipsToRemove = 0
    draw = []
    name = ''
    winnerName = ''
    winnerScore = 0
    winnerName = ''
    playersInDraw = 0

#========================== START OF GAME OUTPUTS ===============================

    print('\n====================== NEW GAME ==========================\n')
    
    print('Type "[ctrl]+[c]" at any time to return to home screen', end='\n\n')

    print('Take-away Game, Created by Jackson Currie.', end='\n\n')

    print('This is a simple game which involves two players taking chips away from a plie. Each player has one turn each, where they may take one, two or three chips away from the pile before the next player has a turn. The winner is dictated by the person who takes away the 21st chip (which will be the last chip in the pile).', end='\n\n')

#============================== NAMES INPUT =====================================

    while name == '' or name in players[NAMES] and playersJoined < NUMBER_OF_PLAYERS:

        name = input('Please enter your name: ')

        if name == '':

            print('\nSorry, your name cannot be blank. Please try again.', end='\n\n')

        elif name in players[NAMES]:

            print('\nSorry, you cannot have the same name as another player. Please try again', end='\n\n')
            
        else:

            players[NAMES].append(name)

            players[SCORES].append(0)

            print('\nWelcome ' + name + '. Enjoy the game.', end='\n\n')

            playersJoined += 1

#========================== NUMBER OF ROUNDS INPUT ================================

    while numberOfRounds < 1:

        roundFail = False

        roundsInput = input('Please enter the number of rounds you wish to play: ')

        try:

            numberOfRounds = int(roundsInput)

        except ValueError:

            print('\nSorry, the number of rounds must be an integer.', end='\n\n')

            roundFail = True

        if numberOfRounds < 1 and not roundFail:

            print('\nSorry, the number of rounds must be higher than 0. Please try again.', end='\n\n')

#============================= MAIN GAME LOOP =====================================

    while roundNumber <= numberOfRounds:

        pileOfChips = STARTING_CHIPS

        whichPlayer = -1

        turns = 0

        print('\n******************** ROUND', roundNumber, '********************')

#============================== SETTING PLAYER =====================================

        while pileOfChips > 0:

            whichPlayer += 1
        
            if whichPlayer >= NUMBER_OF_PLAYERS:
        
                whichPlayer = FIRST_PLAYER

            print('\n---------------- ' + players[NAMES][whichPlayer] + "'s, turn -----------------", end='\n\n')

            print('There is', pileOfChips, 'chip(s) remaining.', end='\n\n')

            chipsToRemove = 0

#=========================== CHIPS TO TAKE-AWAY INPUT ==============================

            while chipsToRemove <= 0 or chipsToRemove > 3:

                if pileOfChips <= 3:

                    max_chips = pileOfChips

                else:

                    max_chips = 3

                chipFail = False

                chipsInput = input('How many chips do you wish to remove: ')

                try:

                    chipsToRemove = int(chipsInput)

                except ValueError:

                    print('\nSorry, the chips you wish to remove must be an integer.', end='\n\n')

                    chipFail = True

                if chipsToRemove > max_chips or chipsToRemove < MIN_CHIPS and not chipFail:

                    print('\nSorry, you may only take a maximum of', max_chips, 'chip(s), and a minimum of', MIN_CHIPS, 'chip. Please try again.', end='\n\n')

                    chipsToRemove = 0

            pileOfChips -= chipsToRemove

            turns += 1

#=============================== END OF ROUND SCORING ===============================

        players[SCORES][whichPlayer] += 1

        print('\n****************** ROUND OVER ******************', end='\n\n')
        
        print('It took', turns, 'turns.', players[NAMES][whichPlayer], 'is the winner of this round.', end='\n\n')

        print('You have played', roundNumber, 'round(s).', end='\n\n')

        playersJoined -= NUMBER_OF_PLAYERS

        while playersJoined < NUMBER_OF_PLAYERS:

            print(players[NAMES][playersJoined] + "'s score is: ", players[SCORES][playersJoined])

            playersJoined += 1

        playersJoined = NUMBER_OF_PLAYERS

        roundNumber += 1

#============================= IDENTIFYING THE WINNER(S) ==============================

    winnerScore = players[SCORES][FIRST_PLAYER]

    winnerName = players[NAMES][FIRST_PLAYER]

    draw = [FIRST_PLAYER]

    while winnerCheck < NUMBER_OF_PLAYERS:

        if players[SCORES][winnerCheck] > winnerScore:

            winnerScore = players[SCORES][winnerCheck]

            winnerName = players[NAMES][winnerCheck]

            draw = []

        elif players[SCORES][winnerCheck] == winnerScore:

            draw.append(winnerCheck)

        winnerCheck += 1

#=============================== OUTPUTING WINNER(S) ====================================

    print('\n====================== GAME OVER ========================', end='\n\n')
    
    if len(draw) > 1:
        
        while playersInDraw < len(draw):

            print(players[NAMES][draw[playersInDraw]], end='')

            if playersInDraw == len(draw) - 2:

                print(' and ', end='')

            else:

                print(', ', end='')

            playersInDraw += 1

        print('drew this game with scores of', winnerScore, end='\n\n')

    else:
        
        print(winnerName, 'won this game with a score of', winnerScore, end ='\n\n')

    input("---Press [ctrl]+[c] to return to home screen, or [ENTER] key to close---\n")

#================================== END OF GAME ===========================================

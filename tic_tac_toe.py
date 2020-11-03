from random import *

game_being_played = True
winner = None
current_player = True

def init_gameboard():
    #creating board
    gameboard=["-", "-", "-",
               "-", "-", "-",
               "-", "-", "-"]
    return gameboard

def showgameboard(gameboard,display):
    if display=="index":
        #displaying board to show user how index works
        print("1 | 2 | 3")
        print("---------")
        print("4 | 5 | 6")
        print("---------")
        print("7 | 8 | 9")
    elif display=="game":
        #I beleive it can be accompished with just 5 lines
        #Can confirm that this works perfectly
        print(gameboard[0]+" | "+gameboard[1]+" | "+gameboard[2])
        print("---------")
        print(gameboard[3]+" | "+gameboard[4]+" | "+gameboard[5])
        print("---------")
        print(gameboard[6]+" | "+gameboard[7]+" | "+gameboard[8])

        #Don't need any of this down here
        """ gameline=['-',' ','|',' ','-',' ','|',' ','-']
        index=0
        for item in gameboard[0:3]:
            if item == 'X':
                gameline[index] = 'X'
            elif item == 'O':
                gameline[index] = 'O'
            index+=4
        print("".join(gameline))
        print("---------")

        gameline2=['-',' ','|',' ','-',' ','|',' ','-']
        index=0
        for item in gameboard[3:6]:
            if item == 'X':
                gameline2[index] = 'X'
            elif item == 'O':
                gameline2[index] = 'O'
            index+=4
        print("".join(gameline2))
        print("---------")

        gameline3=['-',' ','|',' ','-',' ','|',' ','-']
        index=0
        for item in gameboard[6:]:
            if item == 'X':
                gameline3[index] = 'X'
            elif item == 'O':
                gameline3[index] = 'O'
            index+=4
        print("".join(gameline3))
        print("---------") """

def print_instructions(gameboard,display):
    #introductory print
    print("Welcome to Tik-Tak-Toe by Camels_1")
    print("This is a two-player tik-tak-toe game. The game is turn-based and played on a 3x3 grid,"\
    "where the goal is to match your symbol 3 in a row horizontally, vertically, or diagonally."\
    " Try and get a match before your opponent does while also blocking them from winning. You will be prompted"\
    " to enter your name and pick your symbol, then enter moves one after another. The board is indexed like this:\n")
    showgameboard(gameboard,display)
    print("\nTo place a symbol, enter the index of the location you want to move in when prompted.\n")
    print("Press 'Enter' when you are ready to continue")
    input()

def get_names():
    #gets names, stores them in list temporarily
    p1_name = input("Player 1, enter your name: ")
    p2_name = input("Player 2, enter your name: ")
    player_names = [p1_name,p2_name]
    return player_names

def pick_symbol(names):
    #user picks symbols
    picking = True
    while(picking):
        p1_string = str(names[0]) + " enter your symbol (X/O): "
        p1_symbol = input(p1_string)

        if p1_symbol == "X" or p1_symbol == "x":
            p1_symbol = "X"
            p2_symbol = "O"
            print(names[1]+", your symbol is 'O'.")
            print(names[0]+", your symbol is 'X'.")
            picking = False
        elif p1_symbol == "O" or p1_symbol == "o":
            p1_symbol = "O"
            p2_symbol="X"
            print(names[0]+", your symbol is 'O'.")
            print(names[1]+", your symbol is 'X'.")
            picking = False
        else:
            print("Sorry, that is not an option. Please enter X or O.")
        
    playerdata ={
        names[0]:p1_symbol,
        names[1]:p2_symbol
    }
    return p1_symbol, p2_symbol

def rand_start():
    #randomly picks which player is going to start
    starting = randrange(0,2)
    if starting == 0:
        current_player = True
        return "1"
    else:
        current_player = False
        return "2"
    
def user_turn(player, gameboard, p1_symbol, p2_symbol,playernames):
    turn = True
    #sets the correct name for the player
    if(player):
        name = playernames[0]
    else:
        name = playernames[1]
    while(turn):
        #empty print statements to create more spacing
        print()
        #put the index board in every turn so its easier for the user
        showgameboard(gameboard, "index")
        print()
        print("=========")
        print()
        showgameboard(gameboard,"game")
        #prompts player to input move (index 1-9)
        #should say here whos turn it is
        print(name + " it is your turn")
        position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if(gameboard[position] == "-"):
            if(player):
                gameboard[position] = p1_symbol
                turn = False
            else:
                gameboard[position] = p2_symbol
                turn = False
        else:
            print("That position is already taken, please enter a new one.")
   
def win_check(gameboard, playernames, p1_symbol, p2_symbol):
    
    #check rows
    if(check_rows(gameboard)):
        return True
    #check columns
    if(check_columns(gameboard)):
        return True
    #check diagonals
    if(check_diagonals(gameboard)):
        return True
    else:
        return False
    
def check_rows(gameboard, playernames, p1_symbol, p2_symbol):
    global game_being_played
    
    if(gameboard[0] == gameboard[1] == gameboard[2] and gameboard[0] !=  "-"):
        if(gameboard[0] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    elif(gameboard[3] == gameboard[4] == gameboard[5] and gameboard[3] !=  "-"):
        if(gameboard[3] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    elif(gameboard[6] == gameboard[7] == gameboard[8] and gameboard[8] !=  "-"):
        if(gameboard[6] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    else:
        return None

def check_columns(gameboard, playernames, p1_symbol, p2_symbol):
    global game_being_played
    
    if(gameboard[0] == gameboard[3] == gameboard[6] and gameboard[0] !=  "-"):
        if(gameboard[0] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    elif(gameboard[1] == gameboard[4] == gameboard[7] and gameboard[1] !=  "-"):
        if(gameboard[1] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    elif(gameboard[2] == gameboard[5] == gameboard[8] and gameboard[2] !=  "-"):
        if(gameboard[2] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    else:
        return None    

def check_diagonals(gameboard, playernames, p1_symbol, p2_symbol):
    global game_being_played

    if(gameboard[0] == gameboard[4] == gameboard[8] and gameboard[0] !=  "-"):
        if(gameboard[0] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    elif(gameboard[2] == gameboard[4] == gameboard[6] and gameboard[2] !=  "-"):
        if(gameboard[2] == p1_symbol):
            winner = playernames[0]
            return winner
        else:
            winner = playernames[1]
            return winner
    else:
        return None

def tie_check(gameboard):
    global game_being_played 
    
    #Checks if board is full and there is a tie
    if "-" not in gameboard:
        return True

def switch_player():
    global current_player
    
    if current_player == True:
        current_player = False
    elif current_player == False:
        current_player = True
    return
    
def new_game():
    #if win_check is true, initialize a new game
    gameboard=init_gameboard()
    introdisplay="index"
    print_instructions(gameboard,introdisplay)
    playernames=get_names()
    playerdata=pick_symbol(playernames)
    start = rand_start()
    
def play_tic_tac_toe():
    gameboard=init_gameboard()
    introdisplay="index"
    print_instructions(gameboard,introdisplay)
    playernames=get_names()
    p1_symbol, p2_symbol=pick_symbol(playernames)
    start = rand_start()
    game_being_played = True

    while game_being_played:
        user_turn(current_player, gameboard, p1_symbol, p2_symbol,playernames)
    
        if(check_rows(gameboard, playernames, p1_symbol, p2_symbol) == playernames[0] or check_columns(gameboard, playernames, p1_symbol, p2_symbol) == playernames[0] or check_diagonals(gameboard, playernames, p1_symbol, p2_symbol) == playernames[0]):
            winner = playernames[0]
            print(winner, "wins!")
            showgameboard(gameboard,"game")
            game_being_played = False
        elif(check_rows(gameboard, playernames, p1_symbol, p2_symbol) == playernames[1] or check_columns(gameboard, playernames, p1_symbol, p2_symbol) == playernames[1] or check_diagonals(gameboard, playernames, p1_symbol, p2_symbol) == playernames[1]):
             winner = playernames[1]
             print(winner, "wins!")
             showgameboard(gameboard,"game")
             game_being_played = False
        elif(tie_check(gameboard)):
            print("It's a tie!")
            showgameboard(gameboard,"game")
            game_being_played = False
        else:
            switch_player()

    playing_again = True
    while(playing_again):
        play_again = input('Would you like to play again? Enter yes or no: ')
        #directions say we must account for all inputs
        play_again = play_again.upper()
        if (play_again == "Y" or play_again == "YES"):
            play_tic_tac_toe()
            playing_again = False
        elif(play_again == "N" or play_again == "NO"):
            exit()
        else:
            print("Please enter yes or no: ")

play_tic_tac_toe()
    
            

        


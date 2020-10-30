from random import *

game_being_played = True
winner = None
current_player = player


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
    #elif display=="game":
        #code for displaying board during turns

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
    p1_string = str(names[0]) + " enter your symbol (X/O): "
    p1_symbol = input(p1_string)

    if p1_symbol == "X":
        p2_symbol = "O"
        print(names[1]+", your symbol is 'O'.")
    else:
        p2_symbol="X"
        print(names[1]+", your symbol is 'X'.")
    playerdata ={
        names[0]:p1_symbol,
        names[1]:p2_symbol
    }
    return playerdata

def rand_start():
    #randomly picks which player is going to start
    starting = randrange(0,1)
    if starting == 0:
        return "1"
    else:
        return "2"
    
def user_turn(player):
    turn = True
    while(turn):
        print(gameboard)
        #prompts player to input move (index 1-9)
        position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if(gameboard[position] == "-"):
            gameboard[position] = player
            turn = False
        else:
            print("That position is already taken, please enter a new one.")
   
def win_check():
    #checks if win
    global winner
    
    #check rows
    row_winner = check_rows()
    
    #check columns
    column_winner = check_columns()
    
    #check diagonals
    diag_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
        
    else:
        winner = None
    return
    
def check_rows():
    global game_being_played
    
    row_1 = gameboard[0] == gameboard[1] == gameboard[2] !=  "-" 
    row_2 = gameboard[3] == gameboard[4] == gameboard[5] !=  "-"
    row_3 = gameboard[6] == gameboard[7] == gameboard[8] !=  "-"
    
    if row_1 or row_2 or row_3:
        game_being_played = False
        
    if row_1:
        return gameboard[0]
    elif row_2:
        return gameboard[3]
    elif row_3:
        return gameboard[6]
    return

def check_columns():
    global game_being_played
    
    column_1 = gameboard[0] == gameboard[3] == gameboard[6] !=  "-" 
    column_2 = gameboard[1] == gameboard[4] == gameboard[7] !=  "-"
    column_3 = gameboard[2] == gameboard[5] == gameboard[8] !=  "-"
    
    if column_1 or column_2 or column_3:
        game_being_played = False
        
    if column_1:
        return gameboard[0]
    elif column_2:
        return gameboard[1]
    elif column_3:
        return gameboard[2]
    return       

def check_diagonals():
    global game_being_played
    
    diagonals_1 = gameboard[0] == gameboard[4] == gameboard[8] !=  "-" 
    diagonals_2 = gameboard[6] == gameboard[4] == gameboard[2] !=  "-"
    
    
    if diagonals_1 or diagonals_2:
        game_being_played = False
        
    if diagonals_1:
        return gameboard[0]
    elif diagonals_2:
        return gameboard[6]
    return       

def tie_check():
    global game_being_played 
    
    #Checks if board is full and there is a tie
    if "-" not in gameboard:
        game_being_played = False
    return

def switch_player():
    global current_player
    
    if current_player == p1_symbol:
        current_player = p2_symbol
    elif current_player == p2_symbol:
        current_player = p1_symbol
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
    new_game()
    game_being_played = True

    while game_being_played:
        user_turn(current_player)
    
        win_check()
    
        switch_player()
            
    if winner == p1_name or winner == p2_name:
        print(winner + "won!")
        game_being_played = False
    elif winner == None:
        print ("Tie Game.")
        game_being_played = False

    play_again = eval('Would you like to play again? Enter "Y" for yes or "N" for no.')
    if (play_again == "Y" or play_again == "y"):
        play_tic_tac_toe()
    else:
        exit()

play_tic_tac_toe()
    
            

        


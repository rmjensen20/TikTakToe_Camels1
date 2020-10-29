from random import *

def play_tic_tac_toe():

    def init_gameboard():
        #creating board
        gameboard=[]
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
        
    def main():
        gameboard=init_gameboard()
        introdisplay="index"
        print_instructions(gameboard,introdisplay)
        playernames=get_names()
        playerdata=pick_symbol(playernames)

        start = rand_start()

        
    main()

play_tic_tac_toe()
    
            

        


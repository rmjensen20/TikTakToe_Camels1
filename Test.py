from random import *
import unittest
from tic_tac_toe import check_rows
from tic_tac_toe import check_columns
from tic_tac_toe import check_diagonals
from tic_tac_toe import win_check
from tic_tac_toe import pick_symbol
from tic_tac_toe import rand_start

class Test(unittest.TestCase):

    def testRandAssign(self):
        randomcheck=0  # +-20 window allowed
        goodReturn=[1,2]
        for i in range(101):
            self.assertIn(rand_start(),goodReturn) #verifies that correct num chosen
            if rand_start() == 1:   #verifies that selection is actually random
                randomcheck=randomcheck+1
            else:
                randomcheck=randomcheck-1
        if randomcheck <= 20 and randomcheck >= -20:
            print("Suitable Randomness found,",randomcheck)
        else:
            print("Unsuitable Randomness found,",randomcheck)
            
                
    def testWin(self):
        Names = ['Player1','Player2']
        #These return the name of the winner

        #executes check_row on a board that has winning row
        gameboard=["X","X","X","-","-","-","-","-","-"]
        self.assertIn(check_rows(gameboard, Names,'X','O'), Names, "Win not found in rows")

        #executres check_columns on a board that has a winning column
        gameboard=["X","-","-","X","-","-","X","-","-"]
        self.assertIn(check_columns(gameboard, Names,'X','O'), Names, "Win not found in columns")

        #executes check_diagonals on a board that has a winning diagonal
        gameboard=["X","-","-","-","X","-","-","-","X"]
        self.assertIn(check_diagonals(gameboard, Names,'X','O'), Names, "Win not found in diagonals")

        print("Win check works for rows, columns, diagonals")

    def testInput(self):
        #valid symbols
        validInput = ["X","x","O","o"]
        result = pick_symbol(['Player1','Player2'],1)
        for x in result:
            self.assertIn(x, validInput, "Did not pick a valid input")
        print("Symbol selection works as intended, check misinputs properly")

if __name__ == '__main__':
        unittest.main()


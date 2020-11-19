import unittest
import tic_tac_toe

class Test(unittest.TestCase):

    def testRandAssign(self):
        randomcheck=0   # +-10 window allowed
        goodReturn=["1","2"]    #function is working as expected
        for i in range(101):
            self.assertIn(tic_tac_toe().rand_start,goodReturn,"Did not randomly pick player")
            if tic_tac_toe().rand_start == "1":
                randomcheck=randomcheck+1
            else:
                randomcheck=randomcheck-1
        if not (40 >= randomcheck <= 60):
            print("Unsuitable Randomness")
                
    def testWin(self):
        self.assertTrue(tic_tac_toe.check_rows, "No win found in rows")
        self.assertTrue(tic_tac_toe.check_columns, "No win found in columns")
        self.assertTrue(tic_tac_toe.check_diagonals, "No win found in diagonals")
        self.assertTrue(tic_tac_toe().win_check, "Win not found")

    def testInput(self):
        validInput = ["X","x","O","o"]
        result = tic_tac_toe().pick_symbol
        for x in result:
            self.assertIn(x, validInput, "Did not pick a valid input")

if __name__ == '__main__':
        unittest.main()
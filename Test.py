import unittest
import tic_tac_toe

class Test(unittest.TestCase):

    def testRandAssign(self): 
        self.

    def testWin(self):
        self.assertTrue(tic_tac_toe().win_check, "Win not found")

    def testInput(self):
        validInput = ["X","x","O","o"]
        self.assertIn(tic_tac_toe().pick_symbol, validInput, "Did not pick a valid input")

if __name__ == '__main__':
        unittest.main()

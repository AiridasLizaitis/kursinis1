import unittest
from kursinis import TicTacToe, TicTacToeWithLogging
 
class TestTicTacToe(unittest.TestCase):
    def test_initialization(self):
        game = TicTacToe()
        self.assertIsInstance(game, TicTacToe)
 
    def test_board_display(self):
        game = TicTacToe()
        expected_board = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',' '
        ]
        self.assertEqual(game.board, expected_board)
 
class TestTicTacToeWithLogging(unittest.TestCase):
    def test_initialization(self):
        game = TicTacToe()
        game_with_logging = TicTacToeWithLogging(game)
        self.assertIsInstance(game_with_logging, TicTacToeWithLogging)
 
    def test_log_winner(self):
        game = TicTacToe()
        winner_name = "Briusas"
        game.LogWinner(winner_name)
        with open("wins.txt", "r") as file:
            lines = file.readlines()
            self.assertIn(f"{winner_name} - ", lines[-1])
 
if __name__ == '__main__':
    unittest.main()
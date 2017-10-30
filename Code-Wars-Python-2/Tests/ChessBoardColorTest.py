import unittest
from ChessBoardColor import chess_board_cell_color

class ChessBoardTest(unittest.TestCase):
    def test(self):
        self.assertEqual(chess_board_cell_color("A1", "C3"), True)
        self.assertEqual(chess_board_cell_color("A1", "H3"), False)
        self.assertEqual(chess_board_cell_color("A1", "A2"), False)
        self.assertEqual(chess_board_cell_color("B5", "G8"), True)
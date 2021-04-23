import unittest
from gol import Cell, GameOfLife


class TestGameOFLife(unittest.TestCase):
    # def setUp(self) -> None:
    #     newGame = GameOfLife([
    #         [1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 0, 0],
    #         [0, 1, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0]])

    def test_GameOfLifeisInstanceable(self):
        new_game = GameOfLife([[Cell(0, (0, 0))]])
        self.assertTrue(isinstance(new_game, GameOfLife))


class TestCell(unittest.TestCase):

    def test_CellIsInstanceable(self):
        new_Cell = Cell(1, (0, 0))
        self.assertTrue(isinstance(new_Cell, Cell))








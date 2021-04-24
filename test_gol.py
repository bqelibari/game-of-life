import unittest
from gol import *


class TestGameOFLife(unittest.TestCase):
    def test_GameOfLifeisInstanceable(self):
        new_game = GameOfLife([[Cell(0, (0, 0))]])
        self.assertTrue(isinstance(new_game, GameOfLife))


class TestCell(unittest.TestCase):
    def test_CellIsInstanceable(self):
        new_Cell = Cell(1, (0, 0))
        self.assertTrue(isinstance(new_Cell, Cell))








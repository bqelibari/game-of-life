import unittest
from gol import *


class TestGameOFLife(unittest.TestCase):
    def test_GameOfLifeisInstanceable(self):
        new_game = GameOfLife([[Cell(0, (0, 0))]])
        self.assertTrue(isinstance(new_game, GameOfLife))

    def test_amountOfAliveNeighborCells(self):
        newGame = GameOfLife([
            [Cell(1, (0, 0)), Cell(0, (0, 1)), Cell(0, (0, 2))],
            [Cell(0, (1, 0)), Cell(1, (1, 1)), Cell(1, (1, 2))],
            [Cell(1, (2, 0)), Cell(0, (2, 1)), Cell(0, (2, 2))]])
        field_length = len(newGame.field[0]) - 1
        self.assertEqual(1, newGame.amount_of_alive_neighbors(newGame.field[0][0]))
        self.asertEqual(1, newGame.amount_of_alive_neighbors(newGame.field[field_length][0]))
        self.assertEqual(2, newGame.amount_of_alive_neighbors(newGame.field[0][field_length]))
        self.assertEqual(2, newGame.amount_of_alive_neighbors(newGame.field[field_length][field_length]))

    def test_getNeighborsOfAnyCell(self):
        newGame = GameOfLife([
            [Cell(1, (0, 0)), Cell(0, (0, 1)), Cell(0, (0, 2))],
            [Cell(1, (1, 0)), Cell(1, (1, 1)), Cell(1, (1, 2))],
            [Cell(1, (2, 0)), Cell(0, (2, 1)), Cell(0, (2, 2))]])
        self.assertEqual(2, sum(newGame._get_lifestate_of_neighbors(newGame.field[0][0])))
        self.assertEqual(4, sum(newGame._get_lifestate_of_neighbors(newGame.field[0][1])))
        self.assertEqual(2, sum(newGame._get_lifestate_of_neighbors(newGame.field[0][2])))


    def test_newGameAfterFirstRound(self):
        newGame = GameOfLife([
            [Cell(1, (0, 0)), Cell(0, (0, 1)), Cell(0, (0, 2))],
            [Cell(1, (1, 0)), Cell(1, (1, 1)), Cell(1, (1, 2))],
            [Cell(1, (2, 0)), Cell(0, (2, 1)), Cell(0, (2, 2))]])

        newGame.next_round()

        field =[[Cell(1, (0, 0)), Cell(0, (0, 1)), Cell(0, (0, 2))],
            [Cell(1, (1, 0)), Cell(0, (1, 1)), Cell(0, (1, 2))],
            [Cell(1, (2, 0)), Cell(0, (2, 1)), Cell(0, (2, 2))]]
        self.assertEqual(field, newGame.field)



class TestCell(unittest.TestCase):
    def test_CellIsInstanceable(self):
        new_Cell = Cell(1, (0, 0))
        self.assertTrue(isinstance(new_Cell, Cell))

    def test_CellDies(self):
        oneCell = Cell(1, (2, 3))
        oneCell.die()
        self.assertEqual(0, oneCell.state)

    def test_CellRevives(self):
        oneCell = Cell(0, (1, 2))
        oneCell.spawn()
        self.assertEqual(1, oneCell.state)

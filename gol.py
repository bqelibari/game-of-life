from dataclasses import dataclass


@dataclass
class Cell:
    alive: bool
    coordinates: tuple[int, int]


@dataclass
class GameOfLife:
    field: list[list[Cell]]

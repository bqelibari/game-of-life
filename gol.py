from dataclasses import dataclass
import copy


@dataclass
class Cell:
    state: bool
    coordinates: tuple[int, int]

    def die(self):
        self.state = 0

    def spawn(self):
        self.state = 1

    def is_alive(self):
        if self.state == 1:
            return True

    def is_dead(self):
        if self.state == 0:
            return True


@dataclass
class GameOfLife:
    field: list[list[Cell]]

    def amount_of_alive_neighbors(self, current_cell: Cell) -> int:
        return sum(self._get_lifestate_of_neighbors(current_cell))

    def _get_lifestate_of_neighbors(self, current_cell: Cell):
        origin = current_cell.coordinates
        neighbors_lifestate = []
        for idx_row, row in enumerate(self.field):
            for idx_column, cell in enumerate(row):
                if self.is_neighbor(idx_row, idx_column, origin):
                    neighbors_lifestate.append(cell.state)
        return neighbors_lifestate

    @staticmethod
    def is_neighbor(idx_row, idx_column, origin):
        difference_y = abs(idx_row - origin[0])
        difference_x = abs(idx_column - origin[1])
        if difference_y <= 1 and difference_x <= 1:
            if (idx_row, idx_column) != origin:
                return True

    def next_round(self):
        new_field = copy.deepcopy(self.field)
        for idx_row, row in enumerate(self.field):
            for idx_column, current_cell in enumerate(row):
                amount_of_living_neighbors = self.amount_of_alive_neighbors(current_cell)
                self._modify_cell_state(amount_of_living_neighbors, current_cell, new_field)
        self.field = new_field.copy()


    def _modify_cell_state(self, amount_of_living_neighbors: int, current_cell: Cell, new_field: list[list[Cell]]):
        x_coord, y_coord = current_cell.coordinates[0], current_cell.coordinates[1]
        if current_cell.is_dead() and amount_of_living_neighbors == 3:
            new_field[x_coord][y_coord].spawn()
        elif 2 <= amount_of_living_neighbors <=3:
            pass
        else:
            new_field[x_coord][y_coord].die()
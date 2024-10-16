import maze

class Robot:
    def __init__(self, maz: maze):
        self.position = maz.get_start_position()
        self.maz = maz
        self.finish = False
        self.moves = []

    def move(self) -> bool:
        """
        # Attempts to move the robot to the next best position
        :return: True if the robot moves, False otherwise.
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and self.maz.get_val_at(self.position[0] + i, self.position[1] + j) is not None:
                    move_position = self.position[0] + i, self.position[1] + j
                    if self.__best_move(move_position):
                        self.maz.increment_value(self.position)
                        self.position = move_position
                        self.moves.append((i , j))
                        return True
        return False

    def __best_move(self, move_position: tuple) -> bool:
        """
        Determines whether the proposed move is optimal based on neighboring cells
        :param move_position: That's a possible move position given by the function "move"
        :return: True if the neighboring cells have equal or higher access and are not exit cells.
        """
        if self.maz.get_val_at(move_position[0], move_position[1]) == 'E':
            self.finish = True
            return True
        for i in range(-1,2):
            for j in range(-1,2):
                if self.maz.get_val_at(self.position[0] + i, self.position[1] + j) is not None:
                    if not (i == 0 and j == 0):
                        if self.maz.get_val_at(self.position[0] + i, self.position[1] + j) == 'E':
                          return False
                        if self.maz.get_val_at(move_position[0],move_position[1]) > self.maz.get_val_at(self.position[0] + i, self.position[1] + j):
                            return False
        return True

    def robot_movement(self):
        """
        Converts the stored movement directions into human-readable format
        """
        directions = {
            (-1, -1): 'up-left',
            (-1, 0): 'up',
            (-1, 1): 'up-right',
            (0, -1): 'left',
            (0, 1): 'right',
            (1, -1): 'down-left',
            (1, 0): 'down',
            (1, 1): 'down-right'
        }

        move_strings = []
        for mov in self.moves:
            move_strings.append(directions[mov])

        return move_strings

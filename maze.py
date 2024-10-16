
class Maze:
    def __init__(self, file_path):
        self.maze = [] # Stores the maze as a matrix 2x2
        self.__load_maze(file_path) #loads the maze from a file
        self.start_position = self.__find_start_position() # Finds the starting position 'S'
        self.__replace_dots_with_zeros() # Replaces all '.' in order to count how many times the robot will visit the cell

    def __load_maze(self, file_path):
        """
        Loads the maze from the given file path.
        """
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    self.maze.append(list(line.strip())) # Each line is stripped of whitespace and added to the maze
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")

    def display_maze(self):
        """
        Displays the maze, with the number of access for each cell
        """
        for row in self.maze:
            print(''.join(str(char) for char in row))

    def get_val_at(self, row: int, col: int):
        """
        Returns the value of the cell at the given position, if it exists. Otherwise, returns None.
        """
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[row]) and self.maze[row][col] != '#':
            return self.maze[row][col]
        else:
            return None

    def __find_start_position(self):
        """
        Finds the start position of the maze.
        """
        for row in self.maze:
            if 'S' in row:
                self.start_position = (self.maze.index(row), row.index('S'))
                self.maze[self.start_position[0]][self.start_position[1]] = 0
                return self.start_position

    def get_start_position(self):
        """
        Returns the start position of the maze.
        """
        return self.start_position

    def __replace_dots_with_zeros(self):
        """
        Replaces all dots with zeros. In order to count numbers off access in the cells
        """
        for row_idx, row in enumerate(self.maze):
            for col_idx, char in enumerate(row):
                if char == '.':
                    self.maze[row_idx][col_idx] = 0

    def increment_value(self, position: tuple):
        """
        Given the position it will increase the value of the access.
        """
        self.maze[position[0]][position[1]] += 1
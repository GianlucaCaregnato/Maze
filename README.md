
# Maze Solver with Robot

This project simulates a robot navigating a maze. The maze is read from a text file and represented as a matrix of characters, where the robot starts from a defined position ('S'), and its goal is to reach the end position ('E'). The robot can traverse empty cells and track how many times each cell is visited during its journey.

## Project Structure

The project consists of three main components:

### 1. **Maze Class (`maze.py`)**
The `Maze` class represents the maze itself and provides the following key functionalities:
- **Maze Loading**: Reads a maze from a file where the maze is represented as a grid of characters. Walls are marked as `#`, empty spaces as `.`, the start position as `S`, and the end position as `E`.
- **Tracking Visits**: Replaces empty spaces (dots) with zeros and increments the number each time the robot visits the cell.
- **Start Position Identification**: Automatically finds the start position of the robot within the maze.
- **Maze Display**: Prints the current state of the maze, showing the number of visits to each cell.

### 2. **Robot Class (`robot.py`)**
The `Robot` class handles the movement of the robot within the maze and attempts to reach the end position. The robot:
- **Starts at a Predefined Position**: It starts at the position marked with `S` in the maze.
- **Moves in 8 Possible Directions**: The robot checks cells around its current position and makes moves based on the `best move` algorithm, ensuring it moves optimally toward the goal.
- **Tracks Moves**: The sequence of movements (up, down, left, right, and diagonal) is stored and can be retrieved for review.
- **Finish Condition**: The robot stops moving once it reaches the end position (`E`).

### 3. **Main Script (`main.py`)**
The main script ties everything together:
- **Maze Initialization**: Loads the maze from a file.
- **Robot Initialization**: Creates a robot that navigates the maze.
- **Movement Execution**: The robot continuously moves until it reaches the end.
- **Display Output**: After completing the navigation, the sequence of moves is printed, followed by a visual representation of the maze showing how many times each cell was visited.

## Usage

1. **Prepare Maze Files**: Create text files (e.g., `Maze1.txt`, `Maze2.txt`, etc.) containing the maze layout using the following symbols:
   - `S` - Starting position.
   - `E` - Ending position.
   - `#` - Wall.
   - `.` - Empty space.

2. **Run the Program**:
   - Ensure you have the maze file paths configured in the `main.py` script.
   - Run the program:
     ```bash
     python main.py
     ```

3. **Output**:
   - The program will display the sequence of moves the robot took (e.g., `up`, `right`, `down`), and it will show the maze with how many times the robot visited each accessible cell.

### Example Maze File (`Maze1.txt`):
```
S....
.###.
..E..
.#.#.
.....
```

### Example Output:
```
['right', 'right', 'right', 'right', 'down', 'down-left', 'left']
11111
0###1
00E10
0#0#0
00000
```

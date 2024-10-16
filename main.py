from maze import Maze
from robot import Robot


def main(file_path: str):
    """
    Main function to run the maze solver.

    Args:
        file_path (str): Path to the maze file.
    """
    try:
        # Load the maze from the provided file path
        maze = Maze(file_path)

        # Initialize the robot with the maze
        robot = Robot(maze)

        # Robot navigates the maze until it reaches the end
        while not robot.finish:
            if not robot.move():
                print("No valid moves available. The robot is stuck.")
                break

        # Output the sequence of movements the robot took
        print("Robot's Movement Path:", ' -> '.join(robot.robot_movement()))

        # Display the maze with the number of visits to each cell
        print("\nMaze with Access Count:")
        maze.display_maze()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Specify the maze file path (ensure the file exists in the directory)
    maze_file_path = 'Maze1.txt'

    # Run the main function with the specified maze file
    main(maze_file_path)


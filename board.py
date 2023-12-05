import pygame
from cell import Cell
from constants import *


class Board:
    def __init__(self, width, height, screen, difficulty, sudoku_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # extra board to compare user answer with solution
        self.board = sudoku_board

        self.board_rows = len(self.board)  # number of rows
        self.board_cols = len(self.board[0])  # number of columns

        # Create cells with sudoku_board values
        self.cells = [[Cell(self.board[row][col], row, col, self.screen)
                       for col in range(self.board_cols)]
                      for row in range(self.board_rows)]

    def draw(self):
        # width and height of the board
        WIDTH_BOARD = 9 * CELL_SIZE
        HEIGHT_BOARD = 9 * CELL_SIZE

        # starting position
        board_x_start = (WIDTH - WIDTH_BOARD) // 2
        board_y_start = (HEIGHT - HEIGHT_BOARD) // 2 - 70  # move board up 70 px

        # Draw the cells
        for row in self.cells:
            for cell in row:
                cell_rect = pygame.Rect(board_x_start + cell.col * CELL_SIZE, board_y_start + cell.row * CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, SCREEN_COLOR, cell_rect)
                cell.draw(self.screen)

        # Draw the squares for the board
        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_x_start, board_x_start + (3 * i) * CELL_SIZE),
                             (board_x_start + WIDTH_BOARD, board_y_start + (3 * i) * CELL_SIZE),
                             BOARD_LINE_WIDTH)

        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_x_start + (3 * i) * CELL_SIZE, board_x_start),
                             (board_x_start + (3 * i) * CELL_SIZE, board_y_start + HEIGHT_BOARD),
                             BOARD_LINE_WIDTH)

    # Marks the cell at (row, col) in the board as the current selected cell
    def select(self, row, col):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if i == row and j == col:
                    self.cells[i][j].selected = True
                else:
                    self.cells[i][j].selected = False

    # returns a tuple of the (row, col) of the cell which was clicked
    def click(self, x, y):
        # width and height of the board
        WIDTH_BOARD = 9 * CELL_SIZE
        HEIGHT_BOARD = 9 * CELL_SIZE

        # starting position
        board_x_start = (WIDTH - WIDTH_BOARD) // 2
        board_y_start = (HEIGHT - HEIGHT_BOARD) // 2 - 70  # move board up 70 px

        # if coordinates inside the board (which calculated by adding board's width and height to the starting points)
        if board_x_start <= x < board_x_start + WIDTH_BOARD and board_y_start <= y < board_y_start + BOARD_HEIGHT:
            clicked_row = (y - board_y_start) // CELL_SIZE
            clicked_col = (x - board_x_start) // CELL_SIZE
            return clicked_row, clicked_col

        return None

    # allows user to remove the cell values and sketched value that are filled by themselves
    def clear(self):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if self.cells[i][j].selected:
                    # check if the cell is empty
                    if self.board[i][j] == 0:
                        self.cells[i][j].sketched_value = 0
                        self.cells[i][j].value = 0

    # if cell is selected and value is currently 0, set sketched value to value
    def sketch(self, value):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].selected:
                    if self.board[col][row] == 0:
                        self.cells[col][row].set_sketched_value(value)
def place_number(self, value):
    # Iterate through each cell in the board
    for row in range(self.board_rows):
        for col in range(self.board_cols):
            # Check if the cell is selected and the corresponding board value is 0
            if self.cells[col][row].selected and self.board[col][row] == 0:
                # Update the cell's sketched value and set the cell value
                self.cells[col][row].sketched_value = 0
                self.cells[col][row].set_cell_value(value)

# Reset cells in the board to their original values and clear sketched values
def reset_to_original(self):
    # Iterate through each cell in the board
    for row in range(self.board_rows):
        for col in range(self.board_cols):
            # Retrieve the current cell
            cell = self.cells[row][col]
            # Reset the cell's value to its original value and clear sketched value
            cell.value, cell.sketched_value = self.original[row][col], 0

# Check if the board is full by examining each cell
# Return False if any cell value is 0, otherwise, return True (indicating a full board)
def is_full(self):
    # Use the all() function to check if all cell values are non-zero
    return all(cell.value != 0 for row in self.cells for cell in row)

# Update each cell's value to its sketched value
def update_board(self):
    # Iterate through each cell in the board
    for row in range(self.board_rows):
        for col in range(self.board_cols):
            # Retrieve the current cell
            cell = self.cells[col][row]
            # Update the cell's value to its sketched value if it is not 0
            if cell.sketched_value != 0:
                cell.value = cell.sketched_value

# Find the first empty cell (cell with value 0 and sketched value 0) and return its coordinates
def find_empty(self):
    # Iterate through each cell in the board
    for row in range(self.board_rows):
        for col in range(self.board_cols):
            # Retrieve the current cell
            cell = self.cells[col][row]
            # Check if the cell is empty (value is 0 and sketched value is 0)
            if cell.value == 0 and cell.sketched_value == 0:
                return col, row

# Check if the current board configuration is valid by examining each cell
# Return True if the board is correctly solved, otherwise, return False
def check_board(self):
    # Iterate through each cell in the board
    for row in range(self.board_rows):
        for col in range(self.board_cols):
            # Retrieve the current cell and its value
            num = self.cells[col][row].value
            # Check if the value in the cell is valid in its column, row, and box
            if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row, col, num):
                return True
    # If no conflicts are found, return False indicating an incorrect solution
    return False

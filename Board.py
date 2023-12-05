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

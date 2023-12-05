import math,random

class SudokuGenerator:

    # Initialize SudokuGenerator
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [["-" for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(math.sqrt(self.row_length))

    # Returns a 2D python list of numbers which represents the board
    def get_board(self):
        return self.board

    # Displays the board to the console
    def print_board(self):
        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                print(self.board[i][j], end=" ")
            print()

    # Determines if num is contained in the specified row (horizontal) of the board
    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # Determines if num is contained in the specified column (vertical) of the board
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    # Determines if num is contained in the 3x3 box specified on the board
    def valid_in_box(self, row_start, col_start, num):
        box_row = row_start - row_start % int(math.sqrt(self.row_length))
        box_col = col_start - col_start % int(math.sqrt(self.row_length))
        for i in range(box_row, box_row + int(math.sqrt(self.row_length))):
            for j in range(box_col, box_col + int(math.sqrt(self.row_length))):
                if self.board[i][j] == num:
                    return False
        return True

    # Checks if a given function is valid
    # Returns true if valid_in_col, valid_in_row and valid_in_box return true
    def is_valid(self, row, col, num):
        if self.valid_in_col(col, num) and self.valid_in_row(row, num) and self.valid_in_box(row, col, num):
            return True
        else:
            return False

    # Fills the specified 3x3 box with values with random numbers that haven't been used yet
    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                num = random.choice(nums)
                while not self.is_valid(i, j, num):
                    num = random.choice(nums)
                self.board[i][j] = num
                nums.remove(num)
        return self.board

    # Fills the boxes which start at (0,0), (3,3), and (6,6) with random numbers that haven't been used yet
    def fill_diagonal(self):
        boxes = [0, 3, 6]
        for box in boxes:
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(box, box + 3):
                for j in range(box, box + 3):
                    num = random.choice(nums)
                    while not self.is_valid(i, j, num):
                        num = random.choice(nums)
                    self.board[i][j] = num
                    nums.remove(num)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # calls diagonal and remaining to construct
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self, removed_cell):
        # generates a random coordinate on the board and resets its value to 0
        # Removes appropriate cells from board
        removed = set()
        # empty set to store coordinates of removed cells

        while len(removed) < removed_cell:
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            if (row, column) not in removed and self[row][column]:
                self[row][column] = 0
                removed.add((row, column))
        return self


# Simply calls all the necessary functions to generate the game
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


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
    # If no conflicts are found, return False indicating an incorrect solution.
    return False

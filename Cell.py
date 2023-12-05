import pygame

WIDTH = 750
HEIGHT = 900
BOARD_ROWS = 4
BOARD_COLS = 3
BOARD_LINE_WIDTH = 5
CELL_LINE_WIDTH = 1
CELLS_IN_SQUARE = 3
NUMBER_FONT = 100
USER_NUMBER_COLOR = (105, 105, 105)
NUMBER_COLOR = (0, 0, 0)
MESSAGE_FONT = 50
CELL_SIZE = 82
RED = (255, 0, 0)
WHITE = (240, 248, 255)
BG_COLOR = (224, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (25, 25, 112)
DODGER_BLUE = (0, 90, 156)
SCREEN_COLOR = (173, 216, 230)
BLACK = (0, 0, 0)



class Cell:
    def __init__(self, value, row, column, screen):
        self.value = value
        self.row = row
        self.column = column
        self.screen = screen
        self.select = False
        self.sketched_value = 0
    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value

    def draw(self, screen):
        #width and height of board with help of above constants
        board_width = 9 * CELL_SIZE
        board_height = 9 * CELL_SIZE

        Xboard_start = (WIDTH - board_width) // 2
        Yboard_start = (HEIGHT - board_width) // 2 - 70

        # draws the rectangle
        cell_rectangle = pygame.Rect(Xboard_start + self.column * CELL_SIZE, Yboard_start + self.row * CELL_SIZE,CELL_SIZE,CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen, BLACK, cell_rectangle, CELL_LINE_WIDTH)

        if self.selected: # will draw the border thicker
            pygame.draw.rect(screen, BLUE, cell_rectangle, 6)

        if self.value != 0 and self.sketched_value == 0: #Draws cell value
            cell_font = pygame.font.FONT(None, 55)
            cell_surf = cell_font.render (str(self.value), True, BLACK)
            cell_rectangle = cell_surf.get_rect(center = (Xboard_start + self.column *CELL_SIZE + CELL_SIZE // 2,
                                                     Yboard_start + self.row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(cell_surf, cell_rectangle)

        if self.sketched_value != 0: # Draws calue based upon user input
            cell_font = pygame.font.Font(None, 50)
            cell_surf = cell_font.render(str(self.sketched_value), True, USER_NUMBER_COLOR)

            cell_rectangle = cell_surf.get_rect(center = ((Xboard_start + self.column * CELL_SIZE + CELL_SIZE // 2 )-12, (Yboard_start + self.row * CELL_SIZE + CELL_SIZE // 2) - 12 ))
            screen.blit(cell_surf, cell_rectangle)
import numpy as np
import pygame.draw

from settings import SQUARE_HEIGHT, SQUARE_WIDTH, SIZE, BROWN, OFFSET


class Board:
    def __init__(self):
        self.number_of_empty_places = 9
        self.board = np.zeros((3,3), dtype=int)

    def is_end(self):
        if self.number_of_empty_places == 0:
            return True

    def set_mark(self, row, column, mark):
        self.board[row][column] = mark

    def draw_board(self, win):
        for row in range(SIZE):
            y_offset = OFFSET * row
            for column in range(SIZE):
                x_offset = OFFSET * column
                pygame.draw.rect(win, BROWN,(row*SQUARE_WIDTH + y_offset, column*SQUARE_WIDTH + x_offset, SQUARE_WIDTH, SQUARE_HEIGHT))

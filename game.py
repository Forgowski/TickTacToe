from board import Board
import pygame


class Game:
    def __init__(self, win):
        self.board = Board()
        self.turn = 1
        self.play()
        self.end = False
        self.win = win

    def play(self):
        pass

    def update(self):
        self.board.draw_board(self.win)
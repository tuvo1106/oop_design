#!/usr/bin/env python3

from chess.box.box import Box
from chess.piece.knight import Knight, Pawn, Bishop, Rook


class Board:
    def __init__(self):
        self.__boxes = [[]]

    def Board(self):
        self.reset_board()

    def get_box(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            raise Exception("Index out of bound")
        return self.__boxes[x][y]

    def reset_board(self):
        # initialize white pieces
        self.__boxes[0][0] = Box(0, 0, Rook(True))
        self.__boxes[0][1] = Box(0, 1, Knight(True))
        self.__boxes[0][2] = Box(0, 2, Bishop(True))
        # ...
        self.__boxes[1][0] = Box(1, 0, Pawn(True))
        self.__boxes[1][1] = Box(1, 1, Pawn(True))
        # ...
        # initialize black pieces
        self.__boxes[7][0] = Box(7, 0, Rook(False))
        self.__boxes[7][1] = Box(7, 1, Knight(False))
        self.__boxes[7][2] = Box(7, 2, Bishop(False))
        # ...
        self.__boxes[6][0] = Box(6, 0, Pawn(False))
        self.__boxes[6][1] = Box(6, 1, Pawn(False))
        # ...
        # initialize remaining boxes without any piece
        for i in range(2, 6):
            for j in range(0, 8):
                self.__boxes[i][j] = Box(i, j, None)

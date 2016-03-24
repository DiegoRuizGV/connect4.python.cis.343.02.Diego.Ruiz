import Token


class Board:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.boardarray = [[Token for x in range(width)] for x in range(height)]

    def __str__(self):
        board = ""
        for x in range(0, self.w):
            board += str(x) + '  '
        board += '\n'
        for x in range(0, self.h):
            for y in range(0, self.w):
                board += str(self.boardarray[y][x]) + '  '
                if y == self.w - 1:
                    board += '\n'
        return board

    def initialize_board(self):
        for x in range(0, self.w):
            for y in range(0, self.h):
                self.boardarray[x][y] = "*"

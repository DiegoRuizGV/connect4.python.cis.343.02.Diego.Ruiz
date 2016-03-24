import Board
import random
import Player
import Token
import sys


class Game:

    def __init__(self, width, height, winl):
        self.gameboard = Board.Board(width, height)
        self.winl = winl
        self.player1 = Player.Player(1)
        self.player2 = Player.Player(2)
        if random.randint(1, 2) == 1:
            self.currentplayer = self.player1
        else:
            self.currentplayer = self.player2
        self.gameboard.initialize_board()

    #returns 0 if no token could be placed, or the coordinates of the last token that was placed in
    #the form of (x, y)
    def place_token(self, column):
        try:
            if isinstance(self.gameboard.boardarray[column][0], Token.Token):
                print "cant place token here, column is full"
                return 0
            else:
                for x in range(1, self.gameboard.h):
                    if isinstance(self.gameboard.boardarray[column][x], Token.Token):
                        self.gameboard.boardarray[column][x-1] = Token.Token(self.currentplayer)
                        print 'placed token on top of other'
                        return column, x - 1
                self.gameboard.boardarray[column][self.gameboard.h - 1] = Token.Token(self.currentplayer)
                print 'placed lone token'
                return column, self.gameboard.h - 1
        except TypeError:
            print "bad reference passed during the place token function"
            sys.exit(0)

    def check_for_win(self, x, y, winlength, lastplayer):
        if self.horizontal_win(y, winlength, lastplayer) != 0:
            return self.horizontal_win(y, winlength, lastplayer)
        elif self.vertical_win(x, winlength, lastplayer) != 0:
            return self.vertical_win(x, winlength, lastplayer)
        elif self.diagonal_win(x, y, winlength, lastplayer) != 0:
            return self.diagonal_win(x, y, winlength, lastplayer)
        else:
            return 0

    def horizontal_win(self, y, winlength, lastplayer):
        inarow = 0
        for a in range(0, self.gameboard.w - 1):
            if isinstance(self.gameboard.boardarray[a][y], Token.Token):
                if self.gameboard.boardarray[a][y].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
            else:
                inarow = 0
            if inarow == winlength:
                return lastplayer.playernumber
        return 0

    def vertical_win(self, x, winlength, lastplayer):
        inarow = 0
        for a in range(0, self.gameboard.h - 1):
            if isinstance(self.gameboard.boardarray[x][a], Token.Token):
                if self.gameboard.boardarray[x][a].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
            else:
                inarow = 0
            if inarow == winlength:
                return lastplayer.playernumber
        return 0

    def diagonal_win(self, x, y, winlength, lastplayer):
        inarow = 1
        a = x
        s = y
        while a >= 0 and s >= 0:
            a -= 1
            s -= 1
            if isinstance(self.gameboard.boardarray[a][s], Token.Token):
                if self.gameboard.boardarray[a][s].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
                if inarow == winlength:
                    return lastplayer.playernumber
            else:
                break
        a = x
        s = y
        while a < self.gameboard.w - 1 and s < self.gameboard.h - 1:
            a += 1
            s += 1
            if isinstance(self.gameboard.boardarray[a][s], Token.Token):
                if self.gameboard.boardarray[a][s].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
                if inarow == winlength:
                    return lastplayer.playernumber
            else:
                inarow = 1
                break
        a = x
        s = y
        while a >= 0 and s < self.gameboard.h - 1:
            a -= 1
            s += 1
            if isinstance(self.gameboard.boardarray[a][s], Token.Token):
                if self.gameboard.boardarray[a][s].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
                if inarow == winlength:
                    return lastplayer.playernumber
            else:
                break
        a = x
        s = y
        while a < self.gameboard.w - 1 and s >= 0:
            a += 1
            s -= 1
            if isinstance(self.gameboard.boardarray[a][s], Token.Token):
                if self.gameboard.boardarray[a][s].owner.playernumber == lastplayer.playernumber:
                    inarow += 1
                if inarow == winlength:
                    return lastplayer.playernumber
            else:
                break
        return 0
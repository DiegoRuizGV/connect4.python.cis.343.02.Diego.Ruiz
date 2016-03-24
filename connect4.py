import getopt
import sys
from game_components import Game
import pickle


def main(argv):
    boardheight = 7
    boardwidth = 7
    winlength = 4
    usage = 'connect4.py -w <board_width> -h <board_height> -l <win_length>'
    try:
        opts, args = getopt.getopt(argv, 'w:h:l:', ['width=', 'height=', 'winLength=', 'help'])
    except getopt.GetoptError:
        print usage
        sys.exit(0)
    for opt, arg in opts:
        if opt in ('-w', '--width'):
            boardwidth = int(arg)
        elif opt in ("-h", "--height"):
            boardheight = int(arg)
        elif opt in ("-l", "--winLength"):
            winlength = int(arg)
    if (boardwidth or boardheight) < 3 and winlength > (boardheight or boardwidth):
        print 'The boards width and height must both be greater than or equal to 3,\n' \
              'and the length needed to win must not exceed either the height or width of the board'
        sys.exit(0)

    currentgame = Game.Game(boardwidth, boardheight, winlength)
    turn = 0

    print "Welcome to Connect 4! you may enter the following \ncommands with dash instead of a column number \n"
    print "-exit -- will exit the game without saving"
    print "-save <filename> -- will save your current game to filename"
    print "-load <filename> -- will load previously saved game \n"
    startgame = raw_input("would you like to start a new game or\nload a previous game? \nplease enter yes or a filename: ")
    if startgame != 'yes':
        try:
            currentgame = pickle.load(open( startgame+'.p', "rb" ))
        except pickle.PicklingError:
            print 'error loading game, try again'
            sys.exit(0)

    while True:
        print currentgame.gameboard
        print str(currentgame.currentplayer) + ' please select a column to drop your next token: '
        nextcol = raw_input()
        if nextcol[0] == '-':
            if nextcol[1:5] == 'exit':
                sys.exit(0)
            elif nextcol[1:5] == 'save':
                try:
                    pickle.dump(currentgame, open(nextcol[6:]+'.p', "wb"))
                    print 'save successful'
                    continue
                except pickle.PicklingError:
                    print 'error when saving, try again'
                    continue
            elif nextcol[1:5] == 'load':
                try:
                    currentgame = pickle.load(open(nextcol[6:]+'.p', "rb"))
                    print 'load successful'
                    continue
                except pickle.PicklingError:
                    print 'error loading game, try again'
                    continue
            else:
                print 'invalid input, try again'
                continue
        else:
            try:
                nextcol = int(nextcol)
                if nextcol > boardwidth - 1 or nextcol < 0:
                    print 'Im sorry but the column number you have entered is out of range.'
                    continue
            except ValueError:
                print 'invalid input'
                continue

        lastspace = currentgame.place_token(nextcol)
        if lastspace == 0:
            continue
        else:
            turn += 1
            winner = currentgame.check_for_win(lastspace[0], lastspace[1],winlength,currentgame.currentplayer)
            if winner != 0:
                print str(currentgame.currentplayer) + ' congratulations, you got ' + str(winlength) + ' in a row!!'
                print currentgame.gameboard
                sys.exit(0)
            else:
                if currentgame.currentplayer == currentgame.player1:
                    currentgame.currentplayer = currentgame.player2
                else:
                    currentgame.currentplayer = currentgame.player1
            if turn >= boardheight * boardwidth:
                print 'No more spaces for tokens, Looks like its a tie!!'
                print currentgame.gameboard
                sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])

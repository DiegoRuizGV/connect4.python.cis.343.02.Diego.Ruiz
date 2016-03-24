class Player:
    def __init__(self, playernumber):
        self.playernumber = playernumber

    def __str__(self):
        return 'Player ' + str(self.playernumber)
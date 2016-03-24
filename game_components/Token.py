class Token:

    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        try:
            if self.owner.playernumber == 1:
                return "X"
            else:
                return "O"
        except TypeError:
            print "Token is not receiving a valid Player object reference"

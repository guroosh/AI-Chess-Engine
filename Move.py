class Move(object):
    def __init__(self, coded_move):
        self.coded = coded_move

    def isValidInput(self):
        x1 = self.coded[0]
        y1 = self.coded[1]
        x2 = self.coded[2]
        y2 = self.coded[3]
        if not(65 <= ord(x1) <= 72 or 97 <= ord(x1) <= 104):
            return False
        if not(65 <= ord(x2) <= 72 or 97 <= ord(x2) <= 104):
            return False
        if not(1 <= int(y1) <= 8):
            return False
        if not(1 <= int(y2) <= 8):
            return False
        return True

    def isValidRule(self, board):
        x1 = self.coded[0]
        y1 = self.coded[1]
        x2 = self.coded[2]
        y2 = self.coded[3]
        x1 = ord(x1)
        y1 = int(y1)
        x2 = ord(x2)
        y2 = int(y2)
        x1 = x1 - 65
        y1 = 8 - y1
        x2 = x2 - 65
        y2 = 8 - y2
        piece = board.getPiece(y1, x1)
        return True


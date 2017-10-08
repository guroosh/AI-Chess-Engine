from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class Move(object):
    def __init__(self, coded_move):
        self.coded = coded_move

    def isValidInput(self):
        x1 = self.coded[0]
        y1 = self.coded[1]
        x2 = self.coded[2]
        y2 = self.coded[3]

        x1 = x1.upper()
        x2 = x2.upper()
        try:
            y1 = int(y1)
            y2 = int(y2)
        except ValueError:
            return False

        if not (65 <= ord(x1) <= 72):
            return False
        if not (65 <= ord(x2) <= 72):
            return False
        if not (1 <= y1 <= 8):
            return False
        if not (1 <= y2 <= 8):
            return False
        return True

    def isValidRule(self, board, turn):
        x1 = self.coded[0]
        y1 = self.coded[1]
        x2 = self.coded[2]
        y2 = self.coded[3]
        x1 = x1.upper()
        x2 = x2.upper()
        x1 = ord(x1)
        y1 = int(y1)
        x2 = ord(x2)
        y2 = int(y2)
        x1 = x1 - 65
        y1 = 8 - y1
        x2 = x2 - 65
        y2 = 8 - y2
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        this_piece = board.getPieceObject(x1, y1)
        piece_name = this_piece.name
        if (turn is 'BLACK' and piece_name[0] is 'W') or (turn is 'WHITE' and piece_name[0] is 'B'):
            print('Not your turn')
            return False
        if piece_name == 'Wknight' or piece_name == 'Bknight':
            piece = this_piece
        elif piece_name == 'Brook' or piece_name == 'Wrook':
            piece = this_piece
        elif piece_name == 'Wking' or piece_name == 'Bking':
            piece = this_piece
        elif piece_name == 'Wqueen' or piece_name == 'Bqueen':
            piece = this_piece
        elif piece_name == 'Wbishop' or piece_name == 'Bbishop':
            piece = this_piece
        elif piece_name == 'Wpawn' or piece_name == 'Bpawn':
            piece = this_piece
        else:
            print('No piece selected')
            return False
        # print(piece_name)
        if piece.isValid(board, x1, y1, x2, y2):
            return True
        return False

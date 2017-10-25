def encoded(x1, y1, x2, y2):
    if not(0 <= x1 <= 7 and 0 <= x2 <= 7 and 0 <= y1 <= 7 and 0 <= y2 <= 7):
        return 'outside'
    y1 = y1 + 65
    ret_val = chr(y1)
    x1 = 8 - x1
    ret_val += str(x1)
    y2 = y2 + 65
    ret_val += chr(y2)
    x2 = 8 - x2
    ret_val += str(x2)
    return ret_val


class Piece:
    def __init__(self, name, moved):
        self.name = name
        self.moved = moved
        # self.available = available
        # self.x = x
        # self.y = y

    # for BLACK theme
    def unicode(self):
        if self.name == 'Wrook':
            return u'\u265c'
        elif self.name == 'Wknight':
            return u'\u265e'
        elif self.name == 'Wbishop':
            return u'\u265d'
        elif self.name == 'Wking':
            return u'\u265a'
        elif self.name == 'Wqueen':
            return u'\u265b'
        elif self.name == 'Wpawn':
            return u'\u265f'
        elif self.name == 'Brook':
            return u'\u2656'
        elif self.name == 'Bknight':
            return u'\u2658'
        elif self.name == 'Bbishop':
            return u'\u2657'
        elif self.name == 'Bking':
            return u'\u2654'
        elif self.name == 'Bqueen':
            return u'\u2655'
        elif self.name == 'Bpawn':
            return u'\u2659'

    # for WHITE theme
    # def unicode(self):
    #     if self.name == 'Brook':
    #         return u'\u265c'
    #     elif self.name == 'Bknight':
    #         return u'\u265e'
    #     elif self.name == 'Bbishop':
    #         return u'\u265d'
    #     elif self.name == 'Bking':
    #         return u'\u265a'
    #     elif self.name == 'Bqueen':
    #         return u'\u265b'
    #     elif self.name == 'Bpawn':
    #         return u'\u265f'
    #     elif self.name == 'Wrook':
    #         return u'\u2656'
    #     elif self.name == 'Wknight':
    #         return u'\u2658'
    #     elif self.name == 'Wbishop':
    #         return u'\u2657'
    #     elif self.name == 'Wking':
    #         return u'\u2654'
    #     elif self.name == 'Wqueen':
    #         return u'\u2655'
    #     elif self.name == 'Wpawn':
    #         return u'\u2659'

    def isValid(self, board, fromX, fromY, toX, toY):
        if toX == fromX and toY == fromY:
            return False  # connot move anything
        if toX < 0 or toX > 7 or fromX < 0 or fromX > 7 or toY < 0 or toY > 7 or fromY < 0 or fromY > 7:
            return False
        return True

    def getAllPossibleMoves(self, board, i, j):
        color = self.name[0]
        name = self.name[1:]
        if name == 'rook':
            from Rook import Rook
            piece = Rook(name, False)
        elif name == 'knight':
            from Knight import Knight
            piece = Knight(name, False)
        elif name == 'king':
            from King import King
            piece = King(name, False)
        elif name == 'queen':
            from Queen import Queen
            piece = Queen(name, False)
        elif name == 'bishop':
            from Bishop import Bishop
            piece = Bishop(name, False)
        elif name == 'pawn':
            from Pawn import Pawn
            piece = Pawn(name, False)
        else:
            return []
        piece_moves = piece.getPossibleMoves(board, color, i, j)
        return piece_moves

# done


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

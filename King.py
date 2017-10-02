from Piece import Piece


class King(Piece):
    def __init__(self, available, x, y):
        super().__init__(available, x, y)
        self.first_move=True

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if toX != fromX - 1 and toX != fromX + 1 and toX != fromX + 2 and toX != fromX - 2:
            return False
        if toY != fromY - 2 and toY != fromY + 2 and toY != fromY - 1 and toY != fromY + 1:
            return False
        #enter castling constraints

        self.first_move=False
        return True

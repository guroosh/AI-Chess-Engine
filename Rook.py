from Piece import Piece


class Rook(Piece):
    def __init__(self, available, x, y):
        super().__init__(available, x, y)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if toX == fromX:
            return True
        if toY == fromY:
            return True

        return False
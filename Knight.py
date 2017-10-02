from Piece import Piece


class Knight(Piece):
    def __init__(self, available, x, y):
        super().__init__(available, x, y)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if abs(toX - fromX) == 2:
            if abs(toY - fromY) is not 1:
                return False
            else:
                return True
        elif abs(toX - fromX) == 1:
            if abs(toY - fromY) is not 2:
                return False
            else:
                return True
        else:
            return False

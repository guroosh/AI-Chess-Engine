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

    def isPathAllowed(self,board,fromX,fromY,toX,toY):
        if toY==fromY:
            move=toX-fromX/abs(fromX-toX) #+1/-1
            while(fromX!=toX+move):
                fromX += move
                if(board.isSpotVacant(fromX,fromY)==False):
                    return False
            return True
        if toX==fromX:
            move=toY-fromY/abs(toY-fromY)
            while(fromY!=toY+move):
                fromY+=move
                if (board.isSpotVacant(fromX, fromY) == False):
                    return False
            return True



from Piece import Piece


class Rook(Piece):
    def __init__(self, name):
        super().__init__( name)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if toX == fromX or toY == fromY:
            return self.isPathAllowed(board,fromX,fromY,toX,toY)

        return False

    def isPathAllowed(self,board,fromX,fromY,toX,toY):
        print(fromX,fromY,toX,toY)
        if toY==fromY:
            move=int((toX-fromX)/abs(fromX-toX)) #+1/-1
            while(fromX!=toX):
                fromX += move
                if(board.isSpotVacant(fromX,fromY)==False):
                    return False
            return True
        if toX==fromX:
            move=int((toY-fromY)/abs(toY-fromY))
            while(fromY!=toY):
                fromY+=move
                if (board.isSpotVacant(fromX, fromY) == False):
                    return False
            return True



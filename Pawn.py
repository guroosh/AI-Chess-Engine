from Piece import Piece


class Pawn(Piece):
    def __init__(self, name):
        super().__init__(name)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False
        return True
        if toY!=fromY and toY!=fromY +1 and toY!=fromY-1:
            return False

        #Assumption: Black King is on x0 and White King is on x7
        if( self.name[0] is 'W'):
            if toX >= fromX:
                return False
            if fromX is 6:
                if toX<fromX-2:
                  return False
            else:
                if toX<fromX-1:
                    return False

        elif(self.name[0] is 'B'):
            if toX <= fromX:
                return False
            if fromX is 1:
                if toX>fromX+2:
                    return False
            else:
                if toX>fromX+1:
                    return False

        return True

    def isPathAllowed(self,board,fromX,fromY,toX,toY):
        return False

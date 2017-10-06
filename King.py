from Piece import Piece


class King(Piece):
    def __init__(self, available, x, y):
        super().__init__(available, x, y)
        self.first_move=True
        self.isChecked=False

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

    def isPathAllowed(self,board,fromX,fromY,toX,toY):
        source = board.getPiece(fromX, fromY)[0]
        dest = board.getPiece(toX, toY)[0]
        if (fromY==toY and (fromX==toX+1 or fromX==toX-1)) or (fromX==toX and (fromY==toY+1 or fromY==toY-1)):  #single step moves
            if source=='W' and dest=='B' or source=='B' and dest=='W':
                return True
            elif dest=='.':
                return True
            else:
                return False

        if (self.first_move==True and (fromY==toY and (fromX==toX+2 or fromX==toX-2))) and self.isChecked==False: #castling
            return False #TODO Castling


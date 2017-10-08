from Piece import Piece


class King(Piece):
    def __init__(self, name):
        super().__init__(name)
        self.first_move = True

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if toX == fromX - 1 or toX == fromX + 1:
            if fromY - 1 <= toY <= fromY + 1:
                return self.isPathAllowed(board, fromX, fromY, toX, toY)

        if toY == fromY - 1 or toY == fromY + 1:
            if fromX - 1 <= toX <= fromX + 1:
                return self.isPathAllowed(board, fromX, fromY, toX, toY)

    def isPathAllowed(self, board, fromX, fromY, toX, toY):
        source = board.getPiece(fromX, fromY)[0]
        dest = board.getPiece(toX, toY)[0]

        if board.isChecked(source, toX, toY):
            print('Check on destination')
            return False

        if (source == 'W' and dest == 'B') or (source == 'B' and dest == 'W'):
            return True
        elif dest == '.':
            return True
        else:
            return False

        # if (self.first_move==True and (fromY==toY and (fromX==toX+2 or fromX==toX-2))) and self.isChecked==False: #castling
        #     return False #TODO Castling


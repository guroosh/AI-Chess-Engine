from Piece import Piece


class Rook(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)
        self.moved = moved

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False
        print('super:', self.moved)
        if toX == fromX or toY == fromY:
            return self.isPathAllowed(board, fromX, fromY, toX, toY)

        return False

    def isPathAllowed(self, board, fromX, fromY, toX, toY):
        if toY == fromY:
            move = int((toX - fromX) / abs(fromX - toX))  # +1/-1
            fromx=fromX
            while fromx+move != toX:
                fromx += move
                if not board.isSpotVacant(fromx, fromY):
                    return False
            if not board.isSpotVacant(toX, toY):
                if board.isSpotOfSameTeam(fromX,fromY,toX,toY):
                    return False
                return True
            return True
        if toX == fromX:
            move = int((toY - fromY) / abs(toY - fromY))
            fromy=fromY
            while fromy+move != toY:
                fromy += move
                if not board.isSpotVacant(fromX, fromy):
                    return False
            if not board.isSpotVacant(toX, toY):
                if board.isSpotOfSameTeam(fromX, fromY, toX, toY):
                    return False
                return True
            return True

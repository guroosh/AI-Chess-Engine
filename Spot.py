#done
from Piece import Piece


class Spot(object):
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = Piece(piece)

    def occupySpot(self, piece):
        if self.piece is not None:
            self.piece.setAvailable(False)
        self.piece = piece

    def isOccupied(self):
        if self.piece is not None:
            return True
        return False

    def releaseSpot(self):
        releasedPiece = self.piece
        self.piece = None
        return releasedPiece

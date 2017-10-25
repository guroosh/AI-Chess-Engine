from Piece import Piece, encoded
from Global import Global

class King(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)
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

        if abs(toY - fromY) == 2:
            if self.castlingPermitted(board, fromX, fromY, toX, toY):
                # move rook
                Global.doesCastle = True
                return True
            return False

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

    def castlingPermitted(self, board, fromX, fromY, toX, toY):
        if fromX != toX:
            return False

        king = board.getPiece(fromX, fromY)
        if toY == 6:  # check for right rook
            if king.name[0] == "W":
                rook = board.getPiece(7, 7)
            else:
                rook = board.getPiece(0, 7)
            pos = 7

        elif toY == 2:  # check for left rook
            if king.name[0] == "W":
                rook = board.getPiece(7, 0)
            else:
                rook = board.getPiece(0, 0)
            pos = 0
        else:
            return False

        if king.name[1:] != "king" or rook.name[1:] != "rook":
            return False
        if king.moved or rook.moved:
            return False

        color = king.name[0]
        move = int((toY - fromY) / abs(toY - fromY))
        fromy = fromY
        while fromY != toY:
            if board.isChecked(color, fromX, fromY):
                return False
            fromY += move
        fromY = fromy

        while fromY + move != pos:
            if not board.isSpotVacant(fromX, fromY):
                return False
            fromY += move

        return True

    def getPossibleMoves(self, board, color, i, j):
        ret_list = []
        physical_moves = []

        move = encoded(i, j, i - 1, j)
        physical_moves.append(move)
        move = encoded(i, j, i + 1, j)
        physical_moves.append(move)
        move = encoded(i, j, i, j + 1)
        physical_moves.append(move)
        move = encoded(i, j, i, j - 1)
        physical_moves.append(move)
        move = encoded(i, j, i - 1, j - 1)
        physical_moves.append(move)
        move = encoded(i, j, i - 1, j + 1)
        physical_moves.append(move)
        move = encoded(i, j, i + 1, j - 1)
        physical_moves.append(move)
        move = encoded(i, j, i + 1, j + 1)
        physical_moves.append(move)

        if color == 'B':
            turn = 'BLACK'
        else:
            turn = 'WHITE'
        for m in physical_moves:
            from Move import Move
            move = Move(m)
            if move.isValidRule(board, turn):
                ret_list.append(move.coded)
        return ret_list
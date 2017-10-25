from Piece import Piece, encoded


class Pawn(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if toY != fromY and toY != fromY + 1 and toY != fromY - 1:
            return False

        # Assumption: Black King is on x0 and White King is on x7
        if self.name[0] is 'W':
            if toX >= fromX:
                return False
            if fromX is 6:  # first move 2 steps allowed
                if toX < fromX - 2:
                    return False
            else:
                if toX < fromX - 1:
                    return False

        elif self.name[0] is 'B':
            if toX <= fromX:
                return False
            if fromX is 1:  # first move 2 steps allowed
                if toX > fromX + 2:
                    return False
            else:
                if toX > fromX + 1:
                    return False

        return self.isPathAllowed(board, fromX, fromY, toX, toY)

    def isPathAllowed(self, board, fromX, fromY, toX, toY):
        move = int((toX - fromX) / abs(fromX - toX))
        if fromY == toY:  # straight move
            while fromX != toX:
                fromX += move
                if not board.isSpotVacant(fromX, fromY):
                    return False
            return True
        else:
            if board.isSpotVacant(toX, toY) or board.isSpotOfSameTeam(fromX, fromY, toX, toY):
                return False
            return True

    def getPossibleMoves(self, board, color, i, j):
        physical_moves = []
        ret_list = []
        if color == 'W':
            if i == 6:
                move = encoded(i, j, i - 1, j)
                physical_moves.append(move)
                move = encoded(i, j, i - 2, j)
                physical_moves.append(move)
            else:
                move = encoded(i, j, i - 1, j)
                physical_moves.append(move)
            move = encoded(i, j, i - 1, j - 1)
            physical_moves.append(move)
            move = encoded(i, j, i - 1, j + 1)
            physical_moves.append(move)
        else:
            if i == 1:
                move = encoded(i, j, i + 1, j)
                physical_moves.append(move)
                move = encoded(i, j, i + 2, j)
                physical_moves.append(move)
            else:
                move = encoded(i, j, i + 1, j)
                physical_moves.append(move)
            move = encoded(i, j, i + 1, j - 1)
            physical_moves.append(move)
            move = encoded(i, j, i + 1 , j + 1)
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

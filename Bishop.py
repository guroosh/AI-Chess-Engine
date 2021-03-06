from Piece import Piece, encoded


def isPathObstructed(board, fromX, fromY, toX, toY):
    goRight = False
    goBelow = False
    path_len = abs(toX - fromX) - 1

    if fromX < toX:
        goBelow = True
    if fromY < toY:
        goRight = True

    if goBelow and goRight:
        for j in range(path_len):
            i = j + 1
            if not board.isSpotVacant(fromX + i, fromY + i):
                return True
        return False
    elif goBelow and not goRight:
        for j in range(path_len):
            i = j + 1
            if not board.isSpotVacant(fromX + i, fromY - i):
                return True
        return False
    elif not goBelow and goRight:
        for j in range(path_len):
            i = j + 1
            if not board.isSpotVacant(fromX - i, fromY + i):
                return True
        return False
    else:
        for j in range(path_len):
            i = j + 1
            if not board.isSpotVacant(fromX - i, fromY - i):
                return True
        return False


def isDestinationEmpty(board, fromX, fromY, toX, toY):
    piece_name = board.getPiece(fromX, fromY)
    piece_name1 = board.getPiece(toX, toY)
    if piece_name1[0] == '.':
        return True
    if piece_name[0] is not piece_name1[0]:
        return True
    return False


class Bishop(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False
        if abs(fromX - toX) == abs(fromY - toY):
            if (not isPathObstructed(board, fromX, fromY, toX, toY)) and isDestinationEmpty(board, fromX, fromY, toX,
                                                                                            toY):
                return True
        return False


    def getPossibleMoves(self, board, color, i, j):
        ret_list = []
        physical_moves = []
        for k in [1, 2, 3, 4, 5, 6, 7]:
            move = encoded(i, j, i - k, j - k)
            physical_moves.append(move)
            move = encoded(i, j, i + k, j + k)
            physical_moves.append(move)
            move = encoded(i, j, i - k, j + k)
            physical_moves.append(move)
            move = encoded(i, j, i + k, j - k)
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

from Piece import Piece


def isPathObstructed(board, fromX, fromY, toX, toY):
    goRight = False
    goBelow = False
    path_len = abs(toX - fromX - 1)

    if fromX < toX:
        goBelow = True
    if fromY < toY:
        goRight = True

    if goBelow and goRight:
        for j in range(path_len):
            i = j + 1
            if board.isSpotVacant(fromX + i, fromY + i):
                return False
        return True
    elif goBelow and not goRight:
        for j in range(path_len):
            i = j + 1
            if board.isSpotVacant(fromX + i, fromY - i):
                return False
        return True
    elif not goBelow and goRight:
        for j in range(path_len):
            i = j + 1
            if board.isSpotVacant(fromX - i, fromY + i):
                return False
        return True
    else:
        for j in range(path_len):
            i = j + 1
            if board.isSpotVacant(fromX - i, fromY - i):
                return False
        return True


def isDestinationEmpty(board, fromX, fromY, toX, toY):
    piece_name = board.getPiece(fromX, fromY)
    piece_name1 = board.getPiece(toX, toY)
    if piece_name1[0] == '.':
        return True
    if piece_name[0] is not piece_name1[0]:
        return True
    return False


class Bishop(Piece):
    def __init__(self, available, x, y):
        super().__init__(available, x, y)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False
        if abs(fromX - toX) == abs(fromY - toY):
            if (not isPathObstructed(board, fromX, fromY, toX, toY)) and isDestinationEmpty(board, fromX, fromY, toX, toY):
                return True
        return False

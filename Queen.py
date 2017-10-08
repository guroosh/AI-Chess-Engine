from Piece import Piece


def isDestinationEmpty(board, fromX, fromY, toX, toY):
    piece_name = board.getPiece(fromX, fromY)
    piece_name1 = board.getPiece(toX, toY)
    if piece_name1[0] == '.':
        return True
    if piece_name[0] is not piece_name1[0]:
        return True
    return False


def isPathAllowed(self, board, fromX, fromY, toX, toY):
    print(fromX, fromY, toX, toY)
    if toY == fromY:
        move = int((toX - fromX) / abs(fromX - toX))  # +1/-1
        while (fromX != toX):
            fromX += move
            if (board.isSpotVacant(fromX, fromY) == False):
                return False
        return True
    if toX == fromX:
        move = int((toY - fromY) / abs(toY - fromY))
        while (fromY != toY):
            fromY += move
            if (board.isSpotVacant(fromX, fromY) == False):
                return False
        return True


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


class Queen(Piece):
    def __init__(self, name):
        super().__init__(name)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        return False

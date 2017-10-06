from Piece import Piece

def isDestinationEmpty(board, fromX, fromY, toX, toY):
    piece_name = board.getPiece(fromX, fromY)
    piece_name1 = board.getPiece(toX, toY)
    if piece_name1[0] == '.':
        return True
    if piece_name[0] is not piece_name1[0]:
        return True
    return False

def isPathAllowed(board, fromX, fromY, toX, toY):
    if toY == fromY:
        move = toX - fromX / abs(fromX - toX)  # +1/-1
        while fromX != toX + move:
            fromX += move
            if not board.isSpotVacant(fromX, fromY):
                return False
        return True
    if toX == fromX:
        move = toY - fromY / abs(toY - fromY)
        while fromY != toY + move:
            fromY += move
            if not board.isSpotVacant(fromX, fromY):
                return False
        return True

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


class Queen(Piece):
    def __init__(self, name):
        super().__init__(name)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        return False

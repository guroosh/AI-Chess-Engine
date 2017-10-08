from Piece import Piece


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

def isPathAllowed(board, fromX, fromY, toX, toY):
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



class Queen(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if abs(fromX - toX) == abs(fromY - toY):
            if (not isPathObstructed(board, fromX, fromY, toX, toY)) and isDestinationEmpty(board, fromX, fromY, toX, toY):
                return True
            else:
                return False
        elif toX == fromX or toY == fromY:
            return isPathAllowed(board, fromX, fromY, toX, toY)
        return False

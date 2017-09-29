from Spot import Spot


# done
class Board:
    w = 8
    h = 8
    spots = [[0 for x in range(8)] for y in range(8)]

    def __init__(self):
        for i in range(self.h):
            for j in range(self.w):
                self.spots[i][j] = Spot(i, j, '.')

    def getSpot(self, x, y):
        return self.spots[x][y]

    def printBoard(self):
        for i in range(self.h):
            print(8 - i, '\t', end='')
            for j in range(self.w):
                piece = self.spots[i][j].piece
                if piece.name == '.':
                    print(u'\uFE63' + '\t', end='')
                else:
                    print(piece.unicode() + '\t', end='')
            print()
        print(u'\t\u0041\t\u0042\t\u0043\t\u0044\t\u0045\t\u0046\t\u0047\t\u0048')

    def getPiece(self, x, y):
        # print(self.spots[x][y].piece.name)
        return self.spots[x][y].piece.name

    def init(self, color):
        if color == 'B':
            opponent_color = 'W'
            special = {0: 'rook', 1: 'knight', 2: 'bishop', 3: 'king', 4: 'queen', 5: 'bishop', 6: 'knight', 7: 'rook'}
        else:
            opponent_color = 'B'
            special = {0: 'rook', 1: 'knight', 2: 'bishop', 3: 'queen', 4: 'king', 5: 'bishop', 6: 'knight', 7: 'rook'}
        for i in range(self.h):
            self.spots[7][i] = Spot(0, i, color + special[i])
            self.spots[6][i] = Spot(1, i, color + 'pawn')
            self.spots[0][i] = Spot(0, i, opponent_color + special[i])
            self.spots[1][i] = Spot(1, i, opponent_color + 'pawn')

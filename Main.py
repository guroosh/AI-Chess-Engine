from random import randint

from Board import Board


def printBoard(board):
    board.printBoard()


def getMove(board):
    printBoard(board)
    move = input('Do next move: ')
    return move


def updateBoard(board, move):
    return board


def initBoard(color):
    board = Board()
    board.init(color)
    return board


def makeTree():
    return 1


def evaluateTree(tree):
    return tree


def main():
    color = randint(1, 2)
    if color == 1:
        color = 'B'
    else:
        color = 'W'
    print(color)
    board = initBoard(color)
    if color == 'B':
        move = getMove(board)
        board = updateBoard(board, move)
    while True:
        tree = makeTree()
        nextMove = evaluateTree(tree)
        board = updateBoard(board, nextMove)
        nextMove = getMove(board)
        board = updateBoard(board, nextMove)


main()

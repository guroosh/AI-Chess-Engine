from random import randint

from Board import Board

from Move import Move

def printBoard(board):
    board.printBoard()


def getMove(board, example=''):
    printBoard(board)
    move = input('Do next move '+example+': ')
    move = Move(move)
    while True:
        if move.isValidInput():
            if move.isValidRule(board):
                return move.coded
            else:
                move = input('Not valid according to rules, enter again: ')
        else:
            move = input('Please enter a valid move: ')


def updateBoard(board, move):
    board.updateBoard(move);
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
        move = getMove(board, '(eg: from D2 to D4 -> \'D2D4\')')
        board = updateBoard(board, move)
    done_first_move = False
    while True:
        # tree = makeTree()
        # nextMove = evaluateTree(tree)
        # board = updateBoard(board, nextMove)
        if not done_first_move:
            #TODO: check for player vs player alternate move
            nextMove = getMove(board, '(eg: from D2 to D4 -> \'D2D4\')')
            done_first_move = True
        else:
            nextMove = getMove(board)
        board = updateBoard(board, nextMove)


main()

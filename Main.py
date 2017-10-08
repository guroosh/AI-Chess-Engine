from Board import Board
from Global import Global

from Move import Move


def printBoard(board):
    board.printBoard()


def getMove(board, turn, example=''):
    printBoard(board)
    move = input(turn + example + ': ')
    while True:
        if len(move) is not 4:
            move = input('Please enter a four digit input (eg: from D2 to D4 -> \'D2D4\'): ')
        else:
            move = Move(move)
            if move.isValidInput():
                if move.isValidRule(board, turn):
                    return move.coded
                else:
                    move = input('Not valid according to rules, enter again: ')
            else:
                move = input('Please enter a valid move (eg: from D2 to D4 -> \'D2D4\'): ')


def updateBoard(board, move):
    board.updateBoard(move)
    return board


def initBoard(color):
    board = Board()
    board.init(color)
    return board


def makeTree():
    return 1


def evaluateTree(tree):
    return tree


def analyse(board, move):
    board.analyse()
    if Global.doesCastle:
        Global.doesCastle = False

    pass


def main():
    color = 'B'
    turn = 'WHITE'
    board = initBoard(color)
    if color == 'B':
        move = getMove(board, 'WHITE', '\'S TURN (eg: from D2 to D4 -> \'D2D4\')')
        analyse(board, move)
        board = updateBoard(board, move)
        turn = 'BLACK'
    # done_first_move = False
    while True:
        nextMove = getMove(board, turn, '\'S TURN')
        analyse(board, nextMove)
        board = updateBoard(board, nextMove)
        if turn is 'BLACK':
            turn = 'WHITE'
        else:
            turn = 'BLACK'

            # while True:
            #     # tree = makeTree()
            #     # nextMove = evaluateTree(tree)
            #     # board = updateBoard(board, nextMove)
            #     if not done_first_move:
            #         nextMove = getMove(board, '(eg: from D2 to D4 -> \'D2D4\')')
            #         done_first_move = True
            #     else:
            #         nextMove = getMove(board)
            #     board = updateBoard(board, nextMove)


main()

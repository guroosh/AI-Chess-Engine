import copy
import random
import time

from Board import Board
from Global import Global
from Move import Move
from Piece import Piece
from Spot import Spot
from TreeNode import TreeNode


def printBoard(board):
    board.printBoard()


def getMove(board, turn, example=''):
    printBoard(board)
    move = input(turn + example + ': ')
    while True:
        if len(move) != 4:
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


def getTempUpdatedBoard(board, m):
    temp_board = board.nextPossibleBoard(m)
    return temp_board


def my_copy(board):
    temp_board = Board()
    for i in range(board.h):
        for j in range(board.w):
            piece_name = board.spots[i][j].piece.name
            piece = Piece(piece_name, moved=False)
            spot = Spot(i, j, piece, moved=False)
            temp_board.spots[i][j] = spot
    return temp_board


def flipTurn(turn):
    if turn[0] == 'B':
        return 'W'
    return 'B'


def flipMinimax(minimax):
    if minimax == 'max':
        return 'min'
    return 'max'


# def makeTree2(board, level, depth, turn):
#     if level == depth:
#         return -1
#     next_moves = board.getAllMoves(turn[0])
#     node = TreeNode2()
#     for m in next_moves:
#         temp_board = copy.deepcopy(board)
#         temp_board = getTempUpdatedBoard(temp_board, m)
#         child = makeTree2(temp_board, level + 1, depth, flipTurn(turn))
#         if child == -1:
#             if turn == 'B':
#                 node.min_val = board.evaluateBoard()[0]
#                 node.max_val = board.evaluateBoard()[0]
#             else:
#                 node.min_val = board.evaluateBoard()[1]
#                 node.max_val = board.evaluateBoard()[1]
#             return node
#         node.max_val = max(node.max_val, child.max_val)
#         node.min_val = min(node.min_val, child.min_val)
#         # node.children.append(child)
#     return node


def makeTree(board, level, depth, turn, player, minimax, alpha, beta):
    if level == depth:
        return -1
    next_moves = board.getAllMoves(turn[0])
    random.shuffle(next_moves)
    node = TreeNode()
    for m in next_moves:
        temp_board = copy.deepcopy(board)
        temp_board = getTempUpdatedBoard(temp_board, m)
        child = makeTree(temp_board, level + 1, depth, flipTurn(turn), player, flipMinimax(minimax), alpha, beta)
        if child == -1:
            wPoints, bPoints = board.evaluateBoard()
            white_value = wPoints - bPoints
            black_value = bPoints - wPoints
            if player == 'B':
                node.value = black_value
            else:
                node.value = white_value
            # node.children = None
            node.move = m
            return node
        if minimax == 'max':
            if alpha < child.value:
                alpha = child.value
                best_move = m
                node.value = alpha
                node.move = best_move
        else:
            if beta > child.value:
                beta = child.value
                best_move = m
                node.value = beta
                node.move = best_move
        # node.children.append(child)
        if alpha >= beta:
            return node  # could be return -2 or something or this works as well
    return node


def evaluateTree(tree):
    return tree


def analyse(board, move):
    board.analyse()
    if Global.doesCastle:
        Global.doesCastle = False
        if move == 'e1g1' or move == 'E1g1' or move == 'e1G1' or move == 'E1G1':
            updateBoard(board, 'h1f1')
        elif move == 'e1c1' or move == 'E1c1' or move == 'e1C1' or move == 'E1C1':
            updateBoard(board, 'a1d1')
        elif move == 'e8g8' or move == 'E8g8' or move == 'e8G8' or move == 'E8G8':
            updateBoard(board, 'h8f8')
        elif move == 'e8c8' or move == 'E8c8' or move == 'e8C8' or move == 'E8C8':
            updateBoard(board, 'a8d8')


def autoMove(board, turn):
    printBoard(board)
    print()
    print()
    move = board.getRandomMove(turn[0])
    return move


# def main():
#     color = 'B'
#     turn = 'WHITE'
#     board = initBoard(color)
#     if color == 'B':
#         move = getMove(board, 'WHITE', '\'S TURN (eg: from D2 to D4 -> \'D2D4\')')
#         analyse(board, move)
#         board = updateBoard(board, move)
#         turn = 'BLACK'
#     # done_first_move = False
#     while True:
#         nextMove = getMove(board, turn, '\'S TURN')
#         analyse(board, nextMove)
#         board = updateBoard(board, nextMove)
#         if turn is 'BLACK':
#             turn = 'WHITE'
#         else:
#             turn = 'BLACK'
#
#             # while True:
#             #     # tree = makeTree()
#             #     # nextMove = evaluateTree(tree)
#             #     # board = updateBoard(board, nextMove)
#             #     if not done_first_move:
#             #         nextMove = getMove(board, '(eg: from D2 to D4 -> \'D2D4\')')
#             #         done_first_move = True
#             #     else:
#             #         nextMove = getMove(board)
#             #     board = updateBoard(board, nextMove)


# def main():
#     # auto M vs M random
#     color = 'B'
#     turn = 'WHITE'
#     print('INITIAL board')
#     board = initBoard(color)
#     if color == 'B':
#         move = autoMove(board, turn)
#         analyse(board, move)
#         print(turn + '\'s turn')
#         board = updateBoard(board, move)
#         w,b=board.evaluateBoard()
#         print("White: ",w,", Black: ",b);
#         turn = 'BLACK'
#     # done_first_move = False
#     count = 0
#     while True:
#         nextMove = autoMove(board, turn)
#         analyse(board, nextMove)
#         print(turn + '\'s turn')
#         board = updateBoard(board, nextMove)
#         w, b = board.evaluateBoard()
#         print("White: ", w, ", Black: ", b)
#
#         if turn == 'BLACK':
#             turn = 'WHITE'
#         else:
#             turn = 'BLACK'
#         count += 1
#         if count > 10000:
#             break


# def printTree(node):
#     if node is None:
#         print(None)
#         return
#     print(node.value)
#     for i in node.children:
#         printTree(i)
#     pass


def main():
    # auto M vs M tree
    color = 'B'
    turn = 'WHITE'
    depth = 3
    # print('INITIAL board')
    board = initBoard(color)
    alpha = -10000000
    beta = 10000000
    if color == 'B':
        start_time = time.time()
        root = makeTree(copy.deepcopy(board), 0, depth, turn, turn, "max", alpha, beta)
        print(root.move)
        print(time.time() - start_time)
        # start_time = time.time()
        # root = makeTree2(copy.deepcopy(board), 0, 3, turn)
        # print(time.time() - start_time)
        # for i in range(20):
        #     print(len(root.children[i].children))
        # printTree(root)
        # exit()
        # move = autoMove(board, turn)
        analyse(board, root.move)
        printBoard(board)
        print(turn + '\'s turn')
        board = updateBoard(board, root.move)
        w, b = board.evaluateBoard()
        print("White: ", w, ", Black: ", b)
        turn = 'BLACK'
    # done_first_move = False
    count = 0
    while True:
        # nextMove = autoMove(board, turn)
        start_time = time.time()
        root = makeTree(copy.deepcopy(board), 0, depth, turn, turn, "max", alpha, beta)
        analyse(board, root.move)
        if count % 10 == 0:
            print(root.move)
            print(time.time() - start_time)
            printBoard(board)
            print(turn + '\'s turn')
        board = updateBoard(board, root.move)
        if count % 10 == 0:
            w, b = board.evaluateBoard()
            print("White: ", w, ", Black: ", b)

        if turn == 'BLACK':
            turn = 'WHITE'
        else:
            turn = 'BLACK'
        count += 1
        if count > 10000:
            break


main()

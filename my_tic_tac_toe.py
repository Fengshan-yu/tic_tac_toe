# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:39:06 2022

@author: adminstrator
"""

import random
display = """
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
"""

board = [["1","2","3"],["4","5","6"],["7","8","9"]]
board_dict = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(display)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    global move
    move = input("Please indicate your next move: ")
    board[board_dict[int(move)][0]][board_dict[int(move)][1]] = "O"
    del board_dict[int(move)]

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_board = [int(char) for char in display if char.isdigit()]
    return free_board

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    rows = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]

    for row in rows:
        elements = [elem for elem in row if elem==sign]
        if len(elements) == 3:
            return True
        else:
            pass

def draw_move(board):
    global step
    step = random.choice(make_list_of_free_fields(board))
    board[board_dict[int(step)][0]][board_dict[int(step)][1]] = "X"
    del board_dict[int(step)]

print("Welcome to my game.")
input("Please press enter to start")
display = display.replace(f"{board[1][1]}", "X")

del board_dict[int(board[1][1])]
board[1][1] = "X"
display_board(display)

while len(board_dict) > 0:
    enter_move(board)
    display = display.replace(f"{move}", "O")
    display_board(display)
    if victory_for(board, "O"):
        print("You won.")
        break
    else:
        draw_move(board)
        display = display.replace(f"{step}", "X")
        display_board(display)
        if victory_for(board, "X"):
            print("Computer won.")
            break
else:
    print("Game is over.")
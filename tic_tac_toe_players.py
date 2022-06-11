# This is the very first program I wrote up since studying Python on November 10, 2021.
# This is for my son, a first grader, to practise Math.


import numpy as np

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

board = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
board_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    global move
    move = input("Player 1: please indicate your next move: ")
    board[board_dict[int(move)][0], board_dict[int(move)][1]] = f"{player_1}"
    del board_dict[int(move)]


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'sign' has won the game
    lines = [board[:, 0], board[:, 1], board[:, 2], board[0, :], board[1, :], board[2, :],
             [board[0, 0], board[1, 1], board[2, 2]], [board[2, 0], board[1, 1], board[0, 2]]]
    for row in lines:
        elements = []
        for elem in row:
            if elem == sign:
                elements.append(elem)
        if len(elements) == 3:
            return True
        else:
            pass

def draw_move(board):
    global step
    step = input("Player 2: please indicate your next move: ")
    board[board_dict[int(step)][0], board_dict[int(step)][1]] = f"{player_2}"
    del board_dict[int(step)]

print("Welcome to my game.")
input("Please press enter to start")
print(display)
player_1 = input("Play 1, Please enter a character to use: ")
player_2 = input("Play 2, Please enter a character to use: ")

enter_move(board)
display = display.replace(f"{move}", f"{player_1}")
print(display)

while len(board_dict) > 0:
    draw_move(board)
    display = display.replace(f"{step}", f"{player_2}")
    print(display)
    if victory_for(board, f"{player_2}"):
        print("Play 2 won.")
        break

    enter_move(board)
    display = display.replace(f"{move}", f"{player_1}")
    print(display)
    if victory_for(board, f"{player_1}"):
        print("Play 1 won.")
        break
else:
    print("Game is over.")

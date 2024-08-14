import random
from typing import List


def print_tic_tac_toe(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# Initialize a blank Tic Tac Toe board with numbers 1 to 9
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
is_playable = True


def make_move(b, position, mark):
    if b[position - 1] not in ['X', 'O']:
        b[position - 1] = mark

    else:
        print("Position already taken, choose another spot.")


def game_tic_tac_toe():
    global is_playable
    turn = 0
    print_tic_tac_toe(board)
    name = input("Player, what is your name ?\n")

    while is_playable:
        try:
            player_x = int(input(f"{name}, where do you want to place your X?\n"))
            if player_x < 1 or player_x > 9:
                print("Invalid entry. Must be number between 1 and 9")
            make_move(board, player_x, mark="X")
            print_tic_tac_toe(board)
            turn += 1
            updated_board: list[str] = [number for number in board if number != "X"]
        except ValueError:
            print("Invalid entry. Must be number between 1 and 9")

        if turn == 9:
            print("This is a draw")
            is_playable = False
            break
        if (board[0] == board[1] == board[2] or
                board[3] == board[4] == board[5] or
                board[6] == board[7] == board[8] or
                board[0] == board[3] == board[6] or
                board[1] == board[4] == board[7] or
                board[2] == board[5] == board[8] or
                board[0] == board[4] == board[8] or
                board[2] == board[4] == board[6]):
            is_playable = False
            print(f"{name} has won")
            break
        if board[4] == "5":
            ai_input = int(board[4])
        elif board[0] == board[1] == "X" and board[2] != "O":
            ai_input = int(board[2])
        elif board[0] == board[2] == "X" and board[1] != "O":
            ai_input = int(board[1])
        elif board[1] == board[2] == "X" and board[0] != "O":
            ai_input = int(board[0])
        elif board[3] == board[4] == "X" and board[5] != "O":
            ai_input = int(board[5])
        elif board[3] == board[5] == "X" and board[4] != "O":
            ai_input = int(board[4])
        elif board[4] == board[5] == "X" and board[3] != "O":
            ai_input = int(board[3])
        elif board[6] == board[7] == "X" and board[8] != "O":
            ai_input = int(board[8])
        elif board[6] == board[8] == "X" and board[7] != "O":
            ai_input = int(board[7])
        elif board[7] == board[8] == "X" and board[6] != "O":
            ai_input = int(board[8])
        elif board[0] == board[3] == "X" and board[6] != "O":
            ai_input = int(board[6])
        elif board[0] == board[6] == "X" and board[3] != "O":
            ai_input = int(board[3])
        elif board[3] == board[6] == "X" and board[0] != "O":
            ai_input = int(board[0])
        elif board[1] == board[4] == "X" and board[7] != "O":
            ai_input = int(board[7])
        elif board[1] == board[7] == "X" and board[4] != "O":
            ai_input = int(board[3])
        elif board[4] == board[7] == "X" and board[1] != "O":
            ai_input = int(board[1])
        elif board[2] == board[5] == "X" and board[8] != "O":
            ai_input = int(board[8])
        elif board[2] == board[8] == "X" and board[5] != "O":
            ai_input = int(board[5])
        elif board[5] == board[8] == "X" and board[2] != "O":
            ai_input = int(board[2])
        elif board[0] == board[4] == "X" and board[8] != "O":
            ai_input = int(board[8])
        elif board[0] == board[8] == "X" and board[4] != "O":
            ai_input = int(board[4])
        elif board[4] == board[8] == "X" and board[0] != "O":
            ai_input = int(board[0])
        elif board[2] == board[4] == "X" and board[6] != "O":
            ai_input = int(board[6])
        elif board[2] == board[6] == "X" and board[4] != "O":
            ai_input = int(board[4])
        elif board[4] == board[6] == "X" and board[2] != "O":
            ai_input = int(board[2])

        elif board[0] == board[1] == "O" and board[2] != "X":
            ai_input = int(board[2])
        elif board[0] == board[2] == "O" and board[1] != "X":
            ai_input = int(board[1])
        elif board[1] == board[2] == "O" and board[0] != "X":
            ai_input = int(board[0])
        elif board[3] == board[4] == "O" and board[5] != "X":
            ai_input = int(board[5])
        elif board[3] == board[5] == "O" and board[4] != "X":
            ai_input = int(board[4])
        elif board[4] == board[5] == "O" and board[3] != "X":
            ai_input = int(board[3])
        elif board[6] == board[7] == "O" and board[8] != "X":
            ai_input = int(board[8])
        elif board[6] == board[8] == "O" and board[7] != "X":
            ai_input = int(board[7])
        elif board[7] == board[8] == "O" and board[6] != "X":
            ai_input = int(board[8])
        elif board[0] == board[3] == "O" and board[6] != "X":
            ai_input = int(board[6])
        elif board[0] == board[6] == "O" and board[3] != "X":
            ai_input = int(board[3])
        elif board[3] == board[6] == "O" and board[0] != "X":
            ai_input = int(board[0])
        elif board[1] == board[4] == "O" and board[7] != "X":
            ai_input = int(board[7])
        elif board[1] == board[7] == "O" and board[4] != "X":
            ai_input = int(board[3])
        elif board[4] == board[7] == "O" and board[1] != "X":
            ai_input = int(board[1])
        elif board[2] == board[5] == "O" and board[8] != "X":
            ai_input = int(board[8])
        elif board[2] == board[8] == "O" and board[5] != "X":
            ai_input = int(board[5])
        elif board[5] == board[8] == "O" and board[2] != "X":
            ai_input = int(board[2])
        elif board[0] == board[4] == "O" and board[8] != "X":
            ai_input = int(board[8])
        elif board[0] == board[8] == "O" and board[4] != "X":
            ai_input = int(board[4])
        elif board[4] == board[8] == "O" and board[0] != "X":
            ai_input = int(board[0])
        elif board[2] == board[4] == "O" and board[6] != "X":
            ai_input = int(board[6])
        elif board[2] == board[6] == "O" and board[4] != "X":
            ai_input = int(board[4])
        elif board[4] == board[6] == "O" and board[2] != "X":
            ai_input = int(board[2])

        else:
            ai_input = int(random.choice(updated_board))
        make_move(board, ai_input, mark="O")
        print_tic_tac_toe(board)
        turn += 1

        if (board[0] == board[1] == board[2] or
                board[3] == board[4] == board[5] or
                board[6] == board[7] == board[8] or
                board[0] == board[3] == board[6] or
                board[1] == board[4] == board[7] or
                board[2] == board[5] == board[8] or
                board[0] == board[4] == board[8] or
                board[2] == board[4] == board[6]):
            is_playable = False
            print("Computer has won")
            break


game_tic_tac_toe()

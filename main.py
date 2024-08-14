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
    name1 = input("Player 1, what is your name ?\n")
    name2 = input("Player 2, what is your name ?\n")

    while is_playable:
        try:
            player_x = int(input(f"{name1}, where do you want to place your X?\n"))
            if player_x < 1 or player_x > 9:
                print("Invalid entry. Must be number between 1 and 9")
            make_move(board, player_x, mark="X")
            print_tic_tac_toe(board)
            turn += 1
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
            print(f"{name1} has won")
            break
        try:
            player_o = int(input(f"{name2}, where do you want to place your O?\n"))
            if player_o < 1 or player_o > 9:
                print("Invalid entry. Must be number between 1 and 9")
            make_move(board, player_o, mark="O")
            print_tic_tac_toe(board)
            turn += 1
        except ValueError:
            print("Invalid entry. Must be number between 1 and 9")
        if (board[0] == board[1] == board[2] or
                board[3] == board[4] == board[5] or
                board[6] == board[7] == board[8] or
                board[0] == board[3] == board[6] or
                board[1] == board[4] == board[7] or
                board[2] == board[5] == board[8] or
                board[0] == board[4] == board[8] or
                board[2] == board[4] == board[6]):
            is_playable = False
            print(f"{name2} has won")
            break


game_tic_tac_toe()

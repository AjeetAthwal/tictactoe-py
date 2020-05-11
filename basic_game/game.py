# create ticactoe
def hor_win(board):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[2] != "":
            return True
    return False


def vert_win(board):
    for row_num in range(3):
        if board[0][row_num] == board[1][row_num] and board[1][row_num] == board[2][row_num] and board[2][row_num] != "":
            return True
    return False


def diag_win(board):
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != "":
        return True
    elif board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != "":
        return True
    return False


def win(board):
    return hor_win(board) or vert_win(board) or diag_win(board)


def print_board(board):
    for row in board:
        print(row)


if __name__ == '__main__':
    play_game = 'y'
    while play_game == 'y':
        # gameboard
        board = [["" for i in range(3)] for j in range(3)]
        turn = "X"
        turn_number = 1
        while turn_number < 10:
            print_board(board)
            print(f"Player {turn}'s turn")
            row_move = int(input("input row number: "))
            col_move = int(input("input col number: "))

            while row_move-1 not in range(3) or col_move-1 not in range(3):
                print(f"Player {turn}'s turn, previous move was invalid")
                row_move = int(input("input row number: "))
                col_move = int(input("input col number: "))

            while board[row_move-1][col_move-1] != "":
                print(f"Player {turn}'s turn, that space is already taken")
                row_move = int(input("input row number: "))
                col_move = int(input("input col number: "))

            board[row_move-1][col_move-1] = turn
            if win(board):
                break
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            turn_number += 1

        if win(board):
            print(f'Winner is {turn}')
            result = turn
        else:
            print('Draw!')
            result = 'draw'
        print_board(board)

        play = input("Play again? (y/n) ")
        play_game = play.lower()
    print('thank you for playing!')

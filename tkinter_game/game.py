from tkinter import *
from tkinter import ttk
from functools import partial

# Win conditions for tictactoe


def hor_win(board):
    for row in board:
        if row[0].get() == row[1].get() and row[1].get() == row[2].get() and row[2].get() != "":
            return True
    return False


def vert_win(board):
    for row_num in range(3):
        if board[0][row_num].get() == board[1][row_num].get() and board[1][row_num].get() == board[2][row_num].get() and board[2][row_num].get() != "":
            return True
    return False


def diag_win(board):
    if board[0][0].get() == board[1][1].get() and board[0][0].get() == board[2][2].get() and board[0][0].get() != "":
        return True
    elif board[2][0].get() == board[1][1].get() and board[2][0].get() == board[0][2].get() and board[2][0].get() != "":
        return True
    return False


def win(board):
    return hor_win(board) or vert_win(board) or diag_win(board)


turn = "X"


def calculate(row, column):
    global turn
    if board[row][column].get() == "" and not win(board):
        board[row][column].set(turn)
        if turn == "X" and not win(board):
            turn = "O"
        elif turn == "O" and not win(board):
            turn = "X"
        turn_text.set(f"{turn}'s turn to make a move")
    if win(board):
        turn_text.set(f"{turn} wins!")


def clear_board():
    for row in range(3):
        for column in range(3):
            board[row][column].set("")
    turn_text.set(f"{turn}'s turn to make a move")


root = Tk()
root.title("Tic Tac Toe Game")

board = [[StringVar() for i in range(3)] for j in range(3)]

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

turn_text = StringVar()
ttk.Label(mainframe, textvariable=turn_text).grid(
    column=1, row=1, columnspan=3)
turn_text.set(f"{turn}'s turn to make a move")

for row_index in range(1, 4):
    for col_index in range(1, 4):
        ttk.Button(mainframe, textvariable=board[row_index-1][col_index-1], command=partial(calculate, row_index-1, col_index-1)).grid(
            column=col_index, row=row_index+1)
        board[row_index-1][col_index-1].set("")


ttk.Label(mainframe).grid(column=2, row=5)
ttk.Button(mainframe, text="Reset Game", command=clear_board).grid(
    column=1, row=6, columnspan=3, sticky=W+E+N+S)

root.mainloop()

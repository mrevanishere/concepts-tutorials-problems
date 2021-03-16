board = [['X', '.', '0'],
         ['0', '.', '0'],
         ['X', '.', '0'], ]

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[j][i], end="")
    print()

for row in board:
    for col in row:
        print(col, end="")
    print()


def check_columns(board):
    for i in range(len(board)):
        if '.' != board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    return None

print(check_columns(board))
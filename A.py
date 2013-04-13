# Tic-Tac-Toe-Tomek

"""
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. 
The board starts empty, except that a single 'T' symbol may 
appear in one of the 16 squares. There are two players: X and O. 
They take turns to make moves, with X starting. In each move 
a player puts her symbol in one of the empty squares. 
Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal 
containing 4 of that player's symbols, or containing 3 of her 
symbols and the 'T' symbol, she wins and the game ends. 
Otherwise the game continues with the other player's move. 
If all of the fields are filled with symbols and nobody won, 
the game ends in a draw. See the sample input for examples of 
various winning positions.
"""

X = "X"
O = "O"
T = "T"
EMPTY = "."

def solve_next():
    board = read_board()

    # check each row, column and diagonal for a winner
    winner = get_winner(get_rows(board)) or \
            get_winner(get_cols(board)) or \
            get_winner(get_diags(board))

    if not winner:
        if draw(board):
            return "Draw"
        else:
            return "Game has not completed"

    return "{} won".format(winner)

def draw(board):
    for row in board:
        if EMPTY in row:
            return False

    return True

def get_rows(board):
    return board

def get_cols(board):
    cols = []
    for i in range(4):
        cols.append(map(lambda row: row[i], board))

    return cols

def get_diags(board):
    diag1 = []
    diag2 = []
    for i in range(len(board)):
        diag1.append(board[i][i])
        diag2.append(board[i][len(board)-1-i])

    return [diag1, diag2]

def get_winner(L):
    """
    Declares a winner from the given list of board rows, columns
    or diagonals.
    Returns None if no winner can be found.
    """

    # a "fill" is a generic name for a row, col or diag
    for fill in L:
        
        # check if all the elements are the expected value
        all_same = True
        expected = fill[0]
        for elt in fill[1:]:
            if elt == EMPTY or (elt != T and elt != expected):
                all_same = False
                break
        
        if all_same:
            return expected

    return None

def read_board():
    board = []

    for i in range(4):
        row = []
        row.extend(raw_input())
        board.append(row)
    
    return board

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        print("Case #{}: {}".format(i+1, solve_next()))
        
        # take an extra line due to doc's formatting
        raw_input()

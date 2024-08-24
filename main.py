"""
    'X' = 1,
    'O' = 2,
    ' ' = 0

"""

def board():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    board_columns = [0, 0, 1, 0, 0, 1, 0, 0, 1]
    board_diagonal = [0, 0, 2, 0, 2, 0, 2, 0, 0]
    board_rows = [0, 0, 0, 1, 1, 1, 0, 0, 0]
    
    return board_diagonal
    
# returns player(String), 'X' or 'O'
def check_for_win(board, player):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # check columns
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    
    # check diagonals:
    if board[0] == board[4] == board[8] == player or \
       board[2] == board[4] == board[6] == player:
           return True
       
    return False
        
        

print(check_for_win(board(), 2))
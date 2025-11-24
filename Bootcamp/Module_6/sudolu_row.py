    # Validate overall board structure
# Import literal_eval library to safely evaluate string input as a Python literal 
from ast import literal_eval

# Taking the input
board = literal_eval(input())

def validate_sudoku_rows(board):
    if not isinstance(board, list) or len(board) != 9:
        return "Invalid board"
    
    for row in board:
        if not isinstance(row, list) or len(row) != 9:
            return "Invalid board"
        if any(not isinstance(x, int) or x < 1 or x > 9 for x in row):
            return "Invalid board"
    
    results = []
    for row in board:
        results.append(len(set(row)) == 9)

    return results

# Print the output
print(validate_sudoku_rows(board))

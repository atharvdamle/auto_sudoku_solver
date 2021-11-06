# -----------------------------------------------------------------------------------------------------------------
### AUTOMATIC SUDOKU SOLVER ###
# -----------------------------------------------------------------------------------------------------------------
# This program uses the concept of the backtracking algorithm to solve one of the most popular board games, Sudoku.
# -----------------------------------------------------------------------------------------------------------------



# Function to print the board
def printBoard(board):
    for i in range(9):
        print(*board[i])

#Find the zero
def findzero(board, l):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                l[0]=i
                l[1]=j
                return True
    return False

# Rule 1: No repeated no in the row
def checkrow(board, row, num):
    if num not in board[row]:
        return True
    else:
        return False

# Rule 2: No repeated no in the column
def checkcol(board, col, num):
    for i in range(9):
        if num == board[i][col]:
            return True
    return False

# Rule 3: No repeated no in the 3*3 grid
def checkbox(board, row,col, num):
    for i in range(3):
        for j in range(3):
            if board[i+row][j+col] == num:
                return True
    return False

# Check all the three rules of a Sudoku game
def checkRules(board, row, col, num):
    return checkrow(board, row, num) and not checkcol(board, col, num) and not checkbox(board, row-row%3, col-col%3, num)

# Recursive function that drives the backtracking algorithm
def solveSudoku(board):

    # Temporary list denoting the row and column of the blank space.
    l = [0,0]

    # If no zero is found, that means that all the spaces are filled up and we can stop the recursion.
    if not findzero(board, l):
        return True

    # Otherwise, if a zero value is found, we can assign the value of row and column accordingly for every recursive call.
    row, col = l[0], l[1]

    # Checking all the numbers from 1 to 9 that can fill up the empty space.
    for i in range(1,10):

        # If all the rules check out, then the value is assigned (temporarily).
        if checkRules(board, row, col, i):    
            board[row][col] = i

            # We recursively call this function. If the next number fits the rules on a board that includes the value derived by the previous recursive call, we keep calling the function. 
            if solveSudoku(board):
                return True
            # Otherwise if it doesn't then we return False and go back to the previous board and try another value.
            else:
            # We also change the value of the empty space back to zero.
                board[row][col] = 0  
    
    # If after trying all the combinations we do not find a solution, then we simply return False, that denotes that there is no number that can fill up the empty space and hence, no solution is found.
    return False

# Driver function for the above code.
if __name__ == '__main__':
    
    # Sample sudoku board. The zeros denote an empty space where a number must be inserted.
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
             [5, 2, 0, 0, 0, 0, 0, 0, 0], 
             [0, 8, 7, 0, 0, 0, 0, 3, 1], 
             [0, 0, 3, 0, 1, 0, 0, 8, 0], 
             [9, 0, 0, 8, 6, 3, 0, 0, 5], 
             [0, 5, 0, 0, 9, 0, 6, 0, 0], 
             [1, 3, 0, 0, 0, 0, 2, 5, 0], 
             [0, 0, 0, 0, 0, 0, 0, 7, 4], 
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solveSudoku(board):
        printBoard(board)
    else:
        print('No solution is possible')
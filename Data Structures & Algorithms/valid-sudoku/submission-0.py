class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Make each row, col, and square a key
        # and use a set of their values as values
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                # Check to see if value in row
                if board[row][col] in seen_rows[row]:
                    return False

                # Check to see if value in column
                if board[row][col] in seen_cols[col]:
                    return False

                # Check to see if value in square
                if board[row][col] in seen_squares[(row // 3, col // 3)]:
                    return False

                # If not seen yet, add values to sets
                seen_rows[row].add(board[row][col])
                seen_cols[col].add(board[row][col])
                seen_squares[(row // 3, col // 3)].add(board[row][col])

        return True # If there are no duplicates

             
                
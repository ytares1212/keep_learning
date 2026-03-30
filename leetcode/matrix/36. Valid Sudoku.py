# # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# #     Each row must contain the digits 1-9 without repetition.
# #     Each column must contain the digits 1-9 without repetition.
# #     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# # Note:

# #     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# #     Only the filled cells need to be validated according to the mentioned rules.
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We can use three sets to keep track of the numbers we have seen in each row, column, and 3x3 sub-box. 
        # We will iterate through each cell in the board and check if the number in that cell has already been seen in the corresponding row, column, or sub-box. 
        # If it has, then the board is not valid and we can return False. If it has not, we will add the number to the corresponding sets and continue checking the rest of the cells. 
        # If we finish checking all cells without finding any duplicates, then the board is valid and we can return True.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i] or num in cols[j] or num in boxes[(i // 3) * 3 + j // 3]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)

        return True
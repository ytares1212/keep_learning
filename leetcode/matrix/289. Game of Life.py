# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#     Any live cell with fewer than two live neighbors dies as if caused by under-population.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by over-population.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] % 2 == 1:
                        live_neighbors += 1
                
                if board[i][j] == 1 and live_neighbors in [2,3]:
                    board[i][j] += 2
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] += 2
        #print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 or board[i][j] == 0:
                    board[i][j] = 0
                else:
                    board[i][j] = 1

"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] in 'TX':
                return
            board[row][col] = 'T'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        rows, cols = len(board), len(board[0])
        
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
        
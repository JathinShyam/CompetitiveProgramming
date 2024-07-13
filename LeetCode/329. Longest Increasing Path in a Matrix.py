"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}  # for memozation of (row, col) pair
        def dfs(row, col, prevNum):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] <= prevNum:
                return 0
            if (row, col) in dp:
                return dp[(row, col)]
            res = 1
            num = matrix[row][col]
            res = max(res, 1 + dfs(row + 1, col, num))
            res = max(res, 1 + dfs(row - 1, col, num))
            res = max(res, 1 + dfs(row, col + 1, num))
            res = max(res, 1 + dfs(row, col - 1, num))
            dp[(row, col)] = res
            return res
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
        return max(dp.values())

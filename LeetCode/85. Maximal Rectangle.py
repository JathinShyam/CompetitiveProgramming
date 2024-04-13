"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i- index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxArea = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0]*cols
        for i in range(rows):
            for j in range(cols):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            print(dp)
            print(self.largestRectangleArea(dp))
            maxArea = max(maxArea, self.largestRectangleArea(dp))
        return maxArea            
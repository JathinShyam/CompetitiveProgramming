"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of 
submatrices
 that contains:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.

"""

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result = 0
        rows, cols = len(grid), len(grid[0])
        
        prefixX = [[1 if grid[i][j] == 'X' else 0 for j in range(cols)] for i in range(rows)]
        prefixY = [[1 if grid[i][j] == 'Y' else 0 for j in range(cols)] for i in range(rows)]

        for i in range(1, rows):
            for j in range(cols):
                prefixX[i][j] += prefixX[i-1][j]
                prefixY[i][j] += prefixY[i-1][j]
        
        for i in range(rows):
            for j in range(1, cols):
                prefixX[i][j] += prefixX[i][j-1]
                prefixY[i][j] += prefixY[i][j-1]
                
        for i in range(rows):
            for j in range(cols):
                if prefixX[i][j] and prefixX[i][j] == prefixY[i][j]:
                    result += 1


        return result
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def good(x,y):
            seen = set()
            for dx in range(3):
                for dy in range(3):
                    if 0 <= grid[x+dx][y+dy] <= 9:
                        seen.add(grid[x+dx][y+dy])
            if len(seen) != 9:
                return False
            for dx in range(3):
                rowSum = 0
                for dy in range(3):
                    rowSum += grid[x+dx][y+dy]
                if rowSum != 15:
                    return False
            
            for dy in range(3):
                colSum = 0
                for dx in range(3):
                    colSum += grid[x+dx][y+dy]
                if colSum != 15:
                    return False
            
            diag1, diag2 = 0, 0
            for d in range(3):
                diag1 += grid[x+d][y+d]
                diag2 += grid[x+2-d][y+d]
            if diag1 != 15 or diag2 != 15:
                return False
            return True
        
        rows, cols = len(grid), len(grid[0])
        result = 0
        for x in range(rows-2):
            for y in range(cols-2):
                if good(x,y):
                    result += 1
        return result
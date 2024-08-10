"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.

"""

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS1, COLS1 = len(grid), len(grid[0])
        ROWS2, COLS2 = 3 * ROWS1 , 3 * COLS1
        grid2 = [[0] * COLS2 for _ in range(ROWS2)]

        for r in range(ROWS1):
            for c in range(COLS1):
                r2, c2 = r * 3, c * 3
                if grid[r][c] == "/":
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        
        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r == ROWS2 or c == COLS2 or
                grid2[r][c] != 0 or (r, c) in visit):
                return
            visit.add((r, c))
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]

            for nr, nc in neighbors:
                dfs(nr, nc, visit)
        
        visit = set()
        res = 0
        for r in range(ROWS2):
            for c in range(COLS2):
                if grid2[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c, visit)
                    res += 1
        return res
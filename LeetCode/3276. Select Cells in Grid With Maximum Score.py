"""
You are given a 2D matrix grid consisting of positive integers.

You have to select one or more cells from the matrix such that the following conditions are satisfied:

No two selected cells are in the same row of the matrix.
The values in the set of selected cells are unique.
Your score will be the sum of the values of the selected cells.

Return the maximum score you can achieve.

 

Example 1:

Input: grid = [[1,2,3],[4,3,2],[1,1,1]]

Output: 8

Explanation:



We can select the cells with values 1, 3, and 4 that are colored above.

Example 2:

Input: grid = [[8,7,6],[8,3,2]]

Output: 15

Explanation:



We can select the cells with values 7 and 8 that are colored above.

 

Constraints:

1 <= grid.length, grid[i].length <= 10
1 <= grid[i][j] <= 100

"""

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def go(num, mask):
            if num == 0:
                return 0
            res = go(num-1, mask)
            if num in occurences:
                for row in occurences[num]:
                    if (mask & (1 << row)) == 0:
                        res = max(res, num + go(num-1, mask | (1 << row)))
            return res

        occurences = defaultdict(set)
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                val = grid[i][j]
                occurences[val].add(i)
        return go(100, 0)

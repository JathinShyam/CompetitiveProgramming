"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20

"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n
        left, right = 0, n

        result = [[0]*n for _ in range(n)]
        num = 1
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom):
                result[i][right-1] = num
                num += 1
            right -= 1

            for i in range(right-1, left-1, -1):
                result[bottom-1][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result
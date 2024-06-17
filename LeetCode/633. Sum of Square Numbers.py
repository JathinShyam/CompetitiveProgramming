"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1

"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0

        while a * a <= c:
            b2 = c - a * a

            b = int(sqrt(b2))
            if b * b == b2:
                return True
            a += 1
        return False
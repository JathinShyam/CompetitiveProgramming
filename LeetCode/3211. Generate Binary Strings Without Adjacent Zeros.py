"""
You are given a positive integer n.

A binary string x is valid if all 
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

 

Constraints:

1 <= n <= 18

"""

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0","1"]
        if n == 2:
            return ["11", "01", "10"]
        
        result = []
        def backtrack(curr):
            if len(curr) == n:
                result.append(curr[:])
                return
            if curr[-1] == "1":
                backtrack(curr + "1")
                backtrack(curr + "0")
            else:
                backtrack(curr + "1")
        backtrack("1")
        backtrack("0")
        return result
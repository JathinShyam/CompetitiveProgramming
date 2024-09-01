"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].

"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        N = len(n)
        prefix = int(n[:(N+1)//2])
        possible = {10**N + 1, 10**(N-1) - 1}

        for i in range(prefix-1, prefix+2):
            j = i if N % 2 == 0 else i // 10
            palindrome = i
            while j:
                palindrome = palindrome * 10 + j % 10
                j = j//10
            possible.add(palindrome)
        if num in possible:
            possible.remove(num)
        
        closest = -1
        for ans in possible:
            if closest == -1 or abs(ans - num) < abs(closest - num) or (abs(ans-num) == abs(closest - num) and ans < closest):
                closest = ans
        return str(closest)
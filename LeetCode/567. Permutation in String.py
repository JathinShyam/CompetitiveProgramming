"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        required_hash = sum([hash(x) for x in s1])
        left = 0
        now = 0
        N1, N2 = len(s1), len(s2)
        for right in range(N2):
            now += hash(s2[right])
            if now == required_hash:
                return True
            if right + 1 >= N1:
                now -= hash(s2[right-N1+1])
                left += 1
        return False


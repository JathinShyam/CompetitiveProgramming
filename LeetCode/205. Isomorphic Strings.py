"""

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = {}
        l2 = {}
        for a,b in zip(s,t):
            if (a in l1 and l1[a] != b) or (b in l2 and l2[b] != a):
                return False
            l1[a] = b
            l2[b] = a
        return True
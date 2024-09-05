"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        NS, NP = len(s), len(p)

        @lru_cache(None)
        def isMatch(index_s, index_p):
            if index_s == NS and index_p == NP:
                return True
            
            if index_p == NP:
                return False
            
            if index_s == NS:
                if p[index_p] == '*':
                    return isMatch(index_s, index_p + 1) 
                return False
            
            if s[index_s] == p[index_p]:
                return isMatch(index_s + 1, index_p + 1)
            
            if p[index_p] == '?':
                return isMatch(index_s + 1, index_p + 1)
            
            if p[index_p] == '*':
                return isMatch(index_s + 1, index_p) or isMatch(index_s, index_p + 1)
            
            return False
        
        return isMatch(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        last_match = 0
        star = -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                last_match = i
                star = j
                j += 1
            elif star != -1:
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False
        while j<len(p) and p[j] == '*':
            j += 1
        return j == len(p)
"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        N = len(s)
        
        def dfs(index, current):
            if index == N:
                ans.append(current[:])
                return
            
            for end in range(index, N):
                if s[index:end+1] == s[index:end+1][::-1]:
                    current.append(s[index:end+1])
                    dfs(end+1, current)
                    current.pop()
        dfs(0, [])
        return ans
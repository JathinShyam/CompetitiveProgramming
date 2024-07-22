"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.

"""

class Solution:
    def minCut(self, s: str) -> int:
        d = defaultdict(set)
        N = len(s)

        def helper(i, j):
            while i>=0 and j<N and s[i]==s[j]:
                d[i].add(j)
                i -= 1
                j += 1
        
        for i in range(N):
            helper(i, i)
            helper(i, i+1)
        
        @lru_cache(None)
        def dfs(start):
            if start == N:
                return 0
            cuts = []
            for i in range(start, N):
                if i in d[start]:
                    cuts.append(1 + dfs(i+1))
            return min(cuts)
        
        return dfs(0) - 1
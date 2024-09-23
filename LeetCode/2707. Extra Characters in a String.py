"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
 

Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words


"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Solution:

    def buildTree(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.end_of_word = True
        return root

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        root = self.buildTree(dictionary)

        @lru_cache(None)
        def dp(start):
            if start == N:
                return 0
            ans = dp(start + 1) + 1
            node = root
            for end in range(start, N):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.end_of_word:
                    ans = min(ans, dp(end + 1))
            return ans
        return dp(0)
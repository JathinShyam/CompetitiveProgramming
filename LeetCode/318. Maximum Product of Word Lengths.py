"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.

"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)

        sets = [None for _ in range(N)]
        lengths = [len(i) for i in words]
        best = 0

        def get_set(word):
            s = 0
            for c in word:
                s |= 1 << (ord(c) - ord('a'))
            return s
        
        for i in range(N):
            sets[i] = get_set(words[i])

        for i in range(N):
            for j in range(i+1, N):
                if (sets[i] & sets[j]) == 0:
                    current = lengths[i] * lengths[j]
                    best = max(best, current)
        return best
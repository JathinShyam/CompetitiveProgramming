"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a 
palindrome
.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
 

Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.


"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_mapper = {word:index for index, word in enumerate(words)}

        result = []
        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                left = word[:i]
                right = word[i:]

                reversed_left = left[::-1]
                reversed_right = right[::-1]

                if reversed_left in word_mapper and right == reversed_right and word_mapper[reversed_left] != idx:
                    result.append([idx, word_mapper[reversed_left]])
                
                if i > 0 and reversed_right in word_mapper and reversed_left == left and word_mapper[reversed_right] != idx:
                    result.append([word_mapper[reversed_right], idx])

        return result

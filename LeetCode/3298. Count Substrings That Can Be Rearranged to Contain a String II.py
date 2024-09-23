"""
You are given two strings word1 and word2.

A string x is called valid if x can be rearranged to have word2 as a 
prefix
.

Return the total number of valid 
substrings
 of word1.

Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.

 

Example 1:

Input: word1 = "bcca", word2 = "abc"

Output: 1

Explanation:

The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.

Example 2:

Input: word1 = "abcabc", word2 = "abc"

Output: 10

Explanation:

All the substrings except substrings of size 1 and size 2 are valid.

Example 3:

Input: word1 = "abcabc", word2 = "aaabc"

Output: 0

 

Constraints:

1 <= word1.length <= 106
1 <= word2.length <= 104
word1 and word2 consist only of lowercase English letters.

"""

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        required = [0] * 26
        current = [0] * 26
        for i in word2:
            c = ord(i) - ord('a')
            required[c] += 1
        unique = [i for i in range(26) if required[i] > 0]
        left = 0
        count = 0

        for right in range(len(word1)):
            c = ord(word1[right]) - ord('a')
            current[c] += 1

            while all(current[char] >= required[char] for char in unique ):
                current[ord(word1[left]) - ord('a')] -= 1
                left += 1
            count += left
        return count

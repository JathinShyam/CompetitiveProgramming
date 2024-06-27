"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?


"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = Counter()
        countT = Counter(t)

        have, need = 0, len(countT)
        res, resLen = "", float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                windowSize = right - left + 1
                if windowSize < resLen:
                    res = s[left: right+1]
                    resLen = windowSize
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        return res if resLen != float("infinity") else ""

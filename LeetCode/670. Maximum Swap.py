"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        N = len(digits)
        max_digit_index = list(range(N))

        for i in range(N-2, -1, -1):
            if digits[i] <= digits[max_digit_index[i+1]]:
                max_digit_index[i] = max_digit_index[i + 1]
        
        for i in range(N):
            max_index = max_digit_index[i]

            if digits[i] < digits[max_index]:
                digits[max_index], digits[i] = digits[i], digits[max_index]
                break
        return int(''.join(digits))

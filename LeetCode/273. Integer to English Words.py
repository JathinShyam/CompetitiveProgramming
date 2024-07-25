"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1

"""

class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        
        result = []
        i = 0
        while num > 0:
            part = num % 1000
            num = num // 1000

            if part == 0:
                i += 1
                continue
            
            temp = []
            if part // 100:
                temp.append(ones[part // 100])
                temp.append("Hundred")
            if part % 100 >= 10 and part % 100 <= 19:
                temp.append(teens[part % 10])
            else:
                if part % 100 >= 20:
                    temp.append(tens[part % 100 // 10])
                if part % 10:
                    temp.append(ones[part % 10])
            if i > 0:
                temp.append(suffixes[i])
            result = temp + result
            i += 1
        return " ".join(result)
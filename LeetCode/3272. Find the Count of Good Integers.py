"""
You are given two positive integers n and k.

An integer x is called k-palindromic if:

x is a 
palindrome
.
x is divisible by k.
An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

551 because it can be rearranged to form 515.
525 because it is already k-palindromic.
Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

 

Constraints:

1 <= n <= 10
1 <= k <= 9

"""

class Solution:
    def countGoodIntegers(self, N: int, K: int) -> int:
        if N == 1:
            return sum([i%K==0 for i in range(1,10)])
        
        leftHalf = (N+1) // 2
        result = 0
        seen = set()

        fact = [1]
        for i in range(1, N+1):
            fact.append(fact[-1] * i)

        for i in range(10**(leftHalf-1), 10**leftHalf):
            if N % 2 == 0:
                current = str(i) + str(i)[::-1]
            else:
                current = str(i) + str(i//10)[::-1]
            
            if int(current) % K != 0:
                continue
            
            c = Counter(current)
            key = "".join(sorted(list(current)))
            if key in seen:
                continue
            seen.add(key)
            
            combs = fact[N]
            for j in c.values():
                combs //= fact[j]
            
            result += combs

            if c["0"] > 0:
                combs = fact[N-1]
                c["0"] -= 1
                for j in c.values():
                    combs //= fact[j]
                result -= combs
        return result

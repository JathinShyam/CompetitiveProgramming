"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1, 1]
        for x in range(2, 10):
            fact.append(x * fact[-1])
        
        def getP(n, k):
            if n == 1:
                return "1"
            
            ans = ""
            count = 0

            for x in range(1, n+1):
                count += fact[n-1]

                if count > k:
                    ans += str(x)
                    count -= fact[n-1]

                    r = getP(n-1, k-count)
                    for number in r:
                        if int(number) >= x:
                            ans += str(int(number) + 1)
                        else:
                            ans += str(number)

                    return ans
        return getP(n, k-1)
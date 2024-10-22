"""
You are given an integer array nums.

Any positive divisor of a natural number x that is strictly less than x is called a proper divisor of x. For example, 2 is a proper divisor of 4, while 6 is not a proper divisor of 6.

You are allowed to perform an operation any number of times on nums, where in each operation you select any one element from nums and divide it by its greatest proper divisor.

Return the minimum number of operations required to make the array non-decreasing.

If it is not possible to make the array non-decreasing using any number of operations, return -1.

 

Example 1:

Input: nums = [25,7]

Output: 1

Explanation:

Using a single operation, 25 gets divided by 5 and nums becomes [5, 7].

Example 2:

Input: nums = [7,7,6]

Output: -1

Example 3:

Input: nums = [1,1,1,1]

Output: 0

 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106

"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        def factors(num):
            f = []
            for i in range(num//2+1, 0, -1):
                if(num%i==0):
                    return i
            return -1

        curr = len(nums) - 2
        op = 0
        calculated = {}

        while curr >= 0:
            now = nums[curr]
            next = nums[curr + 1]
            if now <= next:
                curr -= 1
                continue
            if now not in calculated:
                nowf = factors(now)
                calculated[now] = nowf
            else:
                nowf = calculated[now]
            if nowf == 1:
                return -1
            if now // nowf <= next:
                nums[curr] = now // nowf
                curr -= 1
                op += 1
            else:
                return -1
        return op
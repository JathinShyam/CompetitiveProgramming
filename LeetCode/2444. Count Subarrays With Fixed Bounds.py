"""

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106

"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minFound = False
        minStart = 0
        maxFound = False
        maxStart = 0
        start = 0
        count = 0

        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                minFound = False
                maxFound = False
                start = i + 1
            
            if num == minK:
                minFound = True
                minStart = i
            
            if num == maxK:
                maxFound = True
                maxStart = i
            
            if minFound and maxFound:
                count += min(minStart, maxStart) - start + 1

        return count 
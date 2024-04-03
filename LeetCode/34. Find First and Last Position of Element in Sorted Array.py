"""

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

from sortedcontainers import SortedList
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums = SortedList(nums)

        found = False
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                found = True
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        if not found:
            return [-1, -1]
        left = SortedList.bisect_left(nums, target)
        right = SortedList.bisect_right(nums, target)
        return [left, right-1]
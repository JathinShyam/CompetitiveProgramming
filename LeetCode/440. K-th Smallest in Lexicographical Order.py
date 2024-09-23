"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109

"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count the number of elements less than or equal to current prefix within n
        def count_prefix(prefix):
            next_prefix = prefix + 1
            total = 0
            # Keep expanding the current prefix by a factor of 10 (moving to the next level in the trie)
            while prefix <= n:
                # Calculate the number of elements between the current prefix and the next prefix
                total += min(n - prefix + 1, next_prefix - prefix)
                next_prefix *= 10
                prefix *= 10
            return total

        # Starting with the first prefix
        current = 1
        # Since we start from 1, we subtract 1 from k to match 0-based indexing
        k -= 1

        while k:
            count = count_prefix(current)
            # If the remaining k is larger than the count,
            # it means the target is not in the current subtree
            if k >= count:
                k -= count   # Skip the current subtree
                current += 1  # Move to the next sibling
            else:
                # The target is within the current subtree
                k -= 1      # Move to the next level in the trie
                current *= 10
        # The kth number has been found
        return current
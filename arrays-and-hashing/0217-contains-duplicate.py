"""
Problem: 2. Contains Duplicate
Link: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150

Approach: Single-pass hash map. For each element, check if that value has 
already been seen. If yes, return True.
If no, store current value -> index in the map, continue to next index.
If array is fully parsed with no duplicate, return False.

Key insight: Set hash keys to the value, indices as values. 
Think about the hash function h(k) = kmodm.
You need those values to "key" to the indices to find them quickly (O(1))
Doesn't work vice versa.

Time: O(n) - single pass through the array
Space: O(n) - hash map stores up to n entries
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = i
        return False
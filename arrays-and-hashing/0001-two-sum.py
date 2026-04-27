"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach: Single-pass hash map. For each element, check if its complement
(target - current) has been seen. If yes, return the stored index and current
index. If no, store current value -> index in the map.

Key insight: Trade O(n) space for O(n) time. Hash map answers "have I seen
this complement before?" in O(1).

Time: O(n) - single pass through the array
Space: O(n) - hash map stores up to n entries
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            temp = target - nums[i] 
            if temp in seen: 
                res = [seen[temp], i]
                return res
            seen[nums[i]] = i
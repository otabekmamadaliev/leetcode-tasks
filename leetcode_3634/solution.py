"""
LeetCode Problem 3634: Minimum Removals to Balance Array
Difficulty: Medium

Description:
Given an array nums, remove the minimum number of elements so that the
remaining array is balanced: for any remaining elements min and max,
max <= 2 * min.

Approach:
Sort + sliding window:
- Sort nums.
- Expand a right pointer while nums[right] <= 2 * nums[left].
- Track the largest window length that satisfies the condition.
- Minimum removals = n - best_window.

Time Complexity: O(n log n) for sorting
Space Complexity: O(1) extra (sorting in-place)
"""


from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        best_keep = 0
        right = 0

        for left in range(n):
            while right < n and nums[right] <= 2 * nums[left]:
                right += 1
            best_keep = max(best_keep, right - left)

        return n - best_keep

"""
LeetCode Problem 11: Container With Most Water
Difficulty: Medium

Description:
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).
Find two lines that form a container that holds the most water.

Approach:
Two-pointer method:
- Start one pointer at the beginning, the other at the end.
- Move the pointer with the shorter line inward.
- Calculate max area.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        g_max = 0

        while l < r:
            g_max = max(g_max, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return g_max

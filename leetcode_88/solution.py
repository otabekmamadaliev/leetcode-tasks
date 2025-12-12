"""
LeetCode Problem 88: Merge Sorted Array
Difficulty: Medium

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums2 into nums1 as one sorted array in-place.

Approach:
Start filling nums1 from the end:
- Use three pointers: i for nums1, j for nums2, k for merged position.
- Compare elements from the end and place the larger at k.
- Move pointers accordingly.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j != -1:
            if i == -1:
                nums1[k] = nums2[j]
                j -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

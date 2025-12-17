/*
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
*/

import java.util.Arrays;

class Solution {
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int bestKeep = 0;
        int right = 0;

        for (int left = 0; left < n; left++) {
            while (right < n && nums[right] <= 2L * nums[left]) {
                right++;
            }
            bestKeep = Math.max(bestKeep, right - left);
        }

        return n - bestKeep;
    }
}

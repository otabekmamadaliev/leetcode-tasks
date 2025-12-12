/*
LeetCode Problem 80: Remove Duplicates from Sorted Array II
Difficulty: Medium

Description:
Given a sorted array nums, remove duplicates in-place such that duplicates appeared at most twice
and return the new length. Do not allocate extra space for another array.

Approach:
Two-pointer method:
- 'slow' pointer tracks the position to write.
- Iterate through 'nums', allow up to 2 duplicates.
- Update 'nums' in place.

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0;
        for (int num : nums) {
            if (slow < 2 || num != nums[slow-2]) {
                nums[slow] = num;
                slow++;
            }
        }
        return slow;
    }
};

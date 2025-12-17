"""
LeetCode Problem 49: Group Anagrams
Difficulty: Medium

Description:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Approach:
Use a hash map to group strings by their sorted character tuple:
- Sort each string to get a canonical form.
- Use the sorted tuple as a key in a dictionary.
- Group strings with the same sorted form together.

Time Complexity: O(n * k log k) where n is number of strings, k is max length of a string
Space Complexity: O(n * k) for storing the groups
"""


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        checked = {}
        index = 0
        for i in range(len(strs)):
            tmp = tuple(sorted(strs[i]))
            if tmp in checked:
                arr[checked[tmp]].append(strs[i])
            else:
                checked[tmp] = index
                arr.append([strs[i]])
                index += 1
        return arr

/*
LeetCode Problem 49: Group Anagrams
Difficulty: Medium

Description:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Approach:
Use a hash map to group strings by their sorted character form:
- Sort each string to get a canonical form.
- Use the sorted string as a key in a hash map.
- Group strings with the same sorted form together.

Time Complexity: O(n * k log k) where n is number of strings, k is max length of a string
Space Complexity: O(n * k) for storing the groups
*/

import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, Integer> checked = new HashMap<>();
        int index = 0;
        
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            if (checked.containsKey(sorted)) {
                result.get(checked.get(sorted)).add(str);
            } else {
                checked.put(sorted, index);
                List<String> group = new ArrayList<>();
                group.add(str);
                result.add(group);
                index++;
            }
        }
        
        return result;
    }
}

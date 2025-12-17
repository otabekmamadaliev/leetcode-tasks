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
- Use the sorted string as a key in an unordered_map.
- Group strings with the same sorted form together.

Time Complexity: O(n * k log k) where n is number of strings, k is max length of a string
Space Complexity: O(n * k) for storing the groups
*/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, int> checked;
        int index = 0;
        
        for (const string& str : strs) {
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            
            if (checked.find(sorted) != checked.end()) {
                result[checked[sorted]].push_back(str);
            } else {
                checked[sorted] = index;
                result.push_back({str});
                index++;
            }
        }
        
        return result;
    }
};

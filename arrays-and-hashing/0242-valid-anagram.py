"""
Problem: 3. Valid Anagram
Link: https://neetcode.io/problems/is-anagram/history?submissionIndex=0

Approach: Two hash maps. For each element in the each string, increment the count 
of the character each time it is seen. 
Next, parse one hash map, comparing each character count to the other
string's hash map, ensuring all char counts are equal.
If the two string lengths aren't equal, return False. 
If the character counts are equal, return False.
If they are, return True

Key insight: Hash with chars as keys, and COUNTS as values.
Use .get() to retrieve the value associated with the key, 
without raising an error if the key is missing.  

Time: O(n) - single pass through each string
Space: O(n) - hash map stores up to n entries
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(t)):
            seen_s[s[i]] = 1 + seen_s.get(s[i], 0)
            seen_t[t[i]] = 1 + seen_t.get(t[i], 0)

        for c in seen_s:
            if seen_s[c] != seen_t.get(c, 0):
                return False

        return True
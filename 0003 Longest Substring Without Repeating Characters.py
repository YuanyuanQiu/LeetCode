#  Option 1
def lengthOfLongestSubstring(s):
    n = len(s)
    if n <= 1:
        return n
    window = set()
    res = 0
    r = 0
    for i in range(n):
        if i > 0:
            window.remove(s[i-1])
        while r < n and s[r] not in window:
            window.add(s[r])
            r += 1
        res = max(res, r - i)
    return res

# Option 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0

        # FOR loop to iterate right pointer instead of WHILE
        for right in range(len(s)):
            char = s[right]
            
            # If char is found and is within the current window
            if char in char_index_map and char_index_map[char] >= left:
                # Instead of incrementing slow one by one, immediately jump slow to index + 1
                left = char_index_map[char] + 1 
            
            # Update the latest index of the char
            char_index_map[char] = right
            
            # Update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
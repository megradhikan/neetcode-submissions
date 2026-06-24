class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l = 0
        maxlen = 0
        
        # We use r to expand the window across the string
        for r in range(len(s)):
            # If we find a duplicate, shrink the window from the left
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            
            # Now the window is "safe", add the current character
            visit.add(s[r])
            
            # Update the maximum length found so far
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen


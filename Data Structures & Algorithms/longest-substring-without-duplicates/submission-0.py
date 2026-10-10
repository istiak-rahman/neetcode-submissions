class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        countMap = {}
        for r in range(len(s)):
            if s[r] not in countMap:
                countMap[s[r]] = 1
            else:
                countMap[s[r]] += 1
            while countMap[s[r]] > 1:
                countMap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest
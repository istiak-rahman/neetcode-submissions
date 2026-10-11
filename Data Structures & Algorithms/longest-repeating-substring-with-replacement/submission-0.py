class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        countMap = {}
        maxFreq = 0
        
        for r in range(len(s)):
            if s[r] not in countMap:
                countMap[s[r]] = 1
            else:
                countMap[s[r]] += 1
            maxFreq = max(maxFreq, countMap[s[r]])
            curWindowSize = r - l + 1
            if (curWindowSize - maxFreq) > k:
                countMap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest
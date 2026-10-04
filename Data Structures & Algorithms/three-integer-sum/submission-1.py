class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # use a sorted list
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # no duplicate triplets
                continue
            
            j, k = i + 1, n - 1 # two pointers
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: # avoid duplicate triplets
                        j += 1
                        continue
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                        continue
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        
        return result
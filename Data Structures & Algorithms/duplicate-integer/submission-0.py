class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsUnique = set(nums)
        if len(numsUnique) != len(nums):
            return True
        return False
class Solution:
    def distinctDifferenceArray(self, nums):
        n = len(nums)
        res = []
        
        for i in range(n):
            prefix = len(set(nums[:i + 1]))
            suffix = len(set(nums[i + 1:]))
            res.append(prefix - suffix)
        
        return res

class Solution:
    def sumOfUnique(self, nums):
        ans = 0
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for k, v in d.items():
            if v == 1:
                ans += k

        return ans
        

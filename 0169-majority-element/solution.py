class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        t = (n // 2)  # majority threshold
        freq = dict()
        
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for k, v in freq.items():
            if v > t:
                return k
        

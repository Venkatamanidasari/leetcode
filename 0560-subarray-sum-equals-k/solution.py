class Solution:
    def subarraySum(self, nums, k):
        count, cur_sum = 0, 0
        prefix_sum = {0: 1}
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_sum:
                count += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        return count
        

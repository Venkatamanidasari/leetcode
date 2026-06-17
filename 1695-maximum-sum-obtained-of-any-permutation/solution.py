class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = [0] * n
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        count.sort(reverse=True)
        nums.sort(reverse=True)
        return sum(a * b for a, b in zip(nums, count)) % MOD

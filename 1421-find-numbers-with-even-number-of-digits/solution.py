class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)

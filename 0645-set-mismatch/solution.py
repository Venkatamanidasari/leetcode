class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # duplicate = sum(nums) - sum(set(nums))
        duplicate = sum(nums) - sum(set(nums))
        # missing = sum(range(1, n+1)) - sum(set(nums))
        missing = sum(range(1, n + 1)) - sum(set(nums))
        return [duplicate, missing]


# Example usage
nums = [1, 2, 2, 4]
print(Solution().findErrorNums(nums))

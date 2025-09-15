from math import gcd
from typing import List

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x

        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if gcd(first_digit(nums[i]), nums[j] % 10) == 1:
                    ans += 1
        return ans

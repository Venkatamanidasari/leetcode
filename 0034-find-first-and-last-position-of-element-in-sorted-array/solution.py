class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # helper function: finds the first index >= x
        def search(x: int) -> int:
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        l = search(target)          # first index >= target
        r = search(target + 1) - 1  # last index <= target

        if l <= r and l < len(nums) and nums[l] == target:
            return [l, r]
        else:
            return [-1, -1]   

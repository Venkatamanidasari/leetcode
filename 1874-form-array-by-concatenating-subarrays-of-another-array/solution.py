class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        idx = 0
        for group in groups:
            group_len = len(group)
            while idx <= len(nums) - group_len:
                if nums[idx:idx+group_len] == group:
                    idx += group_len
                    break
                idx += 1
            else:
                return False
        return True

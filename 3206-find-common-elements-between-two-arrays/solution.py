from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return [
            sum(x in set2 for x in nums1),  # count nums1[i] also in nums2
            sum(x in set1 for x in nums2)   # count nums2[i] also in nums1
        ]
        

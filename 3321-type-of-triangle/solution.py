class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)  # Sort to make checking easier
        
        # Check triangle inequality
        if a + b <= c:
            return "none"
        
        # Check type
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"

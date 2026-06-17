class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Step 1: compute leftSum
        leftSum = [0] * n
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        
        # Step 2: compute rightSum
        rightSum = [0] * n
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        
        # Step 3: answer
        answer = [abs(leftSum[i] - rightSum[i]) for i in range(n)]
        return answer

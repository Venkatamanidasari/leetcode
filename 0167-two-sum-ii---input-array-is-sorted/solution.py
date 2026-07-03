class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        left=0
        s=0
        right=len(numbers)-1
        while(left<right):
            s=numbers[left]+numbers[right]
            if (s==target):
                result.append(left+1)
                result.append(right+1)
                break
            elif (s>target):
                right=right-1
            else:
                left=left+1
        return result        

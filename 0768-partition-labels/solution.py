class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastoccurrence={}
        for i,char in enumerate(s):
            lastoccurrence[char]=i
        result=[]
        start=0
        end=0
        for i,char in enumerate(s):
            end= max(end, lastoccurrence[char])
            if i==end:
                result.append(end-start+1)
                start=i+1
        return result

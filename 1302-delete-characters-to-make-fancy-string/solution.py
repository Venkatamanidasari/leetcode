class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 1
        for i in range(len(s)):
            if result and result[-1] == s[i]:
                count += 1
            else:
                count = 1
            if count < 3:
                result.append(s[i])
        return ''.join(result)    

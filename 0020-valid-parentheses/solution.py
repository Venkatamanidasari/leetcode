class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif bracket in bracket_map:
                if not stack or stack.pop() != bracket_map[bracket]:
                    return False
        
        return not stack

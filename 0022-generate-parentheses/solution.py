class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(curr, open_count, close_count):
            # If we have used all open and close brackets
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            # Add "(" if we still have open brackets left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            
            # Add ")" if it won't break validity
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter=defaultdict(int)
        bal='balloon'
        for c in text:
            if c in bal:
                counter[c]+=1
        if any(c not in counter for c in bal):
            return 0
        else:
            return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])

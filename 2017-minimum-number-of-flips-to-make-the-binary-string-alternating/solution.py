class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        alt1, alt2 = "", ""

        for i in range(len(s)):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"

        diff1, diff2 = 0, 0
        res = float('inf')

        for i in range(n):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1

        res = min(diff1, diff2)

        for i in range(n, len(s)):
            if s[i - n] != alt1[i - n]:
                diff1 -= 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1

            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1

            res = min(res, diff1, diff2)

        return res

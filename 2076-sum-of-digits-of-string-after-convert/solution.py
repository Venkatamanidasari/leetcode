class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert string to integer
        num = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        num = int(num)

        # Transform the integer k times
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))

        return num

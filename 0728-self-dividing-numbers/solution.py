class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(n: int) -> bool:
            original = n
            while n > 0:
                d = n % 10
                if d == 0 or original % d != 0:
                    return False
                n //= 10
            return True

        result = []
        for x in range(left, right + 1):
            if is_self_dividing(x):
                result.append(x)
        return result

import bisect
from functools import cache


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        @cache
        def Jie(n):
            if n <= 1:
                return 1
            return n * Jie(n - 1)

        i1 = bisect.bisect_right(prime, n)
        i2 = n - i1
        return Jie(i1) * Jie(i2) % (10 ** 9 + 7)
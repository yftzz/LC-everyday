class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        table = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                table[i] += table[i - 1]
        return table[-1]

        


# ----- Formula -----
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        if 1 in [n, m]: return 1
            return reduce(lambda x, y: x*y, range(n, n + m - 1)) / reduce(lambda x, y: x*y, range(1, m))

        
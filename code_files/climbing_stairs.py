class Solution:
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# -------------------------improved-----------------------------------------------------------

    def climbStairs(self, n):
        arr = [-1 for i in range(n + 1)]:
        arr[1] = 1
        arr[2] = 2
        return dp(n, arr)

    def dp(self, n, arr):
        if arr[n] == -1:
            arr[n] = self.dp(n - 1, arr) + self.dp(n - 2, arr)
        return arr[n]

# -------------------------even more improved-----------------------------
    def climbStairs(self, n):
        arr = [-1 for i in range(n + 1)]
        arr[0] = 1
        arr[1] = 1
        for i in range(n - 1):
            arr[i + 2] = arr[i] + arr[i + 1]
        return arr[n]
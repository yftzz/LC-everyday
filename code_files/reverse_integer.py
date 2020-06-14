class Solution:
    def reverse(self, x):
        result = 0

        while x is not 0:
            result = result * 10 + x % (10 * abs(x) // x)
            x = int(x / 10)
        return result if result.bit_length() < 32 or result == -2**31 else 0

    def reverse_improved(self, x):
        result = x // max(abs(x), 1) * int(str(abs(x))[::-1])
        return result if result.bit_length() < 32 or result == -2**31 else 0

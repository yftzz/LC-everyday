class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        res = min(self.findSwap(A, B, A[0]), self.findSwap(A, B, B[0]), self.findSwap(B, A, A[0]), self.findSwap(B, A, B[0]))
        return res if res != float('inf') else -1

    def findSwap(self, A, B, target):
        swap = 0
        for a, b in zip(A, B):
            if a != target:
                if b == target:
                    swap += 1
                else:
                    return float('inf')
        return swap
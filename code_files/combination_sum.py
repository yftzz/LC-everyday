class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        self.back_track(candidates, target,  0, [], res)
        return res

    def back_track(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            self.back_track(candidates=candidates, target=target - candidates[i], index=i, path=path + [candidates[i]], res=res)
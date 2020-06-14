class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        curr = None
        for itv in intervals:
            if not curr:
                curr = itv
                continue

            if curr[1] >= itv[0]:
                curr[1] = max(itv[1], curr[1])
            else:
                res.append(curr)
                curr = itv
        if curr:
            res.append(curr)
        return res

# A more compact solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for itv in sorted(intervals, key = lambda x:x[0]):
            if res and res[-1][-1] >= itv[0]:
                res[-1][-1] = max(res[-1][-1], itv[1])
            else:
                res += [itv]
        return res
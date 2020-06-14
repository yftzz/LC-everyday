class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for c in target:
            if not c in source:
                return -1
        count = 0
        idx = -10
        for c in target:
            idx += 1
            while idx >= 0 and idx < len(source) and source[idx] != c:
                idx += 1 
                    
            if idx < 0 or idx > len(source) - 1:
                idx = source.index(c)
                count += 1
        return count

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        from collections import defaultdict
        from bisect import bisect_left
        for c in target:
            if not c in source:
                return -1
        table = defaultdict(list)
        for i in range(len(source)):
            table[source[i]].append(i)

        count = 1
        idx = -1

        for c in target:
            charList = table[c]
            j = bisect_left(charList, idx)

            if j == len(charList):
                idx = charList[0] + 1
                count += 1
            else:
                idx = charList[j] + 1
        return count
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        setX = set()
        setY = set()
        table = defaultdict(list)
        for x, y in points:
            setY.add(y)
            setX.add(x)
        if len(setX) == len(points) or len(setY) == len(points):
            return 0
        if len(setX) > len(setY):
            for x, y in points:
                table[x].append(y)
        else:
            for x, y in points:
                table[y].append(x)
        
        lastX = {}
        res = float('inf')
        for xi in sorted(table):
            table[xi].sort()
            for i in range(len(table[xi])):
                for j in range(i):
                    if (table[xi][i], table[xi][j]) in lastX:
                        res = min(res, abs(table[xi][i] - table[xi][j]) * abs(lastX[(table[xi][i], table[xi][j])] - xi))
                    lastX[(table[xi][i], table[xi][j])] = xi
        return res if res < float('inf') else 0
        

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')

        for (x, y) in points:
            for (dx, dy) in seen:
                if x == dx or y == dy:
                    continue
                if (x, dy) in seen and (dx, y) in seen:
                    res = min(res, (abs(x - dx) * abs(y - dy)))

            seen.add((x, y))
        return res if res < float('inf') else 0
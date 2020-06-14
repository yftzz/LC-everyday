class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        tableX = dict()
        tableY = dict()
        count = 0 
        for keyX, keyY in stones:
            if not keyX in tableX and not keyY in tableY:
                tableX[keyX] = keyX
                tableY[keyY] = keyX
            elif keyX in tableX and keyY in tableY:
                tableY[tableY[keyY]]
            elif keyY in tableY:
                tableX[keyX] = tableY[keyY]
            elif keyX in tableX:
                tableY[keyY] = tableX[keyX]
            else:
                raise ValueError

        seen = []
        for pos in tableX:
            while pos != tableX[pos]:
                pos = tableX[pos]
            if not pos in seen:
                seen.append(pos)
                count += 1
        return len(stones) - count
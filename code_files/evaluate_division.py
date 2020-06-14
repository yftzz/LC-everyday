class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        table = defaultdict(list)
        for (x, y), val in zip(equations, values):
            table[x].append([val, y])
            table[y].append([1/val, x])
        res_list = []
        for (x, y) in queries:
            res_list.append(self.eval(x,y,table))
        return res_list
    
    def eval(self, x, y, table):
        seen = set()
        seen.add(x)
        if not x in table or not y in table:
            return -1
        stack = [(x, 1)]
        while stack:
            element, val = stack.pop()
            if element == y:
                return val
            seen.add(element)
            for nextVal, nextElement in table[element]:
                if not nextElement in seen:
                    stack.append((nextElement, nextVal * val))
        return - 1
        
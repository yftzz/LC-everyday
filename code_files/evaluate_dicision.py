class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        edges = defaultdict(set)
        for (e1, e2), value in zip(equations, values):
            edges[e1].add((e2, value))
            edges[e2].add((e1, 1/value))
        res = []
        for x, y in queries:
            res.append(self.eval(x,y,edges))
        return res
        
    def eval(self,x, y, table):
        if not x in table:
            return -1.0
        elif x == y:
            return 1.0
        
        stack = [(x, 1)]
        visited = set()
        visited.add(x)
        while stack:
            currNode, currVal = stack.pop()
            if currNode == y:
                return currVal
            for child, value in table[currNode]:
                if not child in visited:
                    stack.append((child, value * currVal))
                    visited.add(child)
        return -1.0
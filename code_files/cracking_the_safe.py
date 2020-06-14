class Solution:
    def crackSafe(self, n,k):
        edges = dict()
        for v in range(k):
            edges[v] = [[(v + i) % k] * 2 for i in range(k)]
        edges

        node = 0
        res = ''
        while edges[node]:
            print(edges[node])
            node = edges[node].pop(0)
            res += str(node)
        return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = []
        res = []
        
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                d = dict()
                if not strs[i][j] in d:
                    d[strs[i][j]] = 0
                d[strs[i][j]] += 1

            if not d in dic:
                dic.append(d)
                res.append([strs[i]])
            else:
                ind = dic.index(d)
                res[ind].append(strs[i])

        return res



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for s in strs:
            key = tuple(sorted(strs))
            dic[key] = dic.get(key, []) + [key]
        return dic.keys()
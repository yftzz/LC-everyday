class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        curr = []
        for d in digits:
            if not res:
                res = list(table[d])
                continue
            for x in res:
                for c in table[d]:
                    curr.append(x+c)
            res = curr
            curr = []
        return res

class improved_Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return table[digits[0]]
        prev = self.letterCombinations(digits[:-1])
        return [x + y for x in prev for y in table[digits[-1]]]



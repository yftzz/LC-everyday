class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = ''
        count = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                if count == K:
                    res = '-' + res
                    count = 0
                res = S[i].upper() + res
                count += 1

        return res



import re
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # S = S.upper().replace('-','')[::-1]
        S = re.sub(r'-','',S[::-1].upper())
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
class Solution:
    def firstUniqChar(self, s):
        if len(s) == 1:
            return 0
        nu = set()
        for i in range(len(s)):
            if s[i] in s[i + 1:] or s[i] in nu:
                nu.add(s[i])
            else:
                return i
        return -1

    def improved(self, s):
        import string
        uniq = [s.index(x) for x in string.ascii_lowercase if s.count(x) == 1]
        return min(uniq) if len(uniq) is not 0 else -1

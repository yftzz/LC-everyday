class Solution:
    def isAnagram(self, s, t):
        a1 = set(list(s))
        for l in a1:
            if s.count(l) != t.count(l):
                return False
        if a1 != set(list(t)):
            return False
        return True

    def imporoved(self, s, t):
        import string
        return all([s.count(i) == t.count(i) for i in string.ascii_lowercase])

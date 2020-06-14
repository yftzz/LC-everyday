class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.put(n)
    def put(self, n, s=0):
    	if n > 0 and s == 0:
    		tmp = self.put(n - 1, 1)
    		return ['(' + x for x in tmp]
    	elif n == 0 and s > 0:
    		return [''.join([')'] * s)]
    	elif n == 0 and s == 0:
    		return ''
    	else:
    		res = []
    		x1 = ['(' + x for x in self.put(n - 1, s + 1)]
    		x2 = [')' + x for x in self.put(n, s - 1)]
    		res.extend(x1)
    		res.extend(x2)
    		return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = 0
        max_count = 0
        record = dict()
        
        for p in s:
            if p == '(':
                if stack not in record:
                    record[stack] = 0
                stack += 1
            elif p == ')' and stack > 0:
                stack -= 1
                record[stack] += 2
                if stack + 1 in record:
                    record[stack] += record[stack + 1]
            else:
                max_count = max(*record.values(), max_count)
                record[0] = 0
        return max(max_count, *record.values())



'''
Another way
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [0] * (len(s) + 1)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    table[i + 1] = table[p] + i - p + 1
        return max(table)
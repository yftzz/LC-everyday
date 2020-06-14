class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        result = s[0]
        for i in range(len(s)):
            if i >= 2 and s[i] == s[i-2]:
                offset = 2
                count = 0
                while i - offset - count > 0 and i + count < len(s) - 1 and s[i - offset - count - 1] == s[i + count + 1]:
                    count += 1

                if count*2 + offset + 1 > len(result):
                    result = s[i - offset - count:i + count + 1]
                
                
            if i >= 1 and s[i] == s[i-1]:
                offset = 1
                count = 0
                while i - offset - count > 0 and i + count < len(s) - 1 and s[i - offset - count - 1] == s[i + count + 1]:
                    count += 1
                if count*2 + offset + 1 > len(result):
                    result = s[i - offset - count:i + count + 1]



        return result



class improved_Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s

        result = s[0]
        for i in range(len(s)):
            result = max(result, self.find(i,i,s), self.find(i,i+1,s), key=len)
        return result

    def find(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
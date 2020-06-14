import string


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        # s = s.lower()

        ptr_pos = 0
        ptr_neg = len(s) - 1
        while ptr_pos<=ptr_neg:
            if s[ptr_pos].lower() == s[ptr_neg].lower():
                ptr_pos += 1
                ptr_neg -= 1
            elif not s[ptr_pos].isalnum() :
                ptr_pos += 1

            elif not s[ptr_neg].isalnum():
                ptr_neg -= 1
            else:
                return False

        return True 
#-----------improved-----------

    def isPalindrome(self, s):
        ss = [k.lower() for k in s if k.islnum()]
        return ss == s[::-1]
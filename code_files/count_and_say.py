class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        '''
        curr_str = '1'
        target = ''
        for _ in range(n-1):
            i = 0
            while i < len(curr_str):
                str_ctr = 1
                while i + str_ctr < len(curr_str):
                    if curr_str[str_ctr + i] == curr_str[i]:
                        str_ctr += 1
                    else:
                        break
                target += str(str_ctr) + curr_str[i]
                i = i + str_ctr
            curr_str = target
            target = ''
        return curr_str
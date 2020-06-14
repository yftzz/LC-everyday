class Solution:
    def myAtoi(self, str):
        num = 0
        sign = 1
        signed = False
        for i in range(len(str)):
            if str[i] == '-' and not signed:
                signed = True
                sign = -1
            elif str[i] == '+' and not signed:
                signed = True
            elif str[i].isdigit():
                num = num * 10 + int(str[i])
                signed = True
            elif str[i]!=' ':
                break
        if num*sign < -2147483648:
            return -2147483648
        if num*sign > 2147483647:
            return 2147483647
        return num*sign

    # def myAtoi(self, str):

# edge case to cover: 1. only one sign. 2. overflow. 3.space in between digits
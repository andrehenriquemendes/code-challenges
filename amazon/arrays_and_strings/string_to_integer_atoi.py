# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):

    def myAtoi(self, s):
        digits_map = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }

        max_int = 2**31 - 1
        min_int = -2**31

        sign = 1
        index = 0
        while index < len(s) and s[index] == ' ':
            index += 1

        if index < len(s) and s[index] == '-':
            sign = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            sign = 1
            index += 1

        result = 0
        while index < len(s) and s[index] in digits_map:
            digit = digits_map[s[index]]

            if result > max_int // 10 or (result == max_int // 10 and digit > max_int % 10):
                return max_int if sign == 1 else min_int

            result = (10 * result) + digit
            index += 1

        return result*sign


sol = Solution()
print(sol.myAtoi("4193 with word"))
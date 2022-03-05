# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        longest_palindrome = ""
        len_longest_palindrome = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len_longest_palindrome:
                    len_longest_palindrome = r - l + 1
                    longest_palindrome = s[l:r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len_longest_palindrome:
                    len_longest_palindrome = r - l + 1
                    longest_palindrome = s[l:r + 1]
                l -= 1
                r += 1

        return longest_palindrome

sol = Solution()
print(sol.longestPalindrome('cbbd'))
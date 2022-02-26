# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2961/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mp = {} # char visited + shift 1
        
        longest_substring = 0
        i = 0
        for j in range(len(s)):
            
            if s[j] in mp:
                # shift the left pointer
                i = max(mp[s[j]], i)
        
            longest_substring = max(longest_substring, j - i + 1)
            mp[s[j]] = j + 1
        
        return longest_substring
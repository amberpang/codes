"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxlen = 1
        string = s[0]
        for i in range(len(s)):
            #odd
            res = self.check(i, i, s, maxlen)
            #even
            res1 = self.check(i, i+1, s, maxlen)
            if len(res) > len(string):
                string = res
            if len(res1) > len(string):
                string = res1
            maxlen = len(string)
        return string

    def check(self, j, k, s, maxlen):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        res = k - j - 1
        if res > maxlen:
            return s[j+1:k]
        else:
            return s[0]


solution = Solution()
print(solution.longestPalindrome("tabax"))

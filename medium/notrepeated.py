"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        templist= []
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in templist:
                templist.append(s[i])
            else:
                maxlen = max(len(templist), maxlen)
                location = self.getlocatin(s[i],templist)
                templist = templist[location:]
                templist.append(s[i])
            maxlen = max(len(templist), maxlen)
        return maxlen

    def getlocatin(self,target, List):
        for i in range(len(List)):
            if target == List[i]:
                return i + 1


solution = Solution()
print(solution.lengthOfLongestSubstring("au"))
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 重点是用zip很方便  a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        #  list(zip(*a))=[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        # a = ["flot","flsab","flxaghj"]  list(zip(*a))=[('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 's', 'x'), ('t', 'a', 'a')]
        temp = list(zip(*strs))
        res = ""
        for item in temp:
            if len(set(item)) == 1:
                res += item[0]
            else:
                break
        return res

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
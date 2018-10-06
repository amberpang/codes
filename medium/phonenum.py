"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

虽然输入的数据从2-9，但是为了输入数据与下标一直，在前两个可随意添加其他数
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        comb = ['']
        for i in digits:
            comb = [prev_+next_ for prev_ in comb for next_ in lookup[int(i)]]
        #如果输入为空，需要把comb换为【】输出
        return comb if comb != [''] else []


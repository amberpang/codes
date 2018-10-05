"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        previous = self.countAndSay(n-1)
        res = item = ""
        num = 0
        for i in range(len(previous)):
            if i == 0:
                num = 1
                item = previous[i]
            else:
                if previous[i] == item:
                    num += 1
                else:
                    res += str(num)+item
                    num = 1
                    item = previous[i]
        res += str(num)+item
        return res


solution = Solution()
print(solution.countAndSay(5))

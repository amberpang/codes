"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """method1"""

        # matrix = [[0]*m for i in range(n)]
        # for i in range(m):
        #     matrix[0][i] = 1
        # for i in range(1,n):
        #     for j in range(m):
        #         if i - 1 > -1:
        #             matrix[i][j] += matrix[i-1][j]
        #         if j - 1 > -1:
        #             matrix[i][j] += matrix[i][j-1]
        # return matrix[n-1][m-1]

        """method2"""
        matrix = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                matrix[j] += matrix[j - 1]
        return matrix[-1]

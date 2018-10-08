"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
#插入第i个点，case1 有两种： i-1个点都在这个点下方，或者 i-1个点都在这个点的上方， 所以case1 = tree[i-1] *2
#case2 : 插入的i点插在中间，以此点为分界点， 加上有x个点在其上面，有y个点在其下面， 则 x + y = i -1
# x 个点的tree 有tree【x】中可能， 则case2 += tree【x】* tree[y], 该情况其实包含case1， 所以可以初始化tree = [1, 1]
#省略case1， 直接用case2

class Solution:
    def numTrees(self, n):
        if n == 0:
            return 0
        tree = [0, 1]
        #需要取到 n ，因为输入的n是指有n个点
        for i in range(2, n + 1):
            case1 = tree[i - 1] * 2
            case2 = 0
            for j in range(i):
                upper = i - 1 - j
                case2 += tree[upper] * tree[j]
            tree.append(case1 + case2)
        return tree[-1]


solution = Solution()
print(solution.numTrees(3))
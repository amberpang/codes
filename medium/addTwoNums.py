"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        carry = 0
        while l1 and l2:
            carry, div = divmod((l1.val + l2.val + carry), 10)
            res.append(div)
            l1 = l1.next
            l2 = l2.next
        while l1:
            carry, div = divmod((l1.val + carry), 10)
            res.append(div)
            l1 = l1.next
        while l2:
            carry, div = divmod((l2.val + carry), 10)
            res.append(div)
            l2 = l2.next
        if carry != 0:
            res.append(carry)
        return res

def func(List):
    head = ListNode(List[0])
    head_temp = head
    for i in List[1:]:
        temp = ListNode(i)
        head_temp.next = temp
        head_temp = temp
    return head


l1 = [2, 4, 3]
l2 = [5, 6, 4]
List1 = func(l1)
List2 = func(l2)
solution = Solution()
print(solution.addTwoNumbers(List1, List2))


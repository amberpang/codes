"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product. 最大乘积

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxafter = minafter = res = nums[0]
        for i in nums[1:]:
            maxhere = max(maxafter * i, minafter * i, i)
            minhere = min(maxafter * i, minafter * i, i)
            res = max(res, maxhere)
            maxafter = maxhere
            minafter = minhere
        return res
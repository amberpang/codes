"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = sum(nums[0:3])
        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                numsum = sum([nums[i], nums[low], nums[high]])
                if abs(target - res) > abs(target - numsum):
                    # print("aaa",res,numsum,abs(target - res) > abs(target - numsum))
                    res = numsum
                if res == target:
                    return res
                if numsum < target:
                    low += 1
                else:
                    high -= 1
        return res
solution = Solution()
print(solution.threeSumClosest([-3, -2, -5, 3, -4],-1))
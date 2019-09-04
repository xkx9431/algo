#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wr, cur, bl = 0, 0, len(nums)-1

        while cur <= bl:
            if nums[cur] == 0:
                nums[wr], nums[cur] = nums[cur], nums[wr]
                cur += 1
                wr += 1
            elif nums[cur] == 2:
                nums[cur], nums[bl] = nums[bl], nums[cur]
                bl -= 1

            else:
                cur += 1

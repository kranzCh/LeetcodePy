#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target > nums[len(nums) - 1]: return len(nums)
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] == target: 
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

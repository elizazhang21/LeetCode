# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i in range(len(nums)):
            if nums[i] in t:
                return [t[nums[i]], i]
            else:
                t[target - nums[i]] = i
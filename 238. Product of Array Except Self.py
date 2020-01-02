# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        count0 = 0
        ind = None
        for i in range(n:=len(nums)):
            if nums[i] != 0:
                mul = mul*nums[i]
            else:
                count0 += 1
                ind = i
                if count0 == 2:
                    return [0 for i in range(n)]
        if count0 == 0:
            return [mul//nums[i] for i in range(n)]
        else:
            return [mul if i == ind else 0 for i in range(n)]
# 0033. Search in Rotated Sorted Array.py

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1

        
        if nums[0] > nums[-1] and target < nums[-1]:
            i = len(nums) - 2
            while i > 0:
                if target == nums[i]:
                    return i
                elif target > nums[i]:
                    return -1
                else:
                    i -= 1
            
        elif target > nums[0]:
                i = 1
                while i<len(nums):         
                    if target == nums[i]:
                        return i
                    elif target < nums[i]:
                        return -1
                    else:
                        i += 1
        return -1
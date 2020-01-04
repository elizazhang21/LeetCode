# 34. Find First and Last Position of Element in Sorted Array.py

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        
        # binary search
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while left > l:
                    if nums[left-1] == target:
                        left -= 1
                    else:
                        break
                while right < r:
                    if nums[right+1] == target:
                        right +=1
                    else:
                        break
                return left, right
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1

        return [-1, -1]
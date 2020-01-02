# 4. Median of Two Sorted Arrays 
from heapq import heapify, heappop, heappush
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = len(nums1)
        k2 = len(nums2)
        i = 0
        heapify(nums1)
        heapify(nums2)
        arr= []
        if not nums1:
            min1 = float("inf")
        else:
            min1 = heappop(nums1)
        
        if not nums2:
            min2 = float("inf")
        else:
            min2 = heappop(nums2)
        prev = None
        curr = None
        
        while i < (k1+k2+1)/2:
            if min1 < min2:
                prev = curr
                curr = min1
                i+=1
                try:
                    min1 = heappop(nums1)
                except:
                    min1 = float("inf")

            else:
                prev = curr
                curr = min2
                i+=1
                try:
                    min2 = heappop(nums2)
                except:
                    min2 = float("inf")
        
        if (k1+k2) % 2 == 0:
            return (curr+prev)/2.0
        else:
            return curr


class findMedianSortedArrays(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        k1 = len(nums1)
        k2 = len(nums2)
        arr = []
        i = 0
        j = 0
        while i < k1 or j < k2:
            if j == k2 and i < k1:
                arr.append(nums1[i])
                i += 1
            elif i == k1 and j < k2:
                arr.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        if (k1+k2) % 2 == 0:
            return (arr[(k1+k2-2)/2] + arr[(k1+k2)/2])/2.0
        else:
            return arr[(k1+k2-1)/2]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 is None:
            nums = nums2
        elif nums2 is None:
            nums = nums1
        else:
            nums = nums1 + nums2
        
        nums.sort()
        
        if len(nums) % 2 == 0:
            i1 = len(nums) / 2 - 1
            i2 = len(nums) / 2
            
            median = nums[int(i1)] + nums[int(i2)]
            median = median / 2
        else:
            median = nums[int(len(nums) / 2)]
        
        return median

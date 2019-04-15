import re

# 1


class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = {}
        for i in range(len(nums)):
            pair = t.get(target-nums[i])
            if(pair is not None):
                return [i, pair]
            t[nums[i]] = i

# 2


class lengthOfLongestSubstring(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = []  # memory for storing characters
        l = 0   # the longest length ever
        for c in s:
            if c in m:
                l = max(l, len(m))
                m = m[m.index(c)+1:]
            m.append(c)
        return max(l, len(m))

# 3


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class addTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        out = None
        while l1 is not None or l2 is not None:
            t1 = 0 if l1 is None else l1.val
            t2 = 0 if l2 is None else l2.val
            o = t1 + t2 + c
            if o >= 10:
                c = 1
                o = o - 10
            else:
                c = 0
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            node = ListNode(o)
            if out is None:
                out = node
                next = out
            else:
                next.next = node
                next = next.next

        if c == 1:
            next.next = ListNode(1)

        return out


# 4

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


class Solution(object):
    def isPalindrome(self, s):
        # convert to alphanumeric
        s = " ".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        s = s.replace(" ", "")  # remove spaces
        if(s != s[::-1]):
            return False  # compare normal string with reversed
        else:
            return True


class reverse:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

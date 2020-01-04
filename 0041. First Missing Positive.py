#0041. First Missing Positive.py

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0 for i in range(n)]
        
        for i in nums:
            if i > 0 and i <= n:
                temp[i-1] += 1
        for i in range(n):
            if temp[i] == 0:
                return i+1
        return n+1
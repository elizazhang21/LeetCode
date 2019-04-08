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
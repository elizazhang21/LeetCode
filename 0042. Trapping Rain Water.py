# 0042. Trapping Rain Water.py

# Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        i, j = 0, len(height) - 1
        lMax, rMax = height[i], height[j]
        water = 0
        while i <= j:
            lMax = max(lMax, height[i])
            rMax = max(rMax, height[j])
            if lMax < rMax:
                water += lMax - height[i]
                i += 1
            else:
                water += rMax - height[j]
                j -= 1
        return water
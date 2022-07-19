# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        currentMax = (len(height) - 1) * min(height[0], height[-1])
        l = 0
        r = len(height) - 1
        while l < r:
            currentMax = max(currentMax, (r - l) * min(height[l],height[r]))
            if height[l] > height[r]:
                r -=1
            else:
                l+=1
        return currentMax
        
            
        
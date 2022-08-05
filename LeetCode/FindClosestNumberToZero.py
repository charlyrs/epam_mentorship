# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = 10e5+1
        for num in nums:
            if num == 0:
                return num
            if abs(num) < abs(ans):
                ans = num
            if abs(num) == abs(ans) and num > ans:
                ans = num
        return ans
        
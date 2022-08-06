# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        for i in range(len(nums) - 1):
            if(sums[i] >= sums[-1] - sums[i]):
                count += 1
        return count
               
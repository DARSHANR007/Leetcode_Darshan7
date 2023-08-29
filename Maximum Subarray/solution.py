class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentmax = totalmax = nums[0]
        for i in range(1, len(nums)):
            currentmax = max(nums[i], nums[i] + currentmax)
            totalmax = max(totalmax, currentmax)
        return totalmax


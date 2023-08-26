# Update the maximum reachable index at each step.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= x:
                x = i
        return True if x == 0 else False






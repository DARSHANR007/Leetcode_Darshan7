class Solution:
    def jump(self, nums: list[int]) -> int:
        l = r = count = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            count += 1
        return count


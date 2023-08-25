class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums):
            r1, r2 = 0, 0
            for num in nums:
                current = max(num + r1, r2)
                r1 = r2
                r2 = current
            return r2

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))

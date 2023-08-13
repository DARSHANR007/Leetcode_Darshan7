class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for i in nums:
            current = max((i + r1), r2)
            r1 = r2
            r2 = current
        return r2

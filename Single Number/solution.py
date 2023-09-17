class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            if nums.count(num) % 2 != 0:
                return num


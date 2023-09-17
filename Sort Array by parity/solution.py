class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        if len(nums) <= 1:
            return nums

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        even.sort()
        odd.sort()

        return even + odd

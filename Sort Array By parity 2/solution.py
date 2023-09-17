class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0  # Index for even positions
        odd_index = 1  # Index for odd positions

        while even_index < len(nums) and odd_index < len(nums):
            if nums[even_index] % 2 == 0:
                # This element is even and in an even position, move to the next even position
                even_index += 2
            elif nums[odd_index] % 2 == 1:
                # This element is odd and in an odd position, move to the next odd position
                odd_index += 2
            else:
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]

        return nums

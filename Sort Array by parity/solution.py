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
#can also be done like this#
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                # Swap odd and even numbers
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1

        return nums



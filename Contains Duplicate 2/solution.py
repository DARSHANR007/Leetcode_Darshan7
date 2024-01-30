class Solution:
    def containsnearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numHash = {}

        for i, num in enumerate(nums):
            if   num in numHash and i - numHash[num] <= k:
                return True
            numHash[num] = i
        return False






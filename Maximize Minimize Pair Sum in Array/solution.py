class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        left=0
        maxElement=0
        right=len(nums)-1
        nums.sort()
        while(left<right):
            maxElement=max(maxElement,nums[right]+nums[left])
            left+=1
            right-=1
        return maxElement


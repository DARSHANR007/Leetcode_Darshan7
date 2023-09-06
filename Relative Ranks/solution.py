class Solution:
    def findRelativeRanks(self, nums: list[int]) -> list[str]:
        d = defaultdict(int)
        place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(nums)
        a = [" "] * n
        for i in range(n): d[nums[i]] = i
        nums.sort(reverse=True)

        for i in range(n):
            if i < 3:
                a[d[nums[i]]] = place[i]
            else:
                a[d[nums[i]]] = str(i + 1)

        return a
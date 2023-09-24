class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 0
        res = 0

        for i in range(len(blocks) - k + 1):
            res = blocks.count('B', i, i + k)
            ans = max(res, ans)

        ans = k - ans
        return ans
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[float("inf")] * (cols + 1) for i in range(rows + 1)]
        dp[rows - 1][cols] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]






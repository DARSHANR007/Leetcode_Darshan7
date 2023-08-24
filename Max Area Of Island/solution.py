class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if 0>r or r>=m or 0>c or c>=n or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
        ans=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans=max(ans,dfs(i,j))
        return ans
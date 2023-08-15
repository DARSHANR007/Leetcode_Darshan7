class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        s = triangle[-1].copy()
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                s[j] = triangle[i][j] + min(s[j], s[j + 1])
        return s[0]
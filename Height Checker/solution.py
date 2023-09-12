class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expectedHeights = [0] * len(heights)
        expectedHeights[0] = heights[0]

        # Sort the expectedHeights list
        for i in range(1, len(heights)):
            expectedHeights[i] = heights[i]
            key = heights[i]
            pos = i - 1
            while pos >= 0 and key < expectedHeights[pos]:
                expectedHeights[pos + 1] = expectedHeights[pos]
                pos -= 1
            expectedHeights[pos + 1] = key

        # Compare heights and expectedHeights
        for j in range(len(heights)):
            if heights[j] != expectedHeights[j]:
                count += 1
        return count

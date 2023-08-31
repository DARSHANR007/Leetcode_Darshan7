class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2: return n
        arr, m = [0, 1], 0
        for i in range(2, n+1):
            arr += [arr[i//2]+arr[i//2+1] if i%2 else arr[i//2]]
            if arr[i]>m: m =arr[i]
        return m
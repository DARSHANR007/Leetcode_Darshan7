class Solution:
    def maxProfit(self, A: List[int]) -> int:
        N=len(A)
        sell=[0]*N
        for _ in range(2):
            buy=-A[0]
            profit=0
            for i in range(1,N):
                buy=max(buy,sell[i]-A[i])
                profit=max(profit,A[i]+buy)
                sell[i]=profit
        return sell[-1]
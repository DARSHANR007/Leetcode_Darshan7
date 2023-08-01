class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,temp=[],[]
        def rec(n,k,num):
            if len(temp)==k:
                ans.append(temp.copy())
            for i in range(num,n+1):
                temp.append(i)
                rec(n,k,i+1)
                temp.pop()
        rec(n,k,1)
        return ans
from typing import List


def sumSubarrayMins(self, A: List[int]) -> int:
        A.append(-1)
        stack,res=[-1],0
        for i in range(len(A)):
            while A[i]<A[stack[-1]]:
                idx=stack.pop()
                res+=A[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return res%(10**9+7)

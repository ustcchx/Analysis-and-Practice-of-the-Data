class Solution:
    def func(self, N: int) -> int:
        mod=1000000007
        if N==0 or N==1 :
            return 1
        elif N==2 :
            return 2
        a=1
        b=1
        c=2
        i=N-2
        while i>0 :
            temp=(a+b+c)%mod
            a=b
            b=c
            c=temp
            i-=1
        return c
n=input()
n=int(n)
So=Solution()
print(So.func(n))
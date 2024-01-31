class Solution:
    def func(self,nums:list[int])->int:
        cout = 0
        if len(nums) == 1 :
            return cout
        cur_pos = 0
        next_pos = 0
        for i in range(len(nums)) :
            next_pos=max(nums[i]+i,next_pos)
            if i == cur_pos :
                cout+=1
                cur_pos=next_pos
                if(cur_pos>=len(nums)-1) :
                    break
        return cout
list0=eval(input())
so=Solution()
print(so.func(list0))            


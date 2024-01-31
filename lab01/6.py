class solution :
    def func(self,list0):
        i = 0
        while i < len(list0):
            if list0[i][0] > list0[i][1] :
                del list0[i]
                continue
            i+=1
        if len(list0) == 1 or len(list0) ==0 :
            return len(list0)
        maxnum=0
        i=0
        for i in range(len(list0)) :
            temp=[]
            for k in range(len(list0)) :
                s=list0[k][:]
                temp.append(s)
            j=0
            while j < len(temp) :
                temp[j][1]-=temp[i][0]
                j+=1
            del temp[i]
            s = self.func(temp)
            if s > maxnum :
                maxnum = s
        return maxnum + 1
so = solution()
list0 = eval(input())
print(so.func(list0))
                
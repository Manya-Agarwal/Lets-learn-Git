def factors(num):
    if num==0 or num==1:
        return num
    else:
        l=[]
        for i in range(1,num//2+1):
            if num%i==0:
                l.append(i)
        return sum(l)

l=list(map(int,input("Enter: ").split()))
l1=[]
for i in l:
    l1.append(factors(i))
flag=0
for i in l1:
    if i in l:
        flag+=1
    else:
        break
if flag==len(l1):
    print(sorted(l1))
else:
    print("-1")
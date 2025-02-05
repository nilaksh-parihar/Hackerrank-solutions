l1=[]
l2=[]
incre=0
num=0
print("Give 5 numbers")
for i in range(0,5):
    a=int(input())
    l1.append(a)
ans=l1[0]+l1[4]
for i in l1:
    for j in l1:
        if i!=j:    
            sum=i+j
            for k in range(0,sum+1):
                num=sum-k
                if num!=0:
                    incre+=1
            if(incre<ans):
                l2.append((i,j))
                ans=incre
        

print(l2," Are the set of numbers closest to zero")                     


'''       if i!=j:    
            sum=i+j
            for k in range(0,sum+1):
                num=sum-k
                if num!=0:
                    incre+=1
                elif (ans==incre):
                    l2.append((i,j))
                elif (ans!=0 & incre<ans):
                    ans = incre
                    l2.clear()
                    l2.append((i,j))'''



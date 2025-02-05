a=int(input("Give the first number:"))
b=int(input("Give the second number:"))
c=0
while(c!=5):
    print("If u want the sum type 1")
    print("If u want the difference type 2")
    print("If u want to multiply type 3")
    print("if u want to divide type 4")
    print("If u want to exit type 5")
    c=int(input())
    if c==1:
        ans=a+b
    elif c==2:
        ans=a-b
    elif c==3:
        ans=a*b
    elif c==4:
        ans=a/b
    elif c==5:
        break    
    else:
        print("wrong input")
    print(ans)        

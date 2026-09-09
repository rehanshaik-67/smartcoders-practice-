n=int(input("enter the number:"))
count=0
while n>0:
    if n&1:
        count=count+1
    n>>=1
print("the number of set bit is:",count)
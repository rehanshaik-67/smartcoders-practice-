n=int(input ("enter the number"))
k=int(input("enter the position"))
if n&(1<<k):
    print("bit is set")
else:
    print("not set")
    
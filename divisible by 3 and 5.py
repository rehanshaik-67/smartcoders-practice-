n=int(input("enter the number"))
if n%3==0 and n%5==0:
    print("divisible by both")
elif n%3==0:
    print("divisible by 3")
elif n%5==0:
    print("divisible by 5")
else:
    print("neither")
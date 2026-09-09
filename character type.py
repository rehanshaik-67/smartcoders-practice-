ch=str(input("enter the charachter type:"))
if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("lowercase")
elif ch.isdigit():
    print("digit")
else:
    print("special character")

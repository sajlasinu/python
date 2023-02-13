
a=str(input("enter a string:"))
b="ing"
c="ly"
print(a)
if (a[-3:]!="ing"):
    a+b
    print(a+b)
elif(a[-3:]=="ing"):
    a+c
    print(a+c)
else:
    print(a)

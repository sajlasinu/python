num= int (input("enter the number"))
factorial=1
if num<0:
    print("sorry it does't exsist ")
elif num==0:
    print (" factorial of 0 os 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of ",num,"is",factorial)

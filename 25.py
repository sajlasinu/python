a=str(input("enter a string:"))
print(a)
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("count of all characters is ",count )

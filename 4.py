list=[]
n=int (input("Enter the number of elements :"))
for i in range(0,n):
    list.append (int(input()))
print("list is :",list)
for i in range (0,n):
    if list [i]>100:
       list [i]='over'
print("result list is :",list)

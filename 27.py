import math
n=int(input("enter the no.of word in list"))
list=[]
print("enter the words:")
for i in range(0,n):
    list.append(str(input()))
print(list)
for i in list:
    a=len(i)
    print("length of",i,"is",a)
    b=max(list)
print("length of longest word",len(b))

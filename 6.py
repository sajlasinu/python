list1=[1,2,3,4,5,6,7,8]
list2=[11,2,13,15,5,6,]
if len(list1) == len(list2):
    print("the list are of same length")
else:
    print("the length of two list is not same")
sum1=0
sum2=0
for i in list1:
    sum1=sum1+i
for i in list2:
    sum2=sum2+i
if sum1 == sum2:
    print("the list sum to same value")
else:
    print("the sum of two list is not same")
z=int(input("enter the value to be checked:"))
if z in list1:
    print("the value is present in list1")
else:
    print("the value is not present in list1")
if z in list2:
    print("the value is present in list2")
else:
    print("the value is not present in list2")

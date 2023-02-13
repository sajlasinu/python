
color1=str(input("enter a set of colours:"))
color2=str(input("enter a set of colours:"))
set1=set(color1.split())
set2=set(color2.split())
print("difference of set1",set1,"and set2",set2,"is")
print(set1.difference(set2))

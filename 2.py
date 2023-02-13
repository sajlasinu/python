list=[1,-1,5,-9,6,4,3,2,1,-7,0,-11,11,78,-10]
print(list)
for i in list:
  if (i>0):
   print(i)
list=[]
n=int(input("enter the no.of elements:"))
for i in range(0, n):
    list.append(int(input()))
print(list)
print("squares are:")
for i in list:
    print(i*i)
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
final = [each for each in string if each in vowels]
print(len(final))
print(final)
string1 = ['a','h','j','u','e']
for char in string1:
    print(char,'-',ord(char))

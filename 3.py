strings= "woodchuck how much wood would a woodchuck chuck if a woodchuck check wood ?"
strings= string.lower()
strings= string.split(" ")
word_frequency ={}
for i in strings:
      if i in word_frequency:
          word_frequency[i]+=1
      else:
          word_frequency[i]=1
print(word_frequency)

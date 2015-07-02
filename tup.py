from collections import defaultdict


user_input = input('Enter a number: ')

print (user_input)
l=range(user_input)


d=defaultdict()
k = 1
for s in l:
    d[s]=s**2
  
print d 
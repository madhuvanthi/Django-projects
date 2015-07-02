import random
def diction(n):
    x=1
    if n%3 == 0 or n%5==0 and n%15==0:
        r = {x: pow(n,3)}

    else:
        if n%3 == 0 or n%5==0:
            r = {x:random.random()}

    return r

n=int(input("Enter a number:"))
i=diction(n)
print(i)
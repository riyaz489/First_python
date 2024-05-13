# add x char in given string after every kth character
x11 = '1000000000200000000030000000004000000000500'
def addchar(a, x=' ', y=10):
    if not a:
        return  a
    index = 0
    l = len(a)

    while l> y:
        l-=y
        index+=y
        a = f'{a[:index-1]}{a[index-1]}{x}{a[index:]}'
        index+=1

    return a
print(addchar(x11),x11)





# lambda function: single line functions
# these are anoymous functions without name,no def, and no return
a = lambda x, y:  (x-y, x+y)
x, y = a(1, 2)
print(x, y)

# directly calling lambda
print((lambda x, y: x + y)(5, 3))

# lambda without return
(lambda: print('yo'))()

# recursion with lambda
x = lambda y: x(y-1) if y else y
print(x(4))


# map: to execute a function to all elements of a iterable. map return a new iterable.
s = list(map(lambda x: x**x, [1,2,3]))
print(s)

# filter: to filter out objects from iterable
# map vs filter: number of elements map will return, will be same as original list. while number of elements in
# filter can be less than the original number of elements.
# func in filter should always return bool values
print(list(filter(lambda x: x % 2, [1,2,3,4])))

# reduce: The reduce() function accepts a function and a sequence and returns a single value calculated
from functools import reduce,partial
# here output of first 2 elements will operate on third arg of list and this thing will continuesly
# go on until we get single value.
print(reduce(lambda a,b: a*b, [1,2,3]))

# zip: it will combine ith element of each list into tuple and return list of tuple.
# the number of elements zip return will be equal to the size of shortest iterable

print(list(zip([1,2,3], ['a', 'b', 'c', 'd'])))

# partial: Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
def sum(a, b,c):
    a = a+c
    print("skpping %s"%b)
    return a
new_func = partial(sum, b=3,c=6)
print(new_func(5))


## try except else finally
#
# try:
#     # some code
# except:
#     # if some error occured in try
# else:
#     # if no error occurred in try
# finally:
#     # always executed

## for else

for x in range(2):
    print(x)
else:
    # else will be executed, if for loop completed all the iteration, if for loop is breaked due to some condition then
    # else will be skipped
    print('completely executed')


for x in range(2):
    if x==1:
        break
    print(x)
else:
    # now else will not be executed
    print('completely executed')


# python first compile all the imported libraries, and if those imported lib also importing some lib
# then those one's also compiled initially, and this chain goes on, if you want to reload/reimport some lib/module
# at runtime then we can use below method

# from importlib import reload
# foo = reload(some_module)

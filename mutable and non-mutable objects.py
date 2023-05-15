# Some of the mutable data types in Python are list, dictionary, set and user-defined classes.
# On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.

class  A:
    x = 10

a = A()
y = [20]

def mutable_change(x:list):
    x.append(10)
    y.append(30)
    print(id(x))
    print(id(y))
    a.x=99

mutable_change(y)
print(y)
print(a.x)

a1 = 9
def non_mutable_change(x):
    x+=1
    print('x inside function:', str(x))
    print(id(x))
non_mutable_change(a1)
print(a1)
print(id(a1))

non_mutable_change(a.x)
print(a.x)
print(id(a.x))

# as we have notice above mutable object share same memory through out the code, so we are able to update them inside
# functions without the use of 'globals' keyword. and if we pass mutable object in function args then also it will
# not create new memory block, it will use same object, but in case of non-mutable object it will create a new.

# so we only access non-mutable outer object inside methods, but we cannot update them. to update them we need to use
# 'globals' keyword. and similarly in case of nested method we can only access outer method non-mutable object in inner function
# but we can't update them, so to update them we use 'nonlocal' keyword

# note: now in inner method we can either use outer method var or global var. but can't use both.
# and both global and nonlocal should be first line of method

# note: as we have seen above mutable types are passed by reference. so in below code intially x refers to tem1 but after
# new list assignment, it points to [1,2] list. so now if x changes it won't effect tem1
tem1 = [3]
def test(x):
    x = [1,2]
    return x

print(test(tem1))
print(tem1)


main_var = 1
def outer():
    main_var = 2
    def inner():
        # because outer method main_var is closest so it will take it's value for printing.
        print('main var',str(main_var))
    inner()
outer()

### default vars #####

# note: mutable objects as default argument share same memory throughout the program but non-mutable data types does not show similar
# behaviour, like int in below case
# if we don't want thi behaviour then either pass some value in args or assign some new object inside method for this default arg
class D():

    # mutable args
    def sum(self, x=[]):
        x.append(1)
        return x
    def update_obj(self, x=a):
        x.x+=1
        print(x.x)

    # or
    # def update_obj(x=A()):
    #     x.x+=1
    #     print(x.x)

    # non mutable default arg
    def add(self, x=1):
        x+=1
        return x


d2 = D()
print(d2.sum())
print(d2.sum([2]))
print(d2.sum())

d2.update_obj()
d2.update_obj()

print(d2.add())
print(d2.add())



# In case of for loops also, if we change the iterable inside loop it will effect the
# main element on which loop is running

# non mutable:
a = '1234'
for x in a:
    # this inner a will update upper loop variable a
    a+='5'

# mutable:
a = [1,2]
# for x in a:
#     # this will update upper a, and this loop become infinite loop
#     a.append(3)

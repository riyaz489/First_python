# like java python also has garbage collector which automatically manages memory.

# everything in python is object. so everything in python is PyObject in C behind the scenes.
# The PyObject, the grand-daddy of all objects in Python, contains only two things:
# ob_refcnt: reference count
# ob_type: pointer to another type
# The reference count is used for garbage collection.  It means that objects created in Python have a reference count
# variable that keeps track of the number of references that point to the object.
# When this count reaches zero, the memory occupied by the object is released.
import sys
a = []
sys.getrefcount(a)
# it wil give unique id of var 'a'
id(a)
# object type is just another struct that describes a Python object (such as a dict or int).

# stack
# all function calls and variables present inside it are stores on stack.
# When a function is called, it is added onto the program’s call stack.
# Any local memory assignments such as variable initializations inside the particular functions are stored temporarily
# on the function call stack, where it is deleted once the function returns.

#heap
# The variables are needed outside of method or function calls or are shared within multiple functions globally are stored in Heap memory.


# in python small strings use same memory i.e
# a = 'hi'
# b= 'hi'
# then `a is b` will result True
# but in case of large strings it will use different memory. so in case if we still want to share memory we can use
# sys.intern()
a = sys.intern('hi I am riyaz')
b = sys.intern('hi I am riyaz')
print(a is b)
# by default python uses sys.intern() in dict keys,class or instance attributes are interned.
# benefits of using intern is:
# 1. less memory is used
# 2. string comparison is faster, because now we just compare memory pointers instead of actual string comparison

## python context manager: we can properly manage resources using context-manager.
# note: this is better than try catch finally, because this is clean. funcnality wise it is simialr to try-catch-finally.
# inside exit() we can catch exception also or ignore it or raise it.

#sample code:
class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')
# On executing the with block, the following operations happen in sequence:
# __init__()
# __enter__()
# statement body (code inside the with block)
# __exit__()[the parameters in this method are used to manage exceptions]

# some best practices
# 1. don't use + with string instead using join() to add string.
# 2. instead of this `"hi"+name+"bye"` use fstring `"hi {name} bye"`
# 3.  Generators allow you to create a function that returns one item at a time rather than all the items at once.
# 4. Python accesses local variables much more efficiently than global variables

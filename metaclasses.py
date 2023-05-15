# metaclasses are classes fo classes
# type() is default meta class in python
# for eg
print(type(str))
print(type(int))
# all these classes metaclass is type class()
# but we can create our own meta class
# but first little understanding of __new__, __init__ and __call__

# __new__ new is called  during object creation
# __new__ is called before __init__, so that means we can return other class object using new, but in that case
# our current init will not be called
# it is neccessary to return object from __new__ and also new will always take cls(current class) as argument
# __init__ is just used to intialize object which is created by new
# __call__ is just used to make class object callable
# so when object is called using '()' then this method will be called

# lets see example of all of these
class Sample:
    def __new__(cls, *args, **kwargs):
        # here we can return object of other class, but in that case our current class inti will not be called
        print('__new called')
        # this is way of creating object without calling class directly
        # here cls is current class
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        # we can add attributed to current object
        print('init called ')

    def __call__(self, *args, **kwargs):
        print('call called')
        # used to make this class object callable

s= Sample()
# now __call__ will be called
s()

# we can create class using type()
# classRef = type(classname, superclasses, attributedict)
# eg
A = type("A", (), {})

# now jump to meta classes
class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        # so here we returning new class using type class __new__
        # type("A", (), {}) in background is calling __new__ of type class
        # when write type(), it will try to create type class object, due to that __new__ is called and
        # that method will return a new class with the help of specified arguments in type()
        return type.__new__(cls, clsname, superclasses, attributedict)

    def __call__(cls, *args, **kwargs):
        print('__call of meta class')
        # now we have to return object of current class
        # otherwise B() will always return None
        # if we create object here using "object.__new__(cls, *args, **kwargs)" then it will dirctly
        # create object and skip the B class init and new
        return super(LittleMeta, cls).__call__(*args, **kwargs)
class S:
    pass

# so when we define a class with given meta class
# then it will call __new__ of given meta class
# becz defining 'B' class means here creating a object of meta class
# becz now B is object of LittleMeta class
class B(S, metaclass=LittleMeta):
    def __init__(self):
        print('init called')

    def __new__(cls, *args, **kwargs):
        print('new of A')
        return object.__new__(cls, *args, **kwargs)
# now 3 functions will be called
# first call of meta class
# (becoz B class is object of littlemeta class, that means we are calling object of meta class )
# then __new__ of B then __init__ of B
a=B()


# call some other class methods through this proxy class. it will add some more funcnality to calling function just like
# decorators
class ProxyClass(object):

    def __init__(self, ob):
        self.ob = ob

    def __getattr__(self, attr):
        """ this __getattr__ will be called when, we try access method/property using this class object (ProxyClass object)
         which is not defined in this class(proxyClass )"""
        print('sdf', attr)
        # this method will pull out the specified attributes from given object
        return getattr(self.ob, attr)


class MyClass:
    we =140
    def show_msg(self, a):
        print("hello", a)


ob = MyClass()
o1 = ProxyClass(ob)
o1.show_msg(12)
print(o1.we)



# ###### create class object dynamically using string names ####
def factory(classname):
    cls = globals()[classname]
    return cls()

#(the advantage of below code is that you can refactor this factory function to any other module with no changes):

def factory(classname):
     from myproject import mymodule
     cls = getattr(mymodule, classname)
     return cls()


# significance of __name__ variable,  When you run your script, the __name__ variable equals __main__.
# When you import the containing script, it will contain the name of the script

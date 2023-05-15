#inheritence

class first:
    def __init__(self, name):
        print('first called')
        self.name= name

    def firstMethod(self):
        print("hellow first")


class paretn2:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print('parent2 called')
    def firstMethod(self):
        print ("hellow parent2")

class child1(first,paretn2):
    def __init__(self, name):
        # in case of multiple parents only first parent methods have been called if they both ave methods with same
        # name like in our case init(name) of `first` class will be called with `super().__init()__`
        # it is necessary to call init of base class if we are creating init of child class, otherwise it will
        # automatically call init of base class
        super().__init__(name)
        # note: here overloading won't work in case of multiple parents with same method name.
        # as you can see if we run super().__init__() then still it try to call init of first class not the parent2
        # class and first class init() require name arg so below code will throw error
        # super().__init__(n1, n2)
        # due to this reason multilevel inheritance is supported instead of multiple inheritance
    def firstMethod(self):
        print ("hellow child1")

class child2(first,paretn2):
    #becoz in pyhton one statement is neccessary for classes and methods
    # so in that case we will use `pass` which act as null statement, do nothing
    pass
#if we inherit from two classes(multiple inheritence)and both of the classes have some methods having same definition
#then the method will called of that class, which inherited first, like here `first` class method is called
c1 = child1('name1')
c1.firstMethod()
c2 = child2('name')
c2.firstMethod()

# calling base class method
# here also first class method is called because it inherited first
super(child1, c1).firstMethod()



# multilevel inheritance
class A:
    def h(self):
        print('A')

class B(A):
    def h(self):
        print('B')
class C(B):
    def __init__(self, c):
        self.c = c
    def h(self):
        print('C')

c= C('sd')
c.h()

# calling base class methods
super(C, c).h()
# calling parent parent class method
# Class.__base__() return new object of base class and __class__ property return current object class
super(C.__base__().__class__, c).h()


# list all methods and attributes
print(c.__dir__())
#list of base classes
print(C.__mro__)


# Note: we can also dynamically add attributes to class objects
class A:
    def pri(self):
        print(self.a)


a = A()
a.a = 'yo'
a.pri()
b = A()
# will throw error because `a` attribute is not defined yet
#b.pri()

# better practice to use slots
class D:
    __slots__ = ('a', '__dict__')

d = D()
d.a = 'a'
print(d.a)
# classes by default uses dict to store objects attributes. __slots__ are faster and consume less memory in
# comparison to dict, but it will disable the dynamic creation of attributes for an object.
# but if we want to add attirbutes to object on fly then we can add __dict__ to slots like we did above.
# by adding __dict__ to slots we loose some benefits of memory saving which we have without __dict__,
# but still we get faster response for attributes present inside slots, not for __dict__ attributes which
# are created on fly, like in our case 'a' will be fetched fast in comparison to 'b' because b will be stored in dict
d.b = 'b'
print(d.b)


# note: slots are inherited from base class, so if base class slot has 'a' attribute then no need to mention it in
# child class slot


class AbstractBase:
    __slots__ = ()
    def __init__(self, a, b):
        self.a = a
        self.b = b

# like above class we can force child classes to have a and b in their slots(it is like duck-typing)
class Foo(AbstractBase):
    __slots__ = 'a', 'b'

# so here Bar class uses __dict__, (which is default behaviour of class) due to which  'a' and 'b' is dynamically
# created.
class Bar(AbstractBase):
    pass

class Far(AbstractBase):
    __slots__ = 'a'

f = Foo(1,2)
print(f.a)
print(f.b)

b = Bar(1,2)
print(b.a)
print(b.b)

# this will throw error because Far does not have b in its slots and it can't create it dynamically also
# f = Far(1,2)
# print(f.a)
# print(f.b)
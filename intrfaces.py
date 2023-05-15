# There’s no interface keyword in Python. so python use duck-typing (dependency injection/runtime polymorphism)
# instead of inheritance, so duck typing is more
# pythonic. In duck-typing any sub class having methods required in base-class will work easily.
# for example according to duck-typing aeroplane is also a bird,
# because it can fly.also duck-typing check for issues at runtime while interface check them at compile time.
# also when we have IS-A relationship, then we should use interfaces instead of duck-typing.
# but best practice is to avoid IS-A relationship (inheritance).

# concrete class: this is a subclass which implements the interfaces in python and all its existing methods
# python interfaces are informal, i.e they are just like any other normal class, and they didn't force users to
# implements all methods of a interface.
# to make formal interfaces we have to use abc.ABCMeta package

# this method return true, if object wih specified name present in specified class
# hasattr(subclass, 'load_data_source')

# return true if specified object is callable
# callable(subclass.load_data_source)



# IS-A relationship: one class use other class methods/attributes using pure inheritance
# class A:
#     def m1(self):
#         pass
# class B(A):
#     pass
# b = B()
# b.m1()

# HAS-A relationship: one class use other class methods/attributes using object of other class
# class A:
#     def m1(self):
#         pass
# class B:
#     def m1(self, ob):
#         ob.m1()
# b = B()
# b.m1(A())


# different types of HAS-A relationship:
# 1. Association: Association is a relation between two separate classes which establishes through their Objects.
# Association can be one-to-one, one-to-many, many-to-one, many-to-many. here there is no ownership of relation.
# also both the objects exists independently, it means both of them have their own lifecycle.
# it can be unidirectional or bidirectional (unidirectional means relationship can be moved only in one direction.
# example: departments can have students but vice-versa is not possible and bidirectional means relationship can be
# from both the directions example, a person can have multiple address and an address can be used by multiple persons )
# example:
class A:
    def shw(self):
        print('m1')


class B:
    def shw(self):
        print('m2')
print(f'I am class A {A().shw()} which has {B().shw()}')


# 2. aggregation is special case of association, here also both the objects can exists independently,
# due to which many-to-many is also possible here. but here relationships can be only unidirectional.
# means one side can be owner for the relationship.
class Foo:

    def __init__(self, bar) :
       self.bar = bar

# 3. composition : it is a special type of aggregation, where one side of object can not exists without the object
# which has ownership of relation.
# for example in below code f we delete foo, bar object will also be deleted.
class Foo2:
    def __init__(self):
        self.bar = B()
# Composition is a strong Association whereas Aggregation is a weak Association
# it is also known as 'part-of' relationship.
# also one-to-one and one-to-many can exists here.

# overriding vs duck-typing (conceptual difference, functionality wise bot are same)
# 1. overriding is IS-A relationship while duck-typing is HAS-A relationship.
# both are used to achieve run time polymorphism.
# 2. overriding means a subclass can override a method of the base class. This means a method of a class can do
# different things in subclasses. For example: a class Animal can have a method talk() and the subclasses Dog and Cat
# of Animal can let the method talk() make different sounds.
# 3. Duck typing means code will simply accept any object that has a particular method. Let's say we have the
# following code: animal.quack(). If the given object animal has the method we want to call then we're good
# (no additional type requirements needed). It does not matter whether animal is actually a Duck or a different
# animal which also happens to quack. That's why it is called duck typing: if it looks like a duck
# (e.g., it has a method called quack() then we can act as if that object is a duck).

# In summary duck-typing is: as-long-as called class has methods which calling class required, then we are fine.
# example of duck-typing
class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")
    def name(self):
        print("ITS A DUCK NO NAME")


class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")

def animal(duck):
    duck.quack()
    duck.feathers()
    duck.name()


animal(Person())
animal(Duck())


# interfaces
from abc import  ABC, abstractmethod

class IRectangles(ABC):
    @property
    @abstractmethod
    def width(self):
        return

    @abstractmethod
    def area(self, x:int, y:int) -> int:
        pass

    # this hook will be called when we run isinstance or issubclass method for this interface
    # so by default if we run isinstance for its child class object with this class, it will return false.
    # so to override that behaviour we have done this
    @classmethod
    def __subclasshook__(cls, C):
        if cls is IRectangles:
            if all([
                any("area" in B.__dict__ for B in C.__mro__),
                any("width" in B.__dict__ for B in C.__mro__)
            ]):
                return True
        return False

class Square(IRectangles):
    # abc will check only for method name not for method signature
    # like below case will not throw error
    def area(self, x):
        return "jh"

    @property
    def width(self):
        return

s=Square()
print(s.area(5))

# these will return true because of subclasshook otherwise it will return false.
print(issubclass(Square, IRectangles))
print(isinstance(Square(), IRectangles))



# define argument types using typing for IDE warnings!
# 1. in case our argument can be multiple types then we can use union:-  x: Union[int, str]
# 2. in can our argument is a function/callable :- x: Callable[[arg1,arg2], return_type]
# 3. in case we don't know number of arguments in our callable then we can use  ... :- x: Callable[...,return_type]
# 4. in case argument is optional :- x: Optional[int] = None   (Optional[X] is equivalent to Union[X, None])
# 5. in case our variable can nto be overridden:- MAX_SIZE: Final = 9000
# 6. iterable of particular type:- x: Iterable[int] or x: list[int] or x: tuple[int]
# 7. for nested iterable:- x: list[int[int]]
# 8. if elements has different data-types in same axis of iterables  (example: ([1,'a'],[2,'b'])):- x: tuple[list[int,str]]


# protocols
from typing import Protocol
# protocols are used for static duck typing (means it will show warning while writing code but still throw error at runtime)
class Switchable(Protocol):
    # for empty methods we just use ... instead of pass in case of protocol class
    def turn_on(self):
        ...

    def turn_off(self):
        ...


class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan:
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    # we are defining what kind of class objects we can accepts here
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


# l = LightBulb()
f = Fan()
# so now we can pass either lightbulb or fan object in this class
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
# so in above example we are doing duck typing, inversion of control/dependency injection and using protocol to check
# if passed object is compatible to our given protocol or not, if fan does not have Switchable class methods, then
# IDe will just show warning , unlike interface it will not throw error. and when ElectricPowerSwitch class try to
# run Switchable class method , which is not present in fan class, then it will throw error at runtime, which is pythonic way
# and this behaviour is know as duck typing.
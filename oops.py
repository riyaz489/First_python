# 1.inheritance
# 2.class
# 3.objects

# 4. polymorphism: single functions behaves differently in different situations
# it can be achieved using method overloading(static binding[calling method identified at compile time])
# and method overriding(dynamic binding[calling method identified at run time]).
# for polymorphism example go to intrfaces.py script page

# 5. abstraction: Abstraction in Programming is about hiding unwanted details while showing most essential information.
# Abstraction in OOP is a process of hiding the real implementation of the method by only showing a method signature.
# In Python, we can achieve abstraction using ABC (abstraction class) or abstract method.

# 6. Encapsulation: it is a process of protecting the data and functionality of a class in a single unit, called an
# object.We can protect the variables in the class by marking them as private. we can prevent accidental modification of
# class attributes using encapsulation.so any modification is done in class privates attributes, is done by its own
# methods which called by same class objects.

# access specifiers
# In python we have public, protected and private access specifiers.
# by default all members of a class in public in python
# to make them protected we add '_' as prefix and to make them private we use '__' as prefix
# protected are accessible within class and subclass. (i.e we can't call or access them outside class
# or outiside inherited class)
# private members we can access only inside current class.
# to access or update private or protected varibales outside class we can also use getters and setters (descriptors)

class A:
    def __init__(self):
        self.__pri = 'private'
        self._pro = 'protected'
        self.pub = 'public'


    def _protected_met(self):
        print('I am '+ self._pro)


    def __private_met(self):
        print('I am '+ self.__pri)

    def public_met(self):
        print("I am "+ self.pub)

class B(A):
    def access_attr(self):
        print(self.pub)
        print(self._pro)
        # thorws error
      #  print(self.__pri)

    def access_methods(self):
        self.public_met()
        self._protected_met()
        # thorws error
     #   self.__private_met()

a= A()
a.public_met()
a._protected_met()

# throws error
#a.__private_met()

# but we can also access private members using below naming convention. best it is not a best practice to use below
# naming convention and fetch private members of class
# obj._class__private_method()
a._A__private_met()

print(a.pub)
print(a._pro)

# throws error
#print(a.__pri)


b = B()
b.access_attr()
b.access_methods()

# as you can see protected members are also accessible outside class in python and private members also with this
# naming convention `obj._class__private_member`. so in python public is only real access specifier other specifiers
# are just naming conventions.


# static members: static members share same memory throughout lifecycle of program. they belongs to class not object.

class C:
    # class attribute
    v1 = 1

    # static method, without self
    @staticmethod
    def m1():
        # note: we can not access class attributes in static method
        # below we just did a hack, we directly used class name to update class atrributes.
        # but usually we use class methods to modify class attributes
        print('yo'+str(C.v1))


# accessing static attr directly with class
print(C.v1)
# accessing static method directly with class
C.m1()
# now if we change v1 so it will be changed for all
C.v1 = 2
C.m1()

# now if we create object of C, so it will have v1 of updated value, which is 2 right now
c1 = C()
c1.m1()

# now we try to update static value at object level, but it won't work here
# it will create a new memory for v1 here. so now c1.v1 is different from C.v1
c1.v1 = 3
print(c1.v1)
c1.m1()

c2 = C()
c2.m1()

# class methods: a class method is a method which is bound to class instead of instance, just like static methods
# but here we provide `cls`(current class) as first argument.
# also these methods is used to change state of class which would then apply to all the instances of class. whereas
# static methods can't update class state, they are just utility methods.

# usually we use class methods as factory methods : Factory methods are those methods that return a class object
# (like constructor) for different use cases.

# example:
from datetime import date
class Person:
    created_from_birthyear = 'x'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.created_from_birthyear)
        # we can access class attributes here but if we try to update it using self it will create new
        # attribute at instance level, like we did below
        # self.created_from_birthyear = 1


    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        # we can't access instance attributes here
        # now this created_from_bithyear is updated for all future objects
        cls.created_from_birthyear = 2
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        # here we can't access class attributes and instance attributes here.
        # but to access class atrribute here we need to use class name
        # example: Person.created_from_birthyear

        return age > 18


person1 = Person('mayank', 21)
print(Person.created_from_birthyear)
print(person1.created_from_birthyear)
print('######')
Person.fromBirthYear('new',1998)
print('######')
person2 = Person('new mayank', 21)
print(Person.created_from_birthyear)
print(person2.created_from_birthyear)


# __main__.py file
# usually we provide file name to run python script , but if we define __main__.py inside a folder,
# then you can simply name the directory or zipfile on the command line, and it executes the __main__.py automatically
# example:
# -- projectfolder
#   -- __main__.py
#      from p1 import a
#      a()
#   -- p1.py
#       def a()
#       print('hello')
#   console-> projectfolder
#   output->  hello


# classes with single underscore prefix
# This is the official Python convention for 'internal' symbols; "from module import *" does not import
# underscore-prefixed objects.
class _Internal:
    pass
# so to override this behaviour we can use __all__ , __all__ contains list of public objects of current module,
# which is later interpreted by import  *
# example:

# in ____p1.py______
__all__ = ['_c1','c2']
class _c1:pass
class c2:pass
class c3:pass
# in ----p2.py------
# from  p1 import * -> it will import _c1 and c2 only (things inside all will be imported using *, others will be
# imported by manual import )

# from p1 import p3 -> it will import c3 class
# note: usually we write __all__ inside __init__.py file.
#
# also importing all classes/methods/objects inside __init__.py gives us shortcut to directly import
# classes/methods/objects using module name instead of writing complete file path
# example:
# from module import c2
# instead of this
# from module.p1 import c3


# Pattern		   Meaning
# 	_var	: Naming convention indicating a name is meant for internal use. Generally not enforced by the Python \
#          	  interpreter (except in wildcard imports) and meant as a hint to the programmer only.
# 	var_	: Used by convention to avoid naming conflicts with Python keywords.
# 	__var	: Triggers name mangling when used in a class context. Enforced by the Python interpreter.
# 	__var__	: Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes.
# 	_	    : Sometimes used as a name for temporary or insignificant variables (“don’t care”).
#             Also: The result of the last expression in a Python REPL.

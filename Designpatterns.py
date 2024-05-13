# declarative vs imperative:
# well in imperative appraoch we try to describe each step to achieve result, but in declarative we describe
# what we want not how we want. best practice is to use declarative approach

# Declarative
small_nums = [x for x in range(20) if x < 5]

# Imperative
small_nums = []
for i in range(20):
    if i < 5:
        small_nums.append(i)

# ####Design Patterns#####

# a. Creational design pattern: these are patterns which tells us how we can create objects.


# 1. singleton: a class can have only single object
class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_a'):
            cls._a = object.__new__(cls, *args, **kwargs)
            return cls._a
        else:
            raise PermissionError

    def prnt(self):
        print('yo!')


a1 = A()
a1.prnt()
# a2 = A()
# a2.prnt()


# 2. factory method:  allows an interface or a base-class to create an object, but let subclasses decide which class or
# object to instantiate. (just like DI using single interface we can create different class objects)
# it will be helpful, in case a new class will come in future, or we are not sure about classes we are going to
# use. So with this design pattern we don't have to modify our code just implement new class with the
# base class. we can use duck typing concept here.
# disadvantage: code become complex because new factory class will added(in below example we used method
# instead of class)

class Cl1:
    def pr(self):
        return 'c1'
class Cl2:
    def pr(self):
        return 'c2'

def Factory(language="English"):
    """Factory Method"""
    language = language.capitalize()
    # use enum or config dict here.
    localizers = {
        "Cl1": Cl1,
        "Cl2": Cl2,
    }
    return localizers[language]()
# better practice is to put these class names into a config dict or enum
c1 = Factory('cl1')
c2 = Factory('cl2')

print(c1.pr())
print(c2.pr())

# 3. Abstract factory: this design pattern is just nested factory pattern.
# we can use it in situations like, we have furniture shop and in furniture we have table and sofa and in
# table and sofa we have different categories like classic modern etc. so in that case we will use abstract factory
# instead of factory. because furniture type and furniture category is not limited.
# disadvantage too many classes

# duck typing
class Furniture:
    def __init__(self, ob):
        self.ob = ob
    def create_table(self):
        return self.ob.create_table()
    def create_sofa(self):
        return self.ob.create_sofa()

class Modern():
    def create_table(self):
        return ModernTable()

    def create_sofa(self):
        return ModernSofa()

class Classic():
    def create_table(self):
        return ClassicTable()

    def create_sofa(self):
        return ClassicSofa()

#  it is interface
class Table:

    def p1(self):
        pass
#  it is interface
class Sofa:
    def p2(self):
        pass

class ModernSofa(Sofa):
    def p2(self):
        print('modenr sofa')

class ClassicSofa(Sofa):
    def p2(self):
        print('classic sofa')

class ClassicTable(Table):
    def pr1(self):
        print('classic table')

class ModernTable(Table):
    def pr1(self):
        print('modenr table')


mf = Furniture(Modern())
mf.create_sofa().p2()
cf = Furniture(Classic())
cf.create_table().pr1()

# 4. Builder: if our class has too many arguments in constructor, so to avoid that kind of issue we can use builder class
# lets take example of Animal class, we can create multiple varieties of animals using animal class,
# due to this reason it's constructor will be big and few of the animal object will not use those constructor arguments.
# like animals who does not have tail will not assign tail value.
# In builder pattern we build an object step by step. but in factory we crate object in one go.
# here we create different builder classes to build different kinds of objects and hide it behind the
# main Builder(base abstract class) class.
# this design pattern provides abstraction .
# instead of this design pattern we could have used properties, but with properties our lines of code will be increased.
# also we can't use method chaining like below. also properties main task is control accessing and setting of value.
# but here we just want to control the setting part.

# example without abstraction
class Car:

    def __init__(self, brand):
        self.brand = brand
    # to avoid ugly constructor we created below methods for optional things
    # below methods can be replaced by properties
    def set_name(self, name):
        self.name = name


    def set_price(self, price):
        self.price= price

c = Car('bmw')
c.set_name('test')


# example with abstraction
class Vehicle:
    def __init__(self, vehicle_builder):
        self.__vehicle = vehicle_builder
        self.__allowed_attr = ['name','tyre','lights']

    def __getattr__(self, item):
        if item in self.__allowed_attr:
            x = getattr(self.__vehicle,item)
            if not hasattr(x,'__call__'):
                return x

    def add_tyre(self):
        self.__vehicle.add_tyre()
        return self
    def add_name(self,x):
        self.__vehicle.add_name(x)
        return self
    def add_lights(self,x):
        self.__vehicle.add_lights(x)
        return self

class fourwheeler:
    def __init__(self):
        self.tyre = None
        self.name = None
        self.lights = None
    def add_tyre(self):
        self.tyre = 4
    def add_name(self, x):
        self.name = x
    def add_lights(self,x):
        self.lights = self.lights +x if self.lights else x
    def private_dummy(self):
        print('inside private dummy')
class twowhheler:
    def __init__(self):
        self.tyre = None
        self.name = None
        self.lights = None
    def add_name(self, x):
        self.name = x
    def add_tyre(self):
        self.tyre = 2
    def add_lights(self,x):
        self.lights = self.lights +x if self.lights else x


v1 = Vehicle(fourwheeler())
v1.add_lights(2).add_lights(2).add_name('bmw')
print(v1.name, v1.tyre, v1.lights)
v2 = Vehicle(twowhheler())
v2.add_tyre().add_lights(1).add_name('vespa')
print(v2.name, v2.tyre,v2.lights,)

v1._Vehicle__vehicle.private_dummy()
v1.private_dummy()


# 5. prototype: this design pattern is just used to copy big objects. so here basically we can just use
# python deep/shallow copy functions to copy objects.


# b. structural design patterns: these patterns explains how to assemble objects and classes into large structures
# while keeping these structures flexible and efficient.
# The structural design patterns simplifies the structure by identifying the relationships.
# These patterns focus on, how the classes inherit from each other and how they are composed from other classes.

# 1. Adapter: it is used in scenarios like we have a third party lib which is not compatible with our code
# so instead of updating lib code,  we introduce a adapter class between third party lib and our our code.
# for example a we have json data cleaning code, but we are using some third party lib to read json data. but that
# third party lib can only read xml data, so in that case we introduce adapter class which convert json to xml for
# 3rd party lib and do xml to json for our code.
# in facade we are trying to take care more than one complicated steps , basically we write simple functions to
# to hide complex implementation of given functions or lib where as in adapter we respect particualr lib and try to
# make it compatible with our code.

# example:
# original third party method, can operate on int numbers only
class MathsOper:
    def add_num(self, x, y):
        return x + y


class Adapter:
    def __init__(self, maths: MathsOper):
        self.__maths = maths

    def add_num(self, x, y):
        x = int(x)
        y = int(y)
        return self.__maths.add_num(x, y)


# client code
# but client has numbers in string form, but 3rd part lib works only on integers
a = Adapter(MathsOper())
z = a.add_num('1', '2')
print(z)

# 2. bridge: we can use it with builder and abstract factory also.
#   The Bridge pattern lets you split the monolithic class into several class hierarchies.
# example:  if the class can work with various database servers.
# it deals with Cartesian product problem, that is if we have vehicles class and passengers class.
# so for each vehicle and passenger pair we need to to create a new class. so to avoid this we create 2 abstract
# classes (create class with actual implementation of these abstract classes as well)
# and then pass one of the class object in others init for further use(which works as bridge).
# so instead of is-A is it will be HAS-A relationship of passenger with vehicle
# because we are using  second class functions inside first one, using second class object
#exmaple:
# Passenger & Cargo Carriers

class Carrier:
    def carry_military(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries ", items, " military cargo goods")



class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ", passengers, " military passengers")



# Military & Commercial Planes
class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier

    def display_description(self):
        pass



class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)


class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)


cargo = Cargo()
passenger = Passenger()

# Bridging Military and Cargo classes
military1 = Military(cargo , 100)
military1.display_description()
military1.add_objects(25)
military1.display_description()

# 3. composite: consider if we have to write code to access files inside folders, in this case we have to create so many
# classes also call each class object one by on to reach there. instead we can use tree structure to solve this problem.
# composite describes a group of objects that are treated the same way as a single instance of the same type of object.
# here we have 2 elements:
# 1. Component: this interface describes operations that are common to both simple and complex elements of the tree.
# 2. leaf: The Leaf is a basic element of a tree that doesn’t have sub-elements.
# Usually, leaf components end up doing most of the real work, since they don’t have anyone to delegate the work to.

# so basically this design pattern is just implementation of tree structure using loops/recursion.
# example:


class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end ="")
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end ="")
            child.showDetails()


if __name__ == "__main__":

	topLevelMenu = CompositeElement("GeneralManager")
	subMenuItem1 = CompositeElement("Manager1")
	subMenuItem2 = CompositeElement("Manager2")
	subMenuItem11 = LeafElement("Developer11")
	subMenuItem12 = LeafElement("Developer12")
	subMenuItem21 = LeafElement("Developer21")
	subMenuItem22 = LeafElement("Developer22")
	subMenuItem1.add(subMenuItem11)
	subMenuItem1.add(subMenuItem12)
	subMenuItem2.add(subMenuItem22)
	subMenuItem2.add(subMenuItem22)

	topLevelMenu.add(subMenuItem1)
	topLevelMenu.add(subMenuItem2)
	topLevelMenu.showDetails()

# 4. decorator: it's same like python decorators, but here we deal with class level instead of method/function level
# which can be achieved by aggregation.
# note: we don't have decorators for classes in python so we simply use aggregation relationship to achieve same.
# example:

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def process(self):
        print("I am add process")
        return self.a + self.b


class Multiply:
    def __init__(self, decorated, num):
        self.decorated = decorated
        self.num = num

    def process(self):
        print("I am multiply process")
        return self.decorated.process() * self.num


add_object = Add(1, 4)
multiply_add_object = Multiply(add_object, 4)
print(multiply_add_object.process())

# 5. facade design pattern: Having a facade is handy when you need to integrate your app with a sophisticated library
# that has dozens of features, but you just need a tiny bit of its functionality.
# here also we uses multiple classes to create single class or method, which is actually going to be useful for us.
# example:
"""Facade pattern with an example of WashingMachine"""

class Washing:
	'''Subsystem # 1'''

	def wash(self):
		print("Washing...")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("Rinsing...")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Spinning...")


class WashingMachine:
	'''Facade'''

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	washingMachine = WashingMachine()
	washingMachine.startWashing()


# 6. flyweight: here we try to remove same data from current class object and put it into some shared class
# so that object size will decrease, and we can run our code in low ram.
# So here we store intrinsic properties in flyweight object
# here we have 2 kind os data:
#
# intrinsic: the constant data of an object is usually called the intrinsic state. other objects can only read it,
# not change it. instrinsic is duplicate and immutable data while extrinsic is unique
# .
# extrinsic: The object state which, often altered “from the outside” by other objects, is called the extrinsic state.
#

# here we might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time
# somebody calls a flyweight method.

# example:
# here we create a arrow factory to create arrow objects and store shared data and all arrow objects
# if u notice in below code we are doing one more thing here, we are not storing duplicate objects.


# the actual class
# class Arrow:
#     def __init__(self, x, y, z, velocity):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.velocity = velocity
#         self.shape = 'cone'


class ArrowContext:
    def __init__(self, x, y, z, velocity):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = velocity


class ArrowFlyweight:
    def __init__(self):
        self.shape = 'cone'
        self.arrows = []

    def arrow_factory(self, x, y, z, velocity):
        arr = []
        for b in self.arrows:
            if b.x == x and b.y == y and b.z == z and b.velocity == velocity:
                arr.append(b)
        if not arr:
            arr = ArrowContext(x, y, z, velocity)
            self.arrows.append(arr)
        else:
            arr = arr[0]

        return arr

    def print_arrows(self):
        print('Arrows:')
        for arrow in self.arrows:
            print(str(arrow.x) + ' ' + str(arrow.y) + ' ' + str(arrow.z) + ' ' + str(arrow.velocity))

obj = ArrowFlyweight()

obj.arrow_factory(1, 1, 1, 1)
obj.arrow_factory(1, 2, 5, 1)
obj.arrow_factory(1, 1, 1, 1)
obj.print_arrows()


# 7. proxy: it's lke middleware. it allows something before or after the requests gets through the original object.
# it's implementation is similar to decorator design pattern.
# A Decorator requires an instance of the interface it is wrapping, while a Proxy does not require such an instance.
# A Proxy can receive an instance, but is also allowed to create this instance itself(ie we can create original class
# object inside proxy class itself).

# example:
class proxy:
    def __init__(self, original_object):
        self._orginal_object = original_object
    def request(self):
        print('proxy started')
        # we can make it generic by dynamically calling function by using get_attr dunder.
        # like below instead of calling request manually
        self._orginal_object.request()
        print('proxy ended')

class Original:
    def request(self):
        print('original request')

p = proxy(Original())
p.request()


# 8. plugin: At its core, a plugin architecture consists of two components: a core system and plug-in modules.
# The main key design here is to allow adding additional features that are called plugins modules to our core system,
# providing extensibility, flexibility, and isolation to our application features.
# so basically core system is generic type of code, which can easily accepts new plugins without any code modification.
# to make it more flexible we can read, plugins list from some external json file.
# for any new plugin simply add import path to json file.
# example:
import importlib

class MyApplication:
    # We are going to receive a list of plugins as parameter
    def __init__(self, plugins:list=[]):
        # Checking if plugin were sent
        if plugins != []:
            # create a list of plugins
            self._plugins = [
                importlib.import_module(plugin,".").Plugin() for plugin in plugins
            ]
        else:
            # If no plugin were set we use our default
            self._plugins = [importlib.import_module('default',".").Plugin()]


    def run(self):
        print("Starting my application")
        print("-" * 10)
        print("This is my core system")

        # Modified for in order to call process method
        for plugin in self._plugins:
            plugin.process(5,3)

        print("-" * 10)
        print("Ending my application")
        print()

# c behavioural design pattern: these are more concerned about object communication.
# 1. chain of responsibility: here we call different methods in chain.
# In this pattern, an object is passed to a Successor, and depending on some kind of logic, will or won’t be passed
# onto another successor and processed. we can implement it's code like linked list using recursion.
# it will be useful when  the set of handlers and their order are supposed to change at runtime.
# example:

class Creature:
    def __init__(self, name, attack, defence):
           self.name = name
           self.attack = attack
           self.defence = defence



class CreatureModifier:



    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier = None


    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttack(CreatureModifier):
    """Concrete Handlers"""
    def handle(self):
        print(f'Doubling {self.creature.name}\'s attack.')
        self.creature.attack *= 2
        super().handle()
class DoubleDefence(CreatureModifier):
    """Concrete Handlers"""
    def handle(self):
        print(f'Doubling {self.creature.name}\'s defence.')
        self.creature.defence *= 2
        super().handle()


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    """root is the client """
    root = CreatureModifier(goblin)

    root.add_modifier(DoubleAttack(goblin))
    root.add_modifier(DoubleDefence(goblin))

    root.handle()
    print(goblin)

# 2. command: The Command Design Pattern allows us to encapsulate and record the action that can
# be performed on an entity in a system. So here instead of directly sending request to receiver, we will send all
# the request to command class, then receiver will fetch request from command class objects.
# In this design pattern, client creates a command object that includes a list of commands to be executed.
# it will be useful if we  want to queue operations, schedule their execution, or execute them remotely.
# or we want to undo or record certain operations or we can use it when we have similar commands for different classes.
# here receiver interface will contain all command methods then our actual command classes will implement it.
# then we will be having command class for each command which takes receiver object as argument and calls receiver
# command function. and invoker class will register commands and call execute function, which eventually calls,
# commands classes execute which then calls receiver class sepecifc method.


# example:
from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    In these classes we can record history of executed commands or we can do other extra stuff before sending
    request to original method
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    In this class we set commands
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()

# 3.Iterator: Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing
# its underlying representation (list, stack, tree, etc.). So main purpose is to create a iterable traversal function
# which is used by client, and we should be able to easily change backend data-structure without changing client code.
# means all the different data-strucuture should implement similar interface for data traversal.
# in python we can easily do it using __iter__ and __next__ dunder methods. and class we can make iterable using these.
# and list, dict ,set, etc already implement these.

# 4. mediator: The pattern restricts direct communications between the objects and forces them to collaborate
# only via a mediator object. we should use this in case we have class which we can reuse after some modification but
# unable to do it, because other classes are tightly coupled with it. so in that case, other dependent classes will
# communicate with mediator instead of original one, so that we can easily modify original class. and others
# class can also use it as long as they support mediator class object.
# drawback of mediator, it will lead to god class.
# it basically restrict 2 low level objects communication directly.where commands restrict direct high level client
# to low level object communication.

# in facade we combine different methods and objects to provide simple interface to client code, so on the basis of
# request facades decides which methods to call. but in case mediator we are not changing functionality,
# client code still tries to call original methods, but only difference is it will go thorough mediator class first
# The facade is like the only door for the clients who call from outside.
# Is a dependence for other classes outside my package. On the other hand, the mediator is like the post office to which
# all people give mail in order not to go to every house they need to send a mail. Is a dependence for all the classes
# in the set, but is the only dependence.

# example:


class Mediator:
    "The Mediator Concrete Class"
    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()
    def colleague1_method(self):
        return self.colleague1.colleague1_method()
    def colleague2_method(self):
        return self.colleague2.colleague2_method()

class Colleague1:
    "This Colleague calls the other Colleague via the Mediator"
    def colleague1_method(self):
        return "Here is the Colleague1 specific data you asked for"

class Colleague2:

    def colleague2_method(self):
        return "Here is the Colleague2 specific data you asked for"

# This Client is either Colleague1 or Colleague2
# This Colleague will instantiate a Mediator, rather than calling
# the other Colleague directly.
MEDIATOR = Mediator()
# If I am Colleague1, I want some data from Colleague2
DATA = MEDIATOR.colleague2_method()
print(f"COLLEAGUE1 <--> {DATA}")
# If I am Colleague2, I want some data from Colleague1
DATA = MEDIATOR.colleague1_method()
print(f"COLLEAGUE2 <--> {DATA}")

# 5. monento: this design pattern that lets you save and restore the previous state of an object without revealing the
# details of its implementation.
# so here, instead of other objects trying to copy the editor’s state from the “outside,” the editor class
# itself can make the snapshot since it has full access to its own state.
# The pattern suggests storing the copy of the object’s state in a special object called memento. The contents of the
# memento aren’t accessible to any other object except the one that produced it
# it has 3 components:
# Originator: The originator is an object with an internal state that changes on occasion.
# Caretaker: (Guardian) this class helps to create and restores snapshots using data stored in momento class
# Memento: where we going to store states of original class object.

#  in command pattern we re-execute commands in the same order that changed attributes of a state,
#  and with the Memento, you completely replace the state by retrieving from a cache/store.
# also we store states occasionally to save ram.

# example:

class Memento():
    def __init__(self, state):
        self.state = state


class Originator():
    def __init__(self):
        self._state = ""

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        self._state = state

    @property
    def memento(self):
        print("Originator: Providing Memento of state to caretaker.")
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state
        print(
            f"Originator: State after restoring from Memento: "
            f"`{self._state}`")


class CareTaker():
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        print("CareTaker: Getting a copy of Originators current state")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        print("CareTaker: Restoring Originators state from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento


# The Client
ORIGINATOR = Originator()
CARETAKER = CareTaker(ORIGINATOR)
# originators state can change periodically due to application events
ORIGINATOR.state = "State #1"
ORIGINATOR.state = "State #2"
# lets backup the originators
CARETAKER.create()
# more changes, and then another backup
ORIGINATOR.state = "State #3"
CARETAKER.create()
# more changes
ORIGINATOR.state = "State #4"
print(ORIGINATOR.state)
# restore from first backup
CARETAKER.restore(0)
print(ORIGINATOR.state)
# restore from second backup
CARETAKER.restore(1)
print(ORIGINATOR.state)


# 6. observer: it let us define a subscription mechanism to notify multiple objects about any events that happen to the
# object they’re observing.
# The object that has some interesting state is often called subject, but since it’s also going to notify other
# objects about the changes to its state, we’ll call it publisher. All other objects that want to track changes to
# the publisher’s state are called subscribers.
# we can use this pattern when, we want to change multiple objects states using some event/or some single object
# state change.

#  mediator and observer seems similar, if we dynamically add dependent classes to mediator class, in this case,
#  mediator object plays the role of publisher, and the components act as subscribers.
#  but we can also permanently link all the components to the same mediator object.
#  so this implementation won’t resemble Observer but will still be an instance of the Mediator pattern.


# example:

class Subject:
    "The Subject (Observable)"
    def __init__(self):
        self._observers = set()
    def subscribe(self, observer):
        self._observers.add(observer)
    def unsubscribe(self, observer):
        self._observers.remove(observer)
    def notify(self, *args):
        for observer in self._observers:
            observer.notify(self, *args)

class Observer:
    def __init__(self, observable):
        observable.subscribe(self)
    def notify(self, observable, *args):
        print(f"Observer 1  id:{id(self)} received {args}")

class Observer2:

    def notify(self, observable, *args):
        print(f"Observer 2 id:{id(self)} received {args}")
# The Client
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)
SUBJECT.notify("First Notification", [1, 2, 3])
SUBJECT.unsubscribe(OBSERVER_B)
SUBJECT.subscribe(Observer2())
SUBJECT.notify("Second Notification", {"A": 1, "B": 2, "C": 3})

# 7. state: usually in finite state machines, we have fixed and same function behave differently on different state.
# and these State machines are usually implemented with lots of conditional operators (if or switch).
# which is hard to maintain. like lock button in smart phone, when phone unlocked same button will lock the phone,
# and if phone locked then same button is used to unlock the phone.
# so here instead of implementing all behaviour in same class code like below:
# def publish():
#     switch(state):
#         "draft":state = "moderation"
#                 break
#         "moderation":
#                 if (currentUser.role == 'admin')
#                 state = "published"
#                 break
#         "published":
#                 // Do nothing
# so instead of doing like above we create new classes for all possible states and implement main logic for statewise
# operations there, like draft create a new class and define draft logic there similar for other states.
# and finally create a common class which client code will call, which also contain only reference of these states classes
# so on the basis of requirements client will simply change the state object into this main class to get different
# functionality in same method.
# implementation is same like other designpatterns, we just introduced DI here, instead of calling main class directly.
# Bridge, State, Strategy (and to some degree Adapter) have very similar structures.
# Indeed, all of these patterns are based on composition, which is delegating work to other objects.
# However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way.
# It can also communicate to other developers the problem the pattern solves.

# this design-pattern can be used when we have :
# a. when we have object who behaves differently on different state.
# b. when class is polluted with massive if-else
# c. lot of duplicate code between different states. which can be merged into some common class.

# exmaple:
from typing import Protocol, Optional


class AlertState(Protocol):

    def alert(self) -> None:
        ...


class AlertStateContext:
    def __init__(self, state: Optional[AlertState] = None):
        if state is None:
            # setting default state to vibration
            self.state = Vibration()
        else:
            self.state = state

    def change_state(self, state: AlertState):
        self.state = state

    def alert(self):
        self.state.alert()


class Vibration:
    def alert(self):
        print("it's in vibration mode")


class Silent:
    def alert(self):
        print("it's in silent mode")


alert_state = AlertStateContext()
alert_state.alert()
alert_state.change_state(Silent())
alert_state.alert()

# 8. Strategy
# this deign pattern let us define a family of algorithms to solve similar problem,
# put each of them into a separate class.
# Strategy usually describes different ways of doing the same thing, letting you swap
# these algorithms within a single context class.
# then we can easily change strategy at runtime using context class.
# let's take example of google maps, there are multile ways to calculate route, for walk,
# it's different algo, for car, it's different algo for bike it's different. so instead
# of writing all these methods in single class(to avoid creating a large class), we will crete different
# classes for these different ways and then pass it's object to main class to execute these different algos.

class StringOps:
    def addition(self, a, b):
        return a + " " +b

class NumberOps:
    def addition(self, a, b):
        return a+b

class Context:
    def __init__(self, strategy):
        self.s = strategy

    def some_business_logic(self, a,b):
        return self.s.addition(a,b)

num_ops = NumberOps()
str_ops = StringOps()

c = Context(num_ops)
print(c.some_business_logic(1,2))
c.s = str_ops
print(c.some_business_logic('1','2'))

# 9. template :
# This pattern allow us to define the skeleton of an algo inside base class.
# and let some subclasses override some specific methods of the base class without changing it's structure. So this case
# is inheritance instead of composition. here we are trying to reduce code duplicates.
# Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm,
# but not the whole algorithm or its structure.
# so that in future if algo changes we don;t have to change in every class.
# let say earlier we have 2 different classes to parse excel and sv, but later we noticed, most of the steps/methods
# were same, so we move common part to base class and then create different
# child classes which contains different steps.

from abc import ABC, abstractmethod
from typing import List


class TradingBot(ABC):

    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

    # in our case this is the template methods, which contains actual algo and call others methods
    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")
        # this is a hook,by default it will no do anything, but child class can override it and performs something extra
        self.finalize_app()

    # so these required methods are abstract methods, these methods child classes has to implement
    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

    #  In our case finalize_app is hook method. hook methods means, Subclasses may override them, but it's not mandatory
    #    since the hooks already have default implementation.Hooks
    #   provide additional extension points in some crucial places of the algorithm.
    def finalize_app(self) -> float:
        pass

class AverageTrader(TradingBot):

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)

    def finalize_app(self):
        print('done with trading !!')


application = MinMaxTrader()
application.check_prices("BTC/USD")


# 10. Visitor:
# It is used when we have to perform an operation on a group of similar kind of Objects.
# with the help of visitor pattern we can move some operation logic from the objects to another class.
# let's take example of shopping cart, for each kind of item we have different class, where we store each item related
# info and have methods to perform operations on that particular item, now let say we want to create separate excel for
# item, easier way would be create a method inside each item class to generate excel with it's data.
# but there are 2 disadvantages, first generating excel method looks alien their as it has completely different
# functionality, second thing is in future if our excel algo changed then we hav to do modification in multiple classes.
# to avoid that we put this excel method in different class. so now our item class will indirectly call this export
# excel class methods with it's object to generate excels.(you place the new behavior into a separate class called
# visitor, instead of trying to integrate it into existing classes. The original object that had to perform the behavior
# is now passed to one of the visitor’s methods as an argument, providing the method access to all necessary data
# contained within the object)




from typing import Protocol

# here we will define the methods for all objects possible, like in our case it is fruit and book
class Visitor(Protocol):
    def visit_fruits(self,data):
        ...
    def visit_books(self, data):
        ...

class Fruits:
    def   __init__(self, cost,  isbn, name):

        self.price = cost
        self.weight = isbn
        self.name = name

    def  getPrice(self):
        return self.price

    def getWeight(self):

        return self.weight

    # this method calls external visitor methods and  decides what data we can pass to visitors, we can pass whole object
    # or we can pass only few attributes also.
    def accept(self,visitor:Visitor):
        # to pass only few attributes we can create a deep copy and remove few attributes which we don't want to pass
        # or we can create new object with few attributes which we want to pass
        return visitor.visit_fruits(self)

class Books:

    def __init__(self, cost, isbn,name):
        self.price = cost
        self.isbnNumber = isbn
        self.name =  name

    def getPrice(self):
        return self.price

    def getIsbnNumber(self):
        return self.isbnNumber

    def accept(self,visitor: Visitor):
        return visitor.visit_books(self)

# fetch cost from main classes objects
class Visitor1:
    def visit_fruits(self,data):
        cost = data.weight*data.price
        print('fruit visited')
        return cost
    def visit_books(self, data):
        cost = data.price * (50 if data.isbnNumber==10 else 100)
        print('book visited')
        return cost

# fetch names from main classes objects
class Visitor2:
    def visit_fruits(self,data:Fruits):
        name = data.name
        print('fruit visited')
        return name
    def visit_books(self, data:Books):
        name = data.name
        print('book visited')
        return name

items_in_cart = [Books(11,150,'b1'),Books(16,10,'b2'),Books(11,150,'b3'),Fruits(50,34,'f1') ]
visit_names = [x.accept(Visitor2()) for x in items_in_cart ]
visit_cost = [x.accept(Visitor1()) for x in items_in_cart ]

print(visit_names)
print(visit_cost)

# SOLID principles: these are 5 principles which help to write manageable, understandable, scalable code
# reduce the frequency with which we need to change our classes

# 1. single Responsibility: each class should have single responsibility. it should not perform multiple jobs
# example: let suppose we have single class which performs DB operations and also it run some business logic code
# to manipulate db data and present it to in front of user. so here single class doing multiple operations, like
# db operations and manipulation of db data. to avoid that we create 2 separate classes, one handles db operations and
# another one handles business logic.(like service and repo layer).
# it helps us to avoid creation of god object  (In short a God Object or God Class is a data structure that does
#  too many things and knows too much).


# 2. open and close: it means a class should open of extension but close but modifications.
# example: let suppose we write a class to calculate discounts of different customers. and in future new customer type
# come, In that case we have to modify the discount method of the class. to avoid that we will create a new class
# specific for each customer and inherit the original class and override the discount method in this new classes.
# like below
class Discount:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   def get_discount(self):
       """A discount method"""
       return self.price * 0.2
class VIPDiscount(Discount):
   """Demo VIP customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2

# 3. Liskov Substitution Principle: according to this principle object of base class should be replacable
# with object of child class. In simple terms if a class B inherits Class A, then class B should be able to use
# all methods defined in class A. for example we have a class vehicle in which we have two methods get_speed
# and get_engine. now let say a cycle class inherits vehicle class. so it will violate Liskov principle, because
# cycle class never be able to use get_engine method of base class. so to avoid that we create 2 new classes
# `WithEngine` and `WithoutEngine`. and these 2 classes base class is Vehicle and we remove engine specific methods
# from vehivle class and put it inside WithEngine class and now cycle will inherit WithoutEngine class.
class Vehicle:
   """A demo Vehicle class"""
   def __init__(self, name: str, speed: float):
       self.speed = speed
   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"
class VehicleWithoutEngine(Vehicle):
   """A demo Vehicle without engine class"""
   def start_moving(self):
      """Moving"""
      raise NotImplemented
class VehicleWithEngine(Vehicle):
   """A demo Vehicle engine class"""
   def engine(self):
      """A vehicle engine"""
      pass
   def start_engine(self):
      """A vehicle engine start"""
      self.engine()
class Car(VehicleWithEngine):
   """A demo Car Vehicle class"""
   def start_engine(self):
       pass
class Bicycle(VehicleWithoutEngine):
   """A demo Bicycle Vehicle class"""
   def start_moving(self):
       pass

# 4. Interface Segregation: It is same as liskov, but here we talk about interfaces
# according to this principle "A client should not be forced to implement an interface that it does not use”
# example
class Shape:
   """A demo shape class"""
   def draw_circle(self):
       """Draw a circle"""
       raise NotImplemented
   def draw_square(self):
       """ Draw a square"""
       raise NotImplemented
class Circle(Shape):
    """A demo circle class"""
    def draw_circle(self):
       """Draw a circle"""
       pass
    def draw_square(self):
       """ Draw a square"""
       pass

# so here ypu can see, we unnecessarily implementing draw_square() method in Circle class.
# so here we can create a single draw() method in Shape class, instead of writing 2 methods.
# so that any class in future(like square, rectangle, etc) can write its code in draw() according to its dimensions

# 5. dependency injection: Here we introduce abstractions(interface) in between of lower and higher level classes
# so that our higher level class will not depend on lower level classes.
# so now higher class use abstractions instead of directly calling lower level classes.

class NewsPerson:
    """This is a high-level module"""
    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(NewsPaper().publish(news=news))
class NewsPaper:
    """This is a low-level module"""
    @staticmethod
    def publish(news: str) -> None:
        """
        :param news:
        :return:
        """
        print(f"{news} Hello newspaper")
person = NewsPerson()
print(person.publish("News Paper"))
# so in above class we are directly calling newspaper class publish method
# to remove this dependency we used duck-typing and modified code below.

class NewsPerson:
   """This is a high-level module"""
   @staticmethod
   def publish(news: str, publisher=None) -> None:
       print(publisher.publish(news=news))
class NewsPaper:
   """This is a low-level module"""
   @staticmethod
   def publish(news: str) -> None:
       print("{} news paper".format(news))
class Facebook:
   """This is a low-level module"""
   @staticmethod
   def publish(news: str) -> None:
       print(f"{news} - share this post on {news}")
person = NewsPerson()
person.publish("hello", NewsPaper())
person.publish("facebook", Facebook())

# so in above example we achieve DI using Duck-typing. so any class has publish() method
# can be used by Newsperson publish(). if we pass any object which does not have publish method, into
# NewsPerson class publish() then it will throw error at runtime. so in duck-typing we are blindly trusting.
# that's why we always use try catch with it.


# principle of least astonashing: don't surprise user, give them experience what they have expected. for example
# usually close button is at top right corner of a window, but if some developer changed it, then user will waste time
# to find it. also name methods according to their funcnalites (like in descriptive manner). in python we say this code
# is pythonic code which follow POLA. for example code which follow proper python naming convention and instead of
# looping on indexes using range, directly iterate over elements which is python actual for-loop.


# YAGNI principle ("You Aren't Gonna Need It"): here we add a feature only when it is needed. The principle helps
# developers avoid wasted effort on features that are assumed to be needed at some point.
# The idea is that this assumption often ends up being incorrect.

# DRY (Do not repeat yourself): let say if you have repeated same code and logic again and again. then in future if
# you need to change the logic, then you have to do modification at all places. so to avoid that we write small and
# reusaable methods.

# KISS keep it simple stupid: we write descrptive code with small methods with single usecase, so that we can easily
# undestand code and find bugs.

# Separation of Concerns (SoC): Separation of Concerns Principle partition a complicated application into different
# sections or domains. good example is mvc code is divided into model, view and controller sections.



# So as we discussed above we can simply acheive DI in python using duck-typing,
# no interface and other third party lib and interface needed to acheive same,
# becase python is dynamically types language unlike java or C#, but if we don't use interfaces at the same time
# it can move compile time errors to run-time so to avoid that we can use protocol, which we discussed in interface.py
# So in C# DI using unity will look like this:

# static void Main(string[] args){
#  UnityContainer IU = nw UnityContainer();
# // creating a unity contianer

# IU.RegisterType<BL>();
# IU.RegisterType<DL>();
# // registered all class types we are going to use

# IU.RegisterType<IProduct, DL>();
# // passing class which is going to replace our Iproduct interface

# BL objDL = IU.Resolve<BL>();
# // using Resolve method we can get new class object which replaced our interface above
# objDL.Insert();
# calling BL class insert which will use DL class insert behind the scenes
#}
# // note for above code DL class implements Iproduct interface and
# // BL class constructor accepts Iproduct type object, code is below for this class
# public class BL{
# public BL(IProduct obj){
# _obj = obj;}
# publc void Insert(){
# _obj.Insertdata();
# which is a method of DL class and Iproduct interface
# }
# }


# you may be wondering we could have passed DL class object directly by casting it to Iproduct type like below:
# Iproduct t1 = new DL();
# BL objDL = new BL(t1);

# but DI framesworks like unity helps us to make this DI configurable outside the code.
# we can simply replace these libs/classes at one place, while testing or for lower env.
# but in python to make it configurable, by simply passing class reference in env congif files
# like in case of Django in settings.py file we can create a section of DI and pass all third_party or facade class
# refs there, and in code instead of importing these libs or facades we can simply fetch class from
# our configs. and while testing we can simply mock these class at one place or replace it with some other class
# while migrating to some other lib also we can simply create new facade and replace new facade class in settings.py

# in settings
# from google import Google
# login_service_class = Google

# base class/function which going to be used in our code directly for loose coupling
# def login(obj):
#    obj.login()
#    return obj.get_user_details()

# in our code
# from Django  import setting/config
# from uour_base_file import login
# user = login(setting/config['login_service_class']())
# print(user)

# note: above writen code is just psuedo code, import and libs des not exists, so please change it before using it

# Functional programming (often abbreviated FP) is the process of building software by composing pure functions,
# avoiding shared state, mutable data, and side-effects. here we can pass function as argument, return functions, etc
# to fulfil our needs.
# it declarative approach and OOPs is imperative approach.

# A) pure functions has 3 properties:
# 1. Pure :  they have no side-effects i.e. they do modify any argument or
# global variables or print something or modify any outside file contents or make any network request or
# Triggering any external process or Calling any other functions with side-effects.
# they can *only* do some transformations on the input and return some value.

# 2. Total: returns values for all inputs. Functions that crash or throw exceptions on some inputs are not total
# or partial. For example a div function: type declaration promises that it takes an Int and returns an Int
# however if the second argument is 0 it will throw ‘division by zero’ exception, hence it’s not total.

# 3. Deterministic: returns the same result for the same input. For deterministic function it does not matter how and
# when it’s called — it will always return the same value. Functions that depend on a current date,
# clock, timezone or some external state are not deterministic.



# Just an example
import datetime


def is_positive(number: int) -> bool:
    if number == 0:
        raise Exception("meh")  # Partial (non total)
    else:
        print("Calling isPositive!")  # Impure (writing to std out is a side effect)

    if int(datetime.datetime.now().second % 2 == 0):  # Non deterministic
        return number > 0
    else:
        return number < 0


print(is_positive(3))

# note: pure function + immutable data = referential transparency
# example: square(2) can be replaced by 4, because square of 2 always return 4.
# if a function consistently yields the same result for the same input, it is referentially transparent.

# B) Shared state is any variable, object, or memory space that exists in a shared scope(critical section), or as
# the property of an object being passed between scopes. A shared scope can include global scope or closure scopes.
# we can get race conditions in case of shared states. but when we avoid shared state and use pure functions then
# we don't get above issues. Functional programming avoids shared state, instead relying on immutable data structures
# and pure calculations to derive new data from existing data.

# C) variables inside functions are immutable. Functional
# programs do not have assignment statements. If we have to store some value, we define new variables instead.
# This eliminates any chances of side effects because any variable can be replaced with its actual value at any point
# of execution. State of any variable is constant at any instant.
# if we want to change some attribute in object then we have to create a copy old object and store it to some new var
# with new properties. for example:
# bob = Person("bob", 42)
# #now if we want to update bob age then we create a copy
# #copy object is provided by Person class
# olderbob = bob.copy(age=43)


# D) Functional programming is a declarative paradigm, meaning that the program logic is expressed without explicitly
# describing the flow control.

# E) A big no for for-loops and while-loops, so iteration is implemented here using recursion.
# because With recursion, we keep our variables immutable.

# F) Functions are first-class and can be a high order functions in functional programming, because functions in the
# functional programming style are treated as variables. First-class functions can be passed to another functions as
# parameter, can be returned from functions or stored in data structures. Higher order functions are the functions
# that take other functions as arguments and they can also return functions.

# example:
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()

# greet taking function as argument, so it is higher order function
def greet(func):
    # storing the function in a variable(first class function example)
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

# shout and whisper passed as argument, so it is first class function
greet(shout)
greet(whisper)

# some builtin higher order functions are map,reduce,filter, etc.



# so in normal programming:
# doThis()
# doThat()
# atlastDoThis()

# in functional programming:
#  atlastDoThis(doThat(doThis()))
# this is called composition

# closures: it is a way to store function with environment, it means in nested methods we are binding inner method with
# the arguments/vars/properties of outer method. so when we call this inner method out of his scope,
# we can also use variables of outer method also.
# like in case of classes we have properties in class, and methods defined in class can use those properties and update
# them also. we can also see and update those properties outside class scope using class objects.
# but in case of closure, you can only use outer method properties inside inner method,
# we can not update them(to update them we have to use nonlocal keyword) inside inner method,
# which makes them immutable. Also we can not access these outer() method vars
# outside its scope (like this: 'outer.a' or 'inner.a' because unlike classes, properties/vars of method
# are not accessible), which makes them truly private
def outer():
    a = 10
    def inner(x):
        return a+x
    return inner

# so now we have reference of inner() and value of 'a' in inner_method variable with the help of closure
inner_method = outer()

# calling inner method out of his scope(inner method scope is outer() method)
# so now we have value of a which is 30, with the help of closure.
# it will return 30
print(inner_method(20))


# So decorators save the original function with the help of closure.
def wrapper(fun):
    def inner(*args):
        # saves this function value with the help of closure
        fun()
    return inner

x = wrapper(lambda x: x*2)
# now x has inner function and that inner function contain our newly created lambda function with the help of closure
# so we can call inner function from out of his scope and it will not throw error, because closure
# saved fun() value for us.

# we can use closure when we have fewer classes and we want to hide data also, but in case of larger functions
# we suggest classes, otherwise code become messy.


# eventual numbers: Anything we would do with regular numbers, we can do with eventual numbers. Mathematicians call
# this ‘isomorphism’. We can always turn a regular number into an eventual number by sticking it in a function.
# And we can get the eventual number back by calling the function.
# example:
# function returnZeroFunc() {
#     function fZero() {
#         console.log('Launching nuclear missiles');
#         // Code to launch nuclear missiles goes here
#         return 0;
#     }
#     return fZero;
# }

# function fIncrement(f) {
#     return () => f() + 1;
# }
#
# const fOne   = fIncrement(zero);

# this is a stratergy to making impure functions pure, because now every function returns the same function reference.
# the reason defining  fzero inside returnZeroFunc, because in pure functions we can't use variables outside its scope
# that's why we define fzero inside scope of returnZeroFunc function.

# functors,applicative and monads uses these kind of approach(eventual numbers) for wrapping, to convert impure to pure.
# and they also increase predictability of a function.
# functors: you apply a function to a wrapped value
# applicatives: you apply a wrapped function to a wrapped value
# monads: you apply a function that returns a wrapped value, to a wrapped value

# so in real scenerio we use monads, because mondas are simple amd smart.

# you may be wondering how we are going to make http requests ore save our objects into db, etc. so to perform these
# operations we did cheating, we use impure and pure functions both, but we try to reduce number of impure functions as
# possibles

# Note: A side effect isn’t a side effect until it actually happens. with this thinking in mind we use functors,
# applicatives and monads.

# there are two ways to handle functional impurity in our code:
# Dependency injection; and
# The Effect functor(functors/applicatives/monads).
# Dependency injection works by moving the impure parts of the code out of the function. So you have to pass them in
# as parameters. The Effect functor, in contrast, works by wrapping everything behind a function. To run the effects,
# we have to make a deliberate effort to run the wrapper function.
# Both approaches are cheats. They don’t remove the impurities entirely, they just shove them out to the edges of our
# code. But this is a good thing. It makes explicit which parts of the code are impure.

# more about monads:
# A monad is a design pattern that allows us to add a context to data values, and also allows us to easily compose
# existing functions so that they execute in a context aware manner. it helps to remove race condition also.
# it is a design pattern which helps us to compose function with effects and monads are not decorators.
# a monad-value is boxed value which contains value with context.
# it makes functions composition easier.

# monad takes warapped values as input then its bind() functions unwraps value and and apply function then wraps result
# again

# so in bind function we can add glue code (which is called between invocations of functions).
# and in init code we can write intialization code
# example: x[init code, f1()]->v2[glue code, f2()]-> v3[glue code, f3()]-> result

# monads use cases:
# 1. if we want to avoid race condition.
# 2. if we want to do something in between composition of different functions.
# example we want to add intermediate result into a list, each time any function called.
# something like this :

# lst = [x]
# res = f1(x)
# lst.append(res)
# res = f2(res)
# lst.append(res)
# print (res, lst)
# so to avoid tis glue code we can use monads.

# #monads implementation
# def unit(x):
#     return (x, [x])
#
# def bind(t, f):
#     res = f(t[0])
#     return (res, t[1] + [res])
#
#
# print( bind(bind(bind(unit(x), f1), f2), f3) )

# 3. if we want to handle null exceptions and remove bloated if-else null checks, then we can use monads
# example : if we want to check employee boss salary,  where boss is also employee. so in case some employees doesn't
# have boss, we can get null.
# also if we get null, then it can change the flow of our program to exceptions. so we can handle those null
# scenarios in monads

#so normally we will do :
result = None
if john is not None:
    boss = john.get_boss()
    if boss is not None:
        wage = boss.get_wage()
        if wage is not None:
            result = wage

print(result)

# with monads
def unit(e):
    return e
def bind(e, f):
    return None if e is None else f(e)


#note: epeating the calls to bind again and again can be tedious and should be avoided.
# For the purpose we define an auxiliary function(if we implement monads using class then we can override operatores
# like `|` to call bind function):

def pipeline(e, *functions):
    for f in functions:
        e = bind(e, f)
    return e
#Then instead of:
bind(bind(bind(bind(unit(x), f1), f2), f3), f4)
#We can use the shorthand:
pipeline(unit(x), f1, f2, f3, f4)

# monads terms: 1.flattern: unboxing of value. ( M(a)=>a )
# 2. map: applying a function
# 3. lift/unit: converting value from sometype to monad context ( a=> M(a) ) (i.e boxing or packing of value)


# monads 3 laws:

# left identity law: packing a value 'a' and then binding function 'k' is equivalent to calling 'k' function with 'a'
# example: bindM(unitM(a),k) === k(a)

# right identity law: binding a packed value 'm' with same packing function `unitM` should result same packed value.
# i.e if we repack the same value again and again, so it should result the same monadic value
# example: bindM(m, unitM) === m

# associative law: for distinct functions k and h, the order in which bind operation is applied doesn't matter, but
# order of functions h and k will remains the same
# i.e a~(b~c) === (a~b)~c
# example: bindM(m, lambda a: bindM(k(a), h)) === bindM(bindM(m, k), h)

# monad python implementation git link: https://gist.github.com/rcrowley/1232809


# note: When you avoid mutable state, the need for synchronization and locking mechanisms disappears along with it.
# Because functional languages usually avoid mutable state, they are naturally more efficient and effective for parallel
# processing - you won't have the runtime overhead of shared resources, and you won't have the added design complexity
# that usually follows.

# list monad: here bind function will be implementing in each element of list, just like map()
# example:
# k = List([1, 2, 3])
# n = k.bind(neg)
# print(n)              # List([-1, -2, -3])

# implementation:
class List():
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def bind(self, f):
        result = list(map(f, self.value))
        return List(result)

    def __str__(self):
        return 'List(' + ', '.join(map(str, self.value)) + ')'

    def __or__(self, f):
        return self.bind(f)

# failure monad: to handle failure we can use this monad, this will return 2 things result value and false if result is
# executed without any error, in case of failure it return (None, True)

# implementation:
from operator import neg

class Failure():
    def __init__(self, value, failed=False):
        self.value = value
        self.failed = failed

    def get(self):
        return self.value

    def is_failed(self):
        return self.failed

    def __str__(self):
        return ''.join([str(self.value), str(self.failed)])

    def bind(self, f):
        if self.failed:
            return self
        try:
            x = f(self.get())
            return Failure(x)
        except:
            return Failure(None, True)

x='n'
y = Failure(x).bind(int)
print(y.get())


# There are various libraries such as OSlash and PyMonad that provide much more complete implementations, together
# with function composition, partial application and currying functions

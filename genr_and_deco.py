l1=[1,2,3,4,5,6]

#list comprehension
fl=[n*2 for n in [1,2,3,4] if n<16]
# with if else
fl2 = [n*2  if n<16  else n for n in [1,2,3,4] ]

#creating generator using expression
fg=(n*2 for n in [1,2,3,4] if n<16)

print (l1)
print ('\n',fl)
print ('this is generator',fg)

print (next(fg))

# yield: Yield is a keyword in Python that is used to return from a function without destroying the states of its local
# variable and when the function is called, the execution starts from the last yield statement.
# Any function that contains a yield keyword is termed a generator.
# so in below code ,gen() will not do anythng, then fitst __next__ call will print '2' and return 2 and stop function
# there and return control. then second next will print '3' and return 3 and last next will print 'done' and raise
# StopIterationException

#creating generator using function
def gen():
    print(2)
    yield  2
    print(3)
    yield 3

    print('done')
g=gen()
print (next(g))

#printing without next method
for n in g:
    print  (n)

for n in fg:
    print ( n)

#now we can use next on list also by getting its iterable
# if we use next() directly to list it will throw exception Becoz list can iterable but list not itslef is iterable
# element which point to next elements , so first we have to get its iterable
# so that we can store its current pointer location in that (like it can store what is the next value to be called )
#creating iterable of list l1(we can point on this elements using differnent iterables)
iterableList =iter(l1)
print (next(iterableList))

file ="SalesJan2009.csv"
lines =(line for line in open(file,encoding="ISO-8859-1"))
formattedLines=(l.split(',')  for l in lines)
column =next(formattedLines)
dictionaryData=(dict(zip(column,row)) for row in formattedLines)
print(next(dictionaryData))


# recursion in generators
def flat_list(l):
    for e in l:
        if type(e) == type([]):
            # yield from equivalent to 'for v in e: yield v'
            # for recursion in generators, we also have to yield the data came from calling recursive function result
            # because the result of recursively called function will be lost in generators, so we have to yield it here
            yield from flat_list(e)
        else:
            yield e


#iterables
'''    we can make any class iterable by implementing  
  __iter__(self) and __next__(self) functions inside it 
  
  '''
class fibo:
    def __init__(self):
        self.n = 1
        self.x = 0
    def __iter__(self):  # define the iter() function
        return self
    def __getitem__(self, index): # help to get item at particular index (example fibo[4])
        # intializing counter back to 0 and n value to 1
        self.x = 0
        self.n = 1
        if not isinstance(index, int):
            raise Exception('only integer is aacepted')
        # calling next() and updating n value
        while self.x < index:
            self.__next__()
        return self.n
    def __next__(self):  # define the next() function
        if self.n < 10:  # Limit to 10
            self.n += 1
            self.x += 1
            return self.n
        else:
            raise StopIteration  # raise exception
#passing fibo calss object to iter() and getting its iterable
iterator = iter(fibo())
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print('First 10 already printed.')
        break  # break the loop


#Decorators
''' 
decorators is used to add more functionality to given function(Here actual function will not change we
 just add more functionality to given function  )
'''
# here if we want to use argument of actual function then we have to use 'inner()'
# note: it is not necessary to be function name 'inner' to get function arguments
# and don't confuse with (*args, **kwargs), * for var args as tuple and ** for var args as dict ( we can give any argument we want )
# decorators always takes function as argument and also return function
def star(func):
    # we will get all arguments of our function automatically here(method name not necessary to be inner)
    def inner(*args, **kwargs):
        print("*" * 30)
        # calling that function with its actual argument
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# @start and @percent will equivalen to 'printer=star(percent(printer))'
@star
@percent
def printer(msg):
    print(msg)
printer("Hello")


'''!!!!!! decorator with argument !!!!!!!!!!'''
# getting the decorator arguments inside this function argument
def dec(deco_arg):
    print('got the decorator argument!')
    # getting actual function inside argument of this funciton (deco)
    def deco(func):
        print('got the actual function!')
        # getting arguments of actual function in the argument if this function (actualFuncArgs)
        def actualFuncArgs(*args):
            print('got the actual function argument!')
            print('adding 3 values ')
            sum = func(*args) +deco_arg
            #returning modified result with new print statement
            return sum
        # returning above function that will be replaced with original function
        return actualFuncArgs
    # returning the decorated function which came from deco function
    return deco

c= 20
@dec(c)
def add(a, b):
    return a+b

print(add(10, 30))

# decorator as class
# here function atuomatically passed to init and when we call function this decorator class call s called
class Power(object):
    def __init__(self, arg):
        self._arg = arg

    def __call__(self, a, b):
        retval = self._arg(a, b)
        return retval ** 2


@Power
def multiply_together(a, b):
    return a * b

# note: if we put decorator over class then it will be applied to al the methods of tht class and parent classes
# methods also which current classes inherited


# ### couroutines ###
# (subroutines is normal small python function)Coroutines are generalizations of subroutines. They are used for
# cooperative multitasking where a process voluntarily
# yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously.
# unlike subroutine, coroutine have multiple entry point and resume execution.Coroutine can suspend its execution
# and transfer control to other coroutine and can resume again execution from the point it left off.
# it pauses execution, until we receive input using send() and start doing other works.

# They benefit from the ability to keep their data throughout their lifetime and, unlike functions,
# can have several entry points for suspending and resuming execution.
# u may be wondering objects can also store states so why coroutines,actually coroutines are
# faster(because of self lookup time), and we use less code here.

# in coroutines we use below mentioned things:
# 1. x = (yield) : this statement is used to consume data
# 2. send(): to send input in above statement
# 3. close(): to close coroutine


# coroutine vs threads: In the case of threads, it’s an operating system (or run time environment) that switches
# between threads according to the scheduler. While in the case of a coroutine, it’s the programmer and programming
# language which decides when to switch coroutines.

# generators vs coroutines: generators are only data producers but coroutines are data
# consumers.

# example:
def print_name(prefix):
	print("Searching prefix:{}".format(prefix))
	try :
		while True:
				name = (yield)
				if prefix in name:
					print(name)
	except GeneratorExit:
			print("Closing coroutine!!")

# below line will not do anything
corou = print_name("Dear")
# after below line execution print_name is called and pauses it's execution on `name=(yield)` line and keep function
# state save in corou var
corou.__next__() # or we can do corou.send(None) , because corotuines requires null value at starting so that they can
# reach to first (yield) statement. next(corou) automatically send None value to (yield)

# once we call send(), line below `name=(yield)` will be executed and when again we reach to `name=(yield)` statement
# then code again pauses it's execution and wait for next input.
corou.send("Atul")
corou.send("Dear Atul")
# close() will raise GeneratorExit exception, also if currents python program ends, then this close will be called
# automatically
corou.close()


# (yield) is bidirectional, it mean it can produce output and take input as well
def print_name(prefix):
    try :
        while True:
            # below line will be triggerred by next or send method, in case of next it will just return 3, but in case of
            # send it will first capture input and run below methods then return 3
            name = (yield 3)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


x = print_name('d')
# it will print 3
print(next(x))
# ot will print prefix then 3
print(x.send('der'))



# generator with coroutine
def produce():
    print('starting method')
    while True:
        n = (yield)
        print(n)
        yield n
x = produce()
x.__next__()
# above line will print msg and  stop at n=yield
z = x.send(10)
# after send() it will return n and stop at yeild n
print(z)
# below line will move code execution after yeild n and code will again stop at n=yield
x.__next__()
z = x.send(20)
#after send() it will return n and stop at yeild n
print(z)


# Chaining coroutines for creating pipeline
#
# Coroutines can be used to set pipes. We can chain together coroutines and push data through the pipe using send() method.
# A pipe needs :
# 1. An initial source(producer) derives the whole pipeline. The producer is usually not a coroutine, it’s just a simple method.
# 2. A sink, which is the endpoint of the pipe. A sink might collect all data and display it.

# code example:
# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):

    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):

    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")

def print_token():
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")

pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine = pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)


# yield and return together:
def test():
    yield 1
    return "abc"
gen = test()
next(gen)
#1
try:
    next(gen)
except StopIteration as exc:
    print(exc.value)
#abc
# so basically on second next() compiler didn't found any yield and throw stop iteration exception
# but inside this exception we have our returned value

# another way using `yield from`, in `yield from` statement first it will yield values present in called generator
# and once generator is exhausted then it will assign returned value of generator in the given variable.
# like in below case `val = yield from inner()` outer function first yield inner function values then once inner is
# exhausted and we reach to return statement, it will assign inner() return value to val variable:
def inner():
    inner_result = yield 2
    # on gen.send("abc") execution , below line will be executed and inner() will return 3 to 'val' of outer function
    # then print() of outer will be executed and finally it will stop at yield 4
    print('inner', inner_result)
    return 3

def outer():
    val = yield from inner()
    print('outer', val)
    yield 4

gen = outer()
print(next(gen))
# 2
print(gen.send("abc"))
# inner abc
# outer 3
# 4




# ###generator based coroutines vs async/ await (note: check multithreading,_processing_aysync.py for async/await code):

# generator based coroutines is old way to do async task, now we have asyncio lib to use async/await keyword,
# async/await is lot more cleaner than generator based code.

# await is equivalent to 'yield from' statement.

# Well, async/await just a syntactic feature on top of generators that was introduced to Python to fix the generators'
# ambiguity.

# A native coroutine(async/await) is basically a generator object that has a different type. The difference between the
# types is that the generator type implements __iter__() and __next__(), while the coroutine type implements
# __await__(). The implementation of send() is the same.

# if you try to use a yield expression in an async def function, what you'll get is not a native coroutine but
# something called an asynchronous generator, which has  __aiter__() and __anext__() special methods .
# also if Python allowed us to await on regular generators, we would again mix the concepts of generators and coroutines
# and come back to the same ambiguity problem. The @types.coroutine decorator explicitly says that the generator is a
# coroutine.
# so basically using this decorator we can call await over our generator based coroutine, otherwise we have to use
# yield from syntax.
# (but now we rarely use generator based coroutine)
# example:
import types
@types.coroutine
def gen_coro():
     yield 3
async def coro3():
    await gen_coro()

coro3().send(None)


### async/await and event loop implementation:


# Deep inside asyncio, we have an event loop. An event loop of tasks. The event loop's job is to call tasks every
# time they are ready and coordinate all that effort into one single working machine.
# The IO part of the event loop is built upon a single crucial function called select (select is multiplexing lib in
# python)(multiplexing:  I/O multiplexing is the capability to tell the kernel that we want to be notified if one
# or more I/O conditions are ready).
# Select is a blocking function, implemented by the operating system underneath,
# that allows waiting on sockets for incoming or outgoing data.
# Upon receiving data it wakes up, and returns the sockets which received data, or the sockets which are ready for
# writing.
# so basically using multiplexing async/await know when to start function which is waiting for I/O.


# simple socket server using generator based coroutines

from collections import deque
import selectors

# The asyncio event loop provides an interface similar to that of our final EventLoopAsyncAwait
# (not exactly same, but has similar kind of functionality, below is just simplified version of it)
class EventLoopYieldFrom:
    def __init__(self):
        self.tasks_to_run = deque([])
        self.sel = selectors.DefaultSelector()

    def create_task(self, coro):
        self.tasks_to_run.append(coro)

    def sock_recv(self, sock, n):
        yield 'wait_read', sock
        return sock.recv(n)

    def sock_sendall(self, sock, data):
        yield 'wait_write', sock
        sock.sendall(data)

    def sock_accept(self, sock):
        yield 'wait_read', sock
        return sock.accept()

    def run(self):
        while True:
            if self.tasks_to_run:
                # first it will fetch task from our queue
                # if see in below code our first task is run_server
                task = self.tasks_to_run.popleft()
                try:
                    # inside our first task which is run_server(), we have this line
                    # `client_sock, addr = yield from loop.sock_accept(sock)`
                    # so below line will get  `'wait_read', sock` because  sock_accept method first yield these things

                    # now let's say once cycle of this while loop is completed for our run_server task,
                    # and if you noticed we are appending same task in queue again at the end of this method.
                    # so now if we run next() on same method it will
                    # call actual sock.recv(n) method and then it will return sock and addr value
                    # to this line : client_sock, addr = yield from loop.sock_accept(sock)
                    # inside run_server method, because that's what yeild from do, once generator is exhasuted and
                    # we reached to return statement then it provide return value to assigned vars.
                    # so if you have noticed, in this case control again goes back to run_server method, there
                    # we will print addr and then create enw task to handle_client()
                    # once that is done,  we will again get control back here and throw StopIteration exception and then
                    # except StopIteration will be executed
                    # and next cycle of this while loop will start, then this time we got handle_client task
                    # and same procedure will follow.
                    # but because run_server calling generator inside while , that means after every cycle we are
                    # getting new generator due to which in case of run_server we will never see StopIteration exception
                    # (simple funda is as long as we are getting yield, this exception will not be thrown)
                    # but in case of handle_client we can see this exception, where there we are breaking loop once all
                    # data is sent to client, so after disconnect print message it will throw this exception


                    op, arg = next(task)
                except StopIteration:
                    continue
                # now we check what kind of operation we get, and on the basis of that we will register it in select()
                if op == 'wait_read':
                    self.sel.register(arg, selectors.EVENT_READ, task)
                elif op == 'wait_write':
                    self.sel.register(arg, selectors.EVENT_WRITE, task)
                else:
                    raise ValueError('Unknown event loop operation:', op)
            # now when all available tasks are succesfully registered to select() queue and we don't have any new task
            # then below else code will run
            else:
                for key, _ in self.sel.select(timeout=0):
                    # now if any of the registered task is ready then select() loop will be run,
                    # otherwise this loop will not run
                    # select() is blocking method, that's why we put timeout 0.
                    # because we don't want to keep waiting until any any of the registered task is ready
                    task = key.data
                    # in above line we will get our registered task, which can be sock_recv/sock_send_all/sock_accept
                    sock = key.fileobj
                    # in below line we are unregistering given task from select()
                    self.sel.unregister(sock)
                    # in below line we are appending same task again to our task queue
                    self.create_task(task)



import socket

loop = EventLoopYieldFrom()


def run_server(host='127.0.0.1', port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
        # yield from is equivalent to : for i in loop.sock_accept():
        #                                   yield i
        # below code will accept new connections
        client_sock, addr = yield from loop.sock_accept(sock)
        print('Connection from', addr)
        # once our above task is completed then we will create task for handle_client code for same client
        loop.create_task(handle_client(client_sock))


def handle_client(sock):
    while True:
        # it will receieve input data from client
        # for current client it will wait here until we receive input from client
        # meanwhile our run() loop will be running to accepts new tasks.
        # same goes for ` yield from loop.sock_sendall(sock, received_data)` also
        received_data = yield from loop.sock_recv(sock, 4096)
        if not received_data:
            break
        # below code will send response to client
        yield from loop.sock_sendall(sock, received_data)

    print('Client disconnected:', sock.getpeername())
    sock.close()


if __name__ == '__main__':
    loop.create_task(run_server())
    loop.run()

##################### simple socket server using await #########################################################
#

from collections import deque
import selectors
import types


class EventLoopAsyncAwait:
    def __init__(self):
        self.tasks_to_run = deque([])
        self.sel = selectors.DefaultSelector()

    def create_task(self, coro):
        self.tasks_to_run.append(coro)

    @types.coroutine
    def sock_recv(self, sock, n):
        yield 'wait_read', sock
        return sock.recv(n)

    @types.coroutine
    def sock_sendall(self, sock, data):
        yield 'wait_write', sock
        sock.sendall(data)

    @types.coroutine
    def sock_accept(self, sock):
        yield 'wait_read', sock
        return sock.accept()

    def run(self):
        while True:
            if self.tasks_to_run:
                task = self.tasks_to_run.popleft()
                try:
                    op, arg = task.send(None)
                except StopIteration:
                    continue

                if op == 'wait_read':
                    self.sel.register(arg, selectors.EVENT_READ, task)
                elif op == 'wait_write':
                    self.sel.register(arg, selectors.EVENT_WRITE, task)
                else:
                    raise ValueError('Unknown event loop operation:', op)
            else:
                for key, _ in self.sel.select(timeout=0):
                    task = key.data
                    sock = key.fileobj
                    self.sel.unregister(sock)
                    self.create_task(task)


import socket


loop = EventLoopAsyncAwait()


async def run_server(host='127.0.0.1', port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
# like yield from on first call run_server will loose the control once reached to below line and once
# ready then it will be called again and return the values for client_sock and addr
        client_sock, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(handle_client(client_sock))


async def handle_client(sock):
    while True:
        received_data = await loop.sock_recv(sock, 4096)
        if not received_data:
            break
        await loop.sock_sendall(sock, received_data)

    print('Client disconnected:', sock.getpeername())
    sock.close()


if __name__ == '__main__':
    loop.create_task(run_server())
    loop.run()



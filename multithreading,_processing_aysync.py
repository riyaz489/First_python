
#single, global lock (mutex lock)on the interpreter when a thread is interacting with the shared resource (the page in the book).
# In other words, only one author can write at a time. Python’s GIL accomplishes this by locking the entire interpreter,
# meaning that it’s not possible for another thread to
# step on the current one. so because of GIL, only one thread can be in a state of execution at any point in time
# (it ensures thread safety).
# GIL is used to avoid race condition, in multithreading environment.
# The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring
# the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead
# ( repeated acquisition and release of locks will be avoided because we are putting lock on var which is using resources,
# instead of other vars which are waiting for resource, hence lesser locks)


# how gil works (lets take example of 2 threads and 2 processor envrionment):
# 1. first thread aquired the gil and keep using it unit it get IO task.
# 2. if second thread is is going to timeout in 5 milli seconds and first thread is still aquired the lock.
#  in that case it will send signal to first thread to release the gil and then after receiving request it will
# signal to second thread again and one second thread got signal from thread1 it will send ack-signal to thread1 again
# after that thread1 will go to wait state and thread2 aquire gil.
# here scheduling and switching done by the OS, which takes some times.
# 3. so here , time-out while switching gil is increasing response time
# and if we have single core then context switching will be done as well.

# to overcome GIL issue we can use:
# multiprocessing: where Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem.
# or we can use multithreading in I/O bound task, because there thread always less resource-hungry than process.
# Multi-threading is a traditional solution that performs tasks asynchronously.


# Asynchronous, single threaded: you start the eggs cooking and set a timer. You start the toast cooking, and set a timer.
# While they are both cooking, you clean the kitchen. When the timers go off you take the eggs off the heat and the
# toast out of the toaster and serve them.
# Asynchronous, multithreaded: you hire two more cooks, one to cook eggs and one to cook toast.
# Now you have the problem of coordinating the cooks so that they do not conflict with each other in the
# kitchen when sharing resources. And you have to pay them.
# Now does it make sense that multithreading is only one kind of asynchrony?
# Threading is about workers; asynchrony is about tasks.

# so for if we don't have much cpu intensive task then don't use multithreading or parallel processing, if single worker can
# handle cpu intensive jobs and mostly we are waiting for network calls or some other resource responses then use async only.
# adding multithreading there will increase response time only.
# so prefered appraoch is use async over multithreading.

# note: if we have 2 threads and 2 cores and both we started parallely so first will go to 1 core  and 2 thread go to 2 core
# this scenerio is still will be multi threading not multiprocessing. because still both thread is fighting for gil.


# When to use multiprocessing vs asyncio or threading:
# 1.  Use multiprocessing when you need to do many heavy calculations and you can split them up.
# 2. Use asyncio or threading when you're performing I/O operations -- communicating with external resources or
# reading/writing from/to files.Use asyncio when you can, threading when you must.
# 3. Multiprocessing and asyncio can be used together, one example is gunicorn, there we can provide combiation of async
# and multiple workers , there each worker use one core,and each worker can take 100s request because it's async
# (for more info check gunicorn file).thumb rule is create processes first then inside process define async functions.
# example:
# def bootstrap(tx,rx):
#  loop = asyncio.new_event_loop()
#  asyncio.set_eventloop(loop)
#  loop.run_until_completed(run_loop(tx,rx))
# def main():
#     p=multiprocessing.Process(target=bootstrap,
#                               args=(tx,rx))
#     p.start()

# multithreading: os decide when to switch task (number of core 1, multiple workers(thread) keep fighting for same cpu
# but if we have more cores than threads can be assigned to other cores as well but still it will not be multiprocessing
# because here even if threads are on different cpu but still thy are running one after another in python.).
# so basically, Multiprocessing is parallelism and Multithreading is concurrency.
# note: we can't kill a running thread but we can kill processes in multiprocessing package
# async: task decide when to give up control (number of core 1, same worker switches tasks)
# multiprocessing: The processes all run at the same time on different processors.
# The processes all run at the same time on different processors.The processes all run at the same time on
# different processors. (multiple cpu)

# https://testdriven.io/blog/concurrency-parallelism-asyncio/

# note: it is bad practice to use locks in async code,  because we don't know how long it is going to hold a
# particular resource and it can also arise deadlock situation.

# note: race condition only occurs in multithreading sync/async code not in single thread async/sync code
# and also in case of distributed system where multiple replicas of backend making request to single db
# or in case of parallel processing if we are using some shared memory(but usually in parallel processing we don't have
# common resource). but python GIL take care of race condition in multithreading.

# note: for static files S3 is now strongly consistent .There’s no impact on performance, you can update an object
# hundreds of times per second if you’d like, and there are no global dependencies.
#https://aws.amazon.com/blogs/aws/amazon-s3-update-strong-read-after-write-consistency/

## multiprocessing

# we can use Event class to send signals or communicate between different process(same class we have in threading also)
# for having shared data we can use queues and manager class of multiprocessing library.
# for locks in shared data we can use locks class
# example for all of these will be preset in this link:
# https://pymotw.com/2/multiprocessing/communication.html

# process vs pool: 1. if you have same function running with different arguments then use pool, because it's faster.
# 2. in case if task is more IO bound wait, then use process because in case of process OS can switch task with other
# process, but in case of pool, it first complete the given task(in case of async pool also it will start all job in
# pool asyncronously but if job is not completed then it will still hold processor and any new process apart from pool
# jobs will not be able to capture core, so OS scheduler can't don anything like it do context switching in case of
# process class).
# 3. in case we hae different methods then use process because creation of pool class will take extra overhead.
# 4. in case of pool same job may or may not run on same processor, but in process class it will surely run in different
# processor.
# 5. pool will take memory only for running process, while process() will take memory for all the specified process.

# to get cpu cores count:
# import multiprocessing as mp
# print("Number of processors: ", mp.cpu_count()

# multiprocessing example (one more example in python_signals file using process(), below example is using pool)
##################
# using process


# # Process simple example ########
from multiprocessing import Process

def f1(name):
    print('hello', name)
def f2(name):
    print('hello', name)
if __name__ == '__main__':
    procs = []
    p1 = Process(target=f1, args=('bob',))
    p1.start()
    procs.append(p1)
    p2 = Process(target=f2, args=('jerry',))
    p2.start()
    procs.append(p2)
    for p in procs:
         p.join()


###### process using class ####
import multiprocessing
import time


class Process(multiprocessing.Process):
    def __init__(self, id):
# By subclassing multiprocessing.process, you can create a process that runs independently.
# By extending the __init__ method you can initialize resource
        super(Process, self).__init__()
        self.id = id
# Here Process.start() will create a new process and will invoke the Process.run() method.
    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))


if __name__ == '__main__':
    p = Process(0)
    p.start()
    p.join()
    p = Process(1)
    p.start()
    p.join()

# using pool
# in case of pool class we set number of process less than or greater than number of available cores.
# but in both the cases it will be more slower because in fist case we are underutilizing and in second case more
# context switching. so ideally provide the exact or 1 less number of cores(same goes with Process class).
# In Pool() if we don't provide argument then it will automatically get current number of cores.


##### sync pool parallel programming ######
import multiprocessing as mp
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count
data = [1,2,3,4,5,6,7,8]
# initializing pool using with, otherwise we have to call pool.close()
with mp.Pool(mp.cpu_count()) as poll:

    # using apply we are calling a function with specified arguments
    results = [pool.apply(howmany_within_range_rowonly, args=(row, 4, 8)) for row in data]
    # using map we can call same function with different aguments,
    # but we can pass only one argument with different scenarios
    # i.e we can pass only one level of iterable.
    # this below result line is equivalent to above result line
    # results = pool.map(howmany_within_range_rowonly, [row for row in data])
    # startmap is used to call same function with different arguments, its same as map, but here we can pass
    # iterable of iterables, second iterable will automatically unpack to function arguments
    # this below line is equivalent to first result line [pool.apply ... ]
    #results = pool.starmap(howmany_within_range_rowonly, [(row, 4, 8) for row in data])

    print(results[:10])

##### sync pool parallel programming ######

# Parallel processing with Pool.apply_async()

import multiprocessing as mp
pool = mp.Pool(mp.cpu_count())

results = []

# Step 1: Redefine, to accept `i`, the iteration number
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


# Step 2: Define callback function to collect the output in `results`
def collect_result(result):
    global results
    results.append(result)


# Step 3: Use loop to parallelize
for i, row in enumerate(data):
    # it same as apply only difference is it will return and will not wait for result .also the order result gets
    # jumbled up, i.e. the processes did not complete in the order it was started.
    pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)

# get() is used to get result from async pool functions.
# call apply_async() without callback:
# result_objects = [pool.apply_async(howmany_within_range2, args=(i, row, 4, 8)) for i, row in enumerate(data)]
# results = [r.get()[1] for r in result_objects]

# with starmap:
# results = pool.starmap_async(howmany_within_range2, [(i, row, 4, 8) for i, row in enumerate(data)]).get()

# With map:
# results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()


# Step 4: Close Pool and let all the processes complete
pool.close()
pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

# Step 5: Sort results [OPTIONAL]
results.sort(key=lambda x: x[0])
results_final = [r for i, r in results]

print(results_final[:10])
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

### pandas df using pool parallel programming:
# map vs imap : imap returns iterables whereas map return out in list. also map will wait for all queue items to
# complete then will start processing, whereas imap will return already processed chunk and start processing it, instead
# of waiting complete data. With map_async, an AsyncResult is returned right away, but you can't actually retrieve
# results from that object until all of them have been processed, at which points it returns the same list that map does
#  There's no way to get partial results; you either have the entire result, or nothing in case of map and async_map both.
# imap_unordered is async version of imap
# 1. below example is of pandas df, processing row in parallel
def hypotenuse(row):
    return round(row[1]**2 + row[2]**2, 2)**0.5

with mp.Pool(4) as pool:
    result = pool.imap(hypotenuse, df.itertuples(name=False), chunksize=10)
    output = [round(x, 2) for x in result]

print(output)
#> [9.43, 5.83, 5.0, 5.66, 11.4]

# 2. columns wise parallisation:
def sum_of_squares(column):
    return sum([i**2 for i in column[1]])

with mp.Pool(2) as pool:
    result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
    output = [x for x in result]

print(output)
#> [163, 147]

# 3. third approach is to parallel-process whole function, for this we use some other lib 'pathos'
# pathos vs multiprocessing: pathos uses dill for serialization of objects but multiprocessing uses pickle.
#  dill is slower typically, but that's the penalty you pay for more robust serialization. also dill is build over pickle.
#  If you are serializing a lot of classes and functions,then we can use dill.
# (pickling: process of converting python objects into bytestream. and unpickling is to convert byte stream into object
# by default we have pickle library load and dump function to do that).

import numpy as np
import pandas as pd
import multiprocessing as mp
from pathos.multiprocessing import ProcessingPool as Pool

df = pd.DataFrame(np.random.randint(3, 10, size=[500, 2]))


# just return shape of whole ds
def func(df):
    return df.shape


if __name__ == '__main__':
    cores = mp.cpu_count()

    # dividing array into multiple sub arrays
    df_split = np.array_split(df, cores, axis=0)

    # create the multiprocessing pool
    pool = Pool(cores)

    # process the DataFrame by mapping function to each subarray across the pool
    # np.stack just concatenate the result comes from each subprocess into a single array
    df_out = np.vstack(pool.map(func, df_split))

    # close down the pool and join
    pool.close()
    pool.join()
    pool.clear()



# sometime we need to share some common data in case of multiprocessing also, so At first thought, it might seem like a
# good idea to have some sort of shared data structures that would be protected
# by locks. but When there is only one shared structure, you can easily run into issues with blocking and contention.
# As such structures proliferate, however, the complexity and unexpected interactions multiply,
# potentially leading to deadlocks, and very likely leading to code that is difficult to maintain and test.
# The better option is to pass messages using `multiprocessing.Queue` objects.
# Queues should be used to pass all data between subprocesses.
# This leads to designs that “chunkify” the data into messages to be passed and handled, so that subprocesses can
# be more isolated and functional/task oriented.
# In multiprocessing environment queue is the sloution for consistency, instead of some shared data-structrue or cron-jobs.
# In a queuing system, this situation can be avoided by setting up multiple workers, which can each pick a job (containing 100 reports to be done each)
# and work in parallel to finish off the task much, much sooner.
# tools for queueing: rabbit mq, rdies, aws, etc.



## async

# note: for generator based coroutine (old way of async/await) and async/await loop works, check genr_and_deco.py file
# An asynchronous function in Python is typically called a 'coroutine', which is just a function that uses the async
# keyword, or one that is decorated with @asyncio.coroutine. Either of the functions below would work as a coroutine
# and are effectively equivalent in type:
# note: coroutines is going to deprecate soon.
import asyncio

async def ping_server(ip):
    pass

@asyncio.coroutine
def load_file(path):
    pass


# In case you ever need to determine if a function is a coroutine or not, asyncio provides the method
# asyncio.iscoroutinefunction(func) that does exactly this for you.
# Or, if you need to determine if an object returned from a function is a coroutine object,
# you can use asyncio.iscoroutine(obj) instead.

# Note: but we now use `async` instead of `coroutine` decorator
# ‘async for’ is used to iterate over asynchronous generator
# ‘async with’ is used to do async operations with cleanup(garbage collected)
# `create_task` is used to convert our async methods to task (this methods returns task object),
# becuase some asycnio methods only accepts tasks and also  it provide some extra methods which helps us to manage
# function lifecycle, like we cn check it's status and cancel it also.

# for sequential calling of asnyc methods we use `await` to call methods, it will wait until current called method
# is completed. to call methods in parallel , we use gather()
# to create async pipeline see below code :

# async def pipeline():
# await step1()
# await step2()
# await step3()
# await step4()

# asyncio.gather(pipeline,pipeline,pipeline,pipeline,pipeline,pipeline,pipeline,pipeline)

# using asyuncio lib we can stream module to stream data asyncronously.
# in asyncio module we have queues also. using queues we can easily create load balance functions.
# in queue we have max size (if we define it 0 or negative then it's indefinite), when queue reach to its max size then
# put function will wait, until we get free slot in queue again

# async/await code example:
import asyncio
import aiofiles
import aiohttp

async def fetch_html(url, session):
    resp = await  session.request(method="GET", url=url)
    resp.raise_for_status()
    html = await resp.text()
    print('fetched')
    return html

async def write_one(file, url, session):
    res = await fetch_html(url=url, session=session)
    async with aiofiles.open(file, "a+") as f:

        await f.write(res[0: 10]+'\n')
    print('wrote to file')
    return 'done'
a=10
async def dummy():
    print(a)
    print(b)
    return str(a)
b=10
async def bulk_crawl(file):
    urls= ['https://realpython.com/async-io-python/#a-full-program-asynchronous-requests',
           'https://pythonprogramming.net/asyncio-basics-intermediate-python-tutorial/']
    result = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            #if we want result of write_one then we have to convert them into task using create_task()
            tasks.append(loop.create_task(write_one(file=file, url=url, session=session)))
        tasks.append(loop.create_task(dummy()))
        # gathering multiple coroutines or async functions and their results
        await asyncio.gather(*tasks)
        return tasks

if __name__ =='__main__':
    with open('a.txt', "w")as output:
        output.write("source_url\tparsed_url\n")
    # create eveent loop and run async methods
    loop = asyncio.get_event_loop()
    r1 = loop.run_until_complete(bulk_crawl(file='a.txt'))
    print(r1[0]._result + r1[1]._result  + r1[2]._result )


# queue example ############

import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())



## multithrading example:
import threading
import time

def counter1(num):

    while num>0:
        print(num)
        num-=1
    time.sleep(10)
    print('thread one completed')

def counter2(num):
    while num>0:
        print(num)
        num-=1
    time.sleep(11)
    print('thread 2')


if __name__ == "__main__":

    # creating thread
    t1 = threading.Thread(target=counter1, args=(2,))
    t2 = threading.Thread(target=counter2, args=(2,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed (till 3 secs)
    t1.join(timeout=5)
    # checking if t1 is still alive after 3 sec or completed already
    if t1.is_alive():
        print(  "thread is not done,now we will not wait for this thread to complete.")
        print('it means now below code will be executed')

    else:
        print( "thread has already finished.")

    # wait until thread 2 is completely executed
    t2.join()



# ##multithreading using locks, to avoid race condition
import threading

# global variable x
x = 0

def increment():
	global x
	x += 1

def thread_task(lock):
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating a lock
	lock = threading.Lock()

	# creating threads
	t1 = threading.Thread(target=thread_task, args=(lock,))
	t2 = threading.Thread(target=thread_task, args=(lock,))

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))

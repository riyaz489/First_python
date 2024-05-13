 # python signals are used to provide custom functions for OS events. its like event based programming.
# there are 2 libraries for signal 1. signal (inbuilt) & 2. blinker

# # example:
# import signal
# def my_custom_handler(signum, stack_frame):
#    print('I have encountered the signal KILL.')
#    print('CTRL+C was pressed.  Do anything here before the process exists')
# signal.signal(signal.SIGINT, my_custom_handler)
#
# # adding 3 sec sleep to test above method so that we can press ctrl+c
# # run from console to test it 'python script_name.py'
# import time
# time.sleep(5)

# this signal function requires 2 arguments signal number and callback. this callback further require 2 arguments
# The signal number and  Current stack frame (or signal.SIG_IGN or signal.SIG_DFL) as arguments.

# flow of signals:
#  1. This signal handler is executed inside the low-level signal handler.
#  The low-level signal handler is written in the C programming language.
# 2. The low-level signal handler sets a flag.
# 3. This flag tells the virtual machine to execute the higher-level signal in Python.
#   It will interrupt the execution of the instructions of the current function.


# some notes about signals:

# 1. Do not use signals for inter-thread communication. The signals are always executed in the main Python thread.

# 2. If we want inter-thread communication then use the synchronisation primitives from the threading module.

# 3. Long-running operations such as a regular expression that attempts to find patterns in a large text run until it
# completes its execution. They are not interrupted by the signals. The signals are called after it
# finished its computation.

# 4. If there is an error raised by C code then it is not optimum to catch those synchronous errors.
# Such examples are SIGFPE or SIGSEGV. This is because Python will return the signal handler to the C code which
# will raise the same signal again. Thus it will hang the code.
# We can use the faulthandler module in Python to report on synchronous errors.

# 5. In Linux, we can pass in any of the acceptable signal enum values .
# In Windows, the acceptable values for signal() are SIGABRT, SIGFPE, SIGINT, SIGILL, SIGSEGV, SIGTERM, SIGBREAK.
# A ValueError is raised for any other case


# signal lib comes with different functions also to trigger/stop/ignore some signals
# example:
# below code will set timeout for given function:
# def handler(signum, stack_frame):
#     print('time limit exceeded',signum)
#     print(stack_frame)
#
# # SIGALRM is unix feature s will not work on windows
# # so to set timeouts on functions use threading lib in windows
# signal.signal(signal.SIGALRM, handler)
# signal.alarm(5)
# # any long time taking function
# time.sleep(6)
# # new alarm will override old one, start counting time from now
# # alarm(0) means, disabled the alarm
# signal.alarm(0)


# so timeout code in windows will look like this (because windows does not have much signals)

import time
from itertools import count
from multiprocessing import Process
def inc_forever():
    print('Starting function inc_forever()...')
    while True:
        time.sleep(1)
        print(next(counter))
def return_zero():
    print('Starting function return_zero()...')
    return 0

# counter is an infinite iterator
counter = count(0)
p1 = Process(target=inc_forever, name='Process_inc_forever')
p2 = Process(target=return_zero, name='Process_return_zero')
p1.start()
p2.start()
p1.join(timeout=5)
p2.join(timeout=5)
p1.terminate()
p2.terminate()
if p1.exitcode is None:
       print(f'Oops, {p1} timeouts!')
if p2.exitcode == 0:
        print(f'{p2} is luck and finishes in 5 seconds!')
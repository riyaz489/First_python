# A traditional webserver does not how to run python web applications.
# let say we have nginx or apache webserver, those server can serve static files or do caching, but they can not
# interact with python applications, so a inter-mediator is required.
# In late 90s there was an implementation of apache known as mod-python to run python applications.
# however mod_python was not the standard specification.
# therefore python community came up with wsgi to carry out communication between python-application and web server,
# WSGI is defined by pep3333 standard.
# There are multiple wsgi containers available today. (GUnicorn[green unicorn], uWSGI, mod_wsgi, cherryPy)
# Hence, a WSGI container is required to be installed in the project so that a web server can communicate to a
# WSGI container which further communicates to the Python application and provides the response back accordingly.
# Finally, when the web server obtains the response, it is sent back to the web browser/users.
# if we easily switch to one of the wsgi container without any application code change required, because all of
# them use same standards for communication. but if we use any custom module to interact with python application
# then we don't get this flexibility.
# so we don't have to worry about wsgi configuration these days because it's already coming pre-configured in
# different python framework.

## Gunicorn
# Gunicorn is a Python WSGI HTTP Server that usually lives between a reverse proxy (e.g., Nginx) or load balancer
# (e.g., AWS ELB) and a web application such as Django or Flask.
# Gunicorn starts a single master process that gets forked, and the resulting child processes are the workers.
# The role of the master process is to make sure that the number of workers is the same as the ones defined in
# the settings. So if any of the workers die, the master process starts another one, by forking itself again.
# The role of the workers is to handle HTTP requests.
# The pre in pre-forked means that the master process creates the workers before handling any HTTP request.


# Gunicorn comes with 3 different settings:

# 1.  Workers: each worker is a unix process which loads python application. there is no shared memory between workers
# The OS kernel handles load balancing between worker processes.
# ideal numbers: 2*cpu+1
# exmaple, for dual core, 5 workers
# gunicorn --workers=5 main:app
# best use case : if application is CPU bounded

# 2. Threads: Gunicorn also allows for each of the workers to have multiple threads.
# In this case, the Python application is loaded once per worker, and each of the threads spawned by the same
# worker shares the same memory space.
# To use threads with Gunicorn, we use the threads setting. Every time that we use threads, the worker
# class is set to gthread:
# gunicorn --workers=5 --threads=2 main:app
# The maximum concurrent requests are workers * threads 10 in our case.
# The suggested maximum concurrent requests when using workers and threads is still(2*CPU)+1.
# So if we are using a quad-core (4 CPU) machine and we want to use a mix of workers and threads, we could use
# 3 workers and 3 threads, to get 9 maximum concurrent requests.
# gunicorn --workers=3 --threads=3 main:app
# best use case: if there is concern of application memory footprint.because threads loads application once and
# also shared same memory.(but async model saves more memory, like in above example ,we will use 9 applications space,
# but async with 3 workers only use 3 applications memory)

# 3. pseudo-thread:
# There are some Python libraries such as gevent and Asyncio that enable concurrency in Python by using \
# “pseudo-threads” implemented with coroutines.
# Gunicorn allows for the usage of these asynchronous Python libraries by setting their corresponding worker class.
# Here the settings that would work for a single core machine that we want to run using gevent:
# gunicorn --worker-class=gevent --worker-connections=1000 --workers=3 main:app
# (2*CPU)+1 is still the suggested workers since we only have 1 core, we’ll be using 3 workers.
# In this case, the maximum number of concurrent requests is 3000 (3 workers * 1000 connections per worker)
# threads option is not present with async, because it's kinda defeat the purpose
# The way they manage to do it is by “monkey patching” your code, mainly replacing blocking parts with compatible
# cooperative counterparts from gevent package. So with this we don't need to modify our, gunicorn patches everything.
# but Gevent needs all of your code to be co-operative in nature or all libraries you use should be monkey-patchable.
# best use case : if application is IO bounded.

# How many worker and thread ?
# numbers of threads + number of workers  =(2×numcores)+1
# The intuition behind this formula is the following:
# +1: One worker should be reserved for scheduling
# 2n: While one thread is doing I/O and waiting, and another thread is used for CPU

# problem with sync model (workers only or workers+threads):
# 1. need more memory
# 2. incoming requests can face timeouts.

# problem with async model:
# 1. code should be gevent friendly. This means either ensuring all the DB drivers, clients, 3rd party libraries
# used all of these are either pure python, which would ensure they can be monkey-patched OR they are written
# specifically with Gevent support. If any of your library or part of code does not yield while doing IO then all your
# greenlets in that worker are blocked and this will result in long halts. You will need to find any such code and fix
# it (if we are facing lot of requests timeout and our cpu usage is low,this means above mentioned issue occured)

# 2. One thing to take into consideration when using gevent is to understand that it’s really easy to end up with a
# lot of concurrent connections.
# we need to have connection pools that can be reused and at the same time ensure that your app and
# backend service can create and maintain that many socket connections.

# So in multi request paradigm where many request are entertained by the server,
# it would be hard to establish and put on wait each client. POOL helps us that it gives us pre prepared connection
# and we use it and discard it. POOL get that connection and re-establish it for the next request.
#
# But in a single threaded environment it is the other way around. POOL would be a very heavy resource
# for a single threaded env.
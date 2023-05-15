# import init_file

# so basically __init__.py file is used to make any folder a module
# and when that module is imported this __init__.py file executed
# like here we imported init_file module so when this main.py runs the __init__.py file of
# init_file folder is also executed.

# note: init file only executed when we import its module or it child module (if we run any python file
# directly which present inside a module then its __init__.py will not run [like in current scenerio if we rn this
# main.py file then __init__.py will not bbe executed until we import the given module ] )
# note: __init__.py is only executed once, it doesn't matter how many times we imported that module.

# like below we have imported some_module but __inti__.py file of init_file module is also execute

#import init_file.some_module

# note: best practice is to avoid writing code inside __init__.py file

class s():

    def __init__(self):
        print('hi')
    def sd(self):
        print('df')

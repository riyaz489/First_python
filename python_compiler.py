# we know that python is intrepreted language, that means it does not use compilers, but it's not true.
# python first compiles python code and generate byte-code file and then run byte-code file using interpreter
# (default interpretor path 'usr/local/bin/python3.8').
# Instead of executing the instructions on cpu , byte code instructions are executed on
# virtual machine (python virtual machine is special environment where byte code files are executed,
# byte-code is like low-level code for these virtual machines)
# which translate byte-code to machine-code.the compilation part is hidden from users. as soon as execution is completed
# the byte-code is delete by python. byte-code files goes with pyc extensions. sometimes we have seen pycache folders
# in our project, those folder contains .pyc files. those are used to speed up compilation process. as long as long we
# don't change our code,  python compiler will use pycache and avoid compilation( and byte-code creation) for those
# python files.

# byte code is not platform dependent, but depends on specific version of pvm(python virtual machine). so as long as
# byte-code and pvm have same version we can execute it on any os(but python virtual machine is os dependent,
# it's different for different os).
# and that version is stored in first 2 bytes of pyc file.
# f = open('test.pyc')
# f.read(4).encode('hex')
# to get current magic number of current installed python
# python -v for version and for magic number:
# import imp
# imp.get_magic().encode('hex')


# this compiler of python check syntax errors but not semantics error.
# syntax error: grammatical error like wrong keyword name, indentation error, missing bracket, etc
# example:
# print('yp!'
# semantics error: meaning of the expressions. example: wrong operation like str divide with number, operation
# in wrong order, etc.

# ways to compile python code manually:
# 1. import dis
#    def hi():
#        print('HI')
#    dis.dis(hi)

# to compile single file
# 2. python -m py_compile python_surce_file.py

# to compile all file
# 3. python -m compileall

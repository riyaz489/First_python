import unittest
import mock
from unittest.mock import MagicMock
import os
import sys


class MyTestCase(unittest.TestCase):


    def test_something(self):
        # from init_file.some_module.some_other_module.main import s
        # sys.path.append is used to help import
        # if our import is not able to find any package then we can use it, here we give absolute path of the module
        # and then we can use that package, but here it will ignore all the parent directory __init__.py
        # like if we have given path to some_module (/home/nineleaps/PycharmProjects/First/init_file/some_module)
        # then init file of some_other_module will run(but we have given
        # /home/nineleaps/PycharmProjects/First/init_file/some_module/some_other_module ) ,
        # so here it is useful when we want to import some python file using normal directory instead of python module
        # because normally python import takes only python modules not simple directory

        sys.path.append(os.getcwd())
        from main import s

        s().sd()

    #mocking __init__() method
    # @mock.patch('init_file.some_module.some_other_module.main.s.__init__', return_value=None)
    # def test_something(self, m):
    #     from init_file.some_module.some_other_module.main import s
    #     t = s()
    #     t.sd()



if __name__ == '__main__':
    unittest.main()


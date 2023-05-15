import os
from setuptools import setup, find_packages
# this file will go parallel to main project code module

# project
# ├── _code_module
# │   ├── __init__.py
# │   └── code.py
# ├── README
# ├── requirements.txt
# └── setup.py
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name='foo',
    version='1.0',
    description='A useful module',
    author='Man Foo',
    author_email='foomail@foo.com',
    python_requires='~=3.6.8',
    url='www.foo.com',
    long_description=read('README'),
    packages=find_packages(include='code_module/*',  exclude=['*.test.*']), # specify modules which u want to include and ignore
    install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies

    include_package_data=True,
    licence='copyright (c) ...',
    entry_points={'console_scripts': 'cursive = cursive.tools.cmd:cursive_command'},# this points to a function which acts as command line tool, to whoever install this package
    # format 'command_name = python_script_path:python_function_name'
    data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
                  ('config', ['cfg/data.cfg'])],  # it's a alternative of manifest.in file to include non python files
)

# to create wheel file out of this setup.py use below command:
 #pip install wheel setuptools
 # python setup.py bdist_wheel --universal
 # once wheel file is created then do pip install to install this package
 # pip install <path-to-wheelfile>

# we also directly install this package using setup.py file instead of creating wheel, in that case it will refer
# to code file directly, i.e whatever changes we do in this package will be reflected to installed package as well.
# pip install -e setup.py

# by default python  will not include non-py files while installing or building a lib/package,
# so, use manifest.in to include non python file in your final python build. just create a manifest.in
# file parallel to your setup.py file. and inside that file specify relative of non python files which you want include
# after packaging/installing current code. also in setup.py in setup function add this argument 'include_package_data=True'


# to perform before or after installation
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
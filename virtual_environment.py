## virtualenv
# creates isolated Python environments for Python libraries

# creating virtual environment using virtualenv
# 1. Enter the project folder and execute the following command:
#     “virtualenv --python=/usr/bin/python3.6 /path_to_new_venv/<environment_name>”(relevant environment name).
#      This creates an environment folder inside the mars folder.
# 2. To activate the environment we execute:
#     “source env_name/bin/activate”
#     This activates the environment.

# To create requirement.txt file first activate venv using above command, then inside your virtual environment type
# 'pip freeze > requirements.txt'
#  this command will add all the libraries and modules installed in your virtual environment into requirements.txt file.

# To install packages inside requirements.txt file type
# 'pip install -r requirements.txt'


# dir() is a special method which returns list of the attributes and methods of any object
# __dict__ return attributes in an object

## venv
# venv is a package shipped with Python 3, which you can run using `python3 -m venv  <folder path>`.
# It serves the same purpose as virtualenv, but only has a subset of its features
# few of the differences are listed below:
# 1. is slower (by not having the app-data seed method),
# 2. is not as extendable,
# 3. cannot create virtual environments for arbitrarily installed python versions (and automatically discover these),
# 4. is not upgrade-able via pip,
# 5. does not have as rich programmatic API (describe virtual environments without creating them).

## Virtaulenvwrapper
# it is basically used when your project has multiple virtual environments.
#  is a set of extensions to virtualenv

# features:
# 1. Wrappers for managing your virtual environments (create, delete, copy).
# 2. Use a single command to switch between environments.
# 3. Organizes all of your virtual environments in one place.


# to install : sudo pip install virtualenv virtualenvwrapper


# python path to specify, which python version to use for virtual env
# `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3`

# path where workon virtual env recides
# `export WORKON_HOME=~/Env`


# activate virtual env wrapper
# `source /usr/local/bin/virtualenvwrapper.sh`

# create a new virtual env in virtualenvwrapper
# `mkvirtualenv venv1`

# list packages in current virtual environment
# `lssitepackages`

# switch to other virtual env
# `workon env2`

# see current virtual env
# `echo $VIRTUAL_ENV`

# remove virtual env
# `rmvirtualenv venv1`


## pyenv
# we use pyenv, when we want to use different-different python versions.
#  For example, you may want to test your code against Python 2.7, 3.6, 3.7 and 3.8, so you'll need
#  a way to switch between them.

# using this package we can easily use newer python versions without changing python version of our OS
# and switch between different python version using global and local commands
# if we set global python version as 3.8.3 and run `python` command then it will open python 3.8.3 version interpretor.

# installation steps
# curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
# sudo apt-get update && sudo apt-get upgrade
# sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev git
#  export PATH="~/.pyenv/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

# to install a python version
#  `pyenv install 3.8.3`

# to Set  the global Python version(s)
# `pyenv global 3.8.3`
# above command will create .pyenv/version file in home directory
# if we edit version in above .pyenv/version file then global python version will also changed

# to check which python versions we can install into our system
#pyenv install - -list

# to see current global version
# `pyenv global`

# to set python version only for current folder/directory
# `pyenv local 3.8.3`
# above command will create `.python-version` file in current folder
# if we edit version in .python-version file then python version for current local folder is also changed


# show current python version
# `pyenv versions`


# Note: we can also use `pyenv-virtualenv` or `pyenv-virtualenvwrapper` (these 2 pacakages are created by same
# author who developed pyenv).


## pipenv
# If your project depends on Python package versions and its dependencies, pipenv is for you.
# here instead of requirements.txt, pipenv creates a Pipfile.lock and you use it when you move to a different system.
# The Pipfile.lock contains all the dependencies and its versions.
# When you install Python packages using Pipfile.lock, it will create exactly the same environment as your original
# system.

# here  pip and virtualenv working together
# Automatically loads .env files, if they exist.

# The requirements.txt file doesn’t specify which version of package to use.
# In this case, pip install -r requirements.txt will install the latest version by default

# installation
#  pip install pipenv

# create virtual environment
# `pipenv --python 3.7`
# the above command will create pip file in current directory and virtual environment in standard location

# to install package with specific version
# pipenv install django==2.0.7

# to install package
# pipenv install django

# to uninstall
# pipenv uninstall django

# to update all/specific packages
# pipenv update
# pipenv update django

# to install all packages specified in pip file
# if version is not specified in pip file, then new version of the dependency will be installed in your
# development environment.
# pipenv install
# to install dev packages also
# pipenv install --dev

# to remove all packages
# pipenv uninstall --all

# to create a pip lock file for production
# pipenv lock
# note: copy pipfile and pipfile.lock into production

# to install lock file in production
# pipenv install --ignore-pipfile
# it will ignore pipfile and install packages from lock file

# to install dev packages also from lock file
#  pipenv install --ignore-pipfile --dev

# to install packages only for dev environment
# pipenv install pytest --dev


# to install requirement.txt file
# pipenv install -r requirements.txt
# note: do not use requirement.txt file(above step is only mentioned for learning purpose)

# to open shell in current virtual environment
# pipenv shell
# and type `exit` to deactivate virtualenv.

# to run command in virtual environment
# pipenv run <command> <args>
# some examples below:
# pipenv run pip freeze
# pipenv run python

# best practice: we can install any version of python using pyenv and use `local` command to set that python version
# into our project folder and then we can use pipenv to create python virtual environment.

import pytest
from my_python_package_scaffold import say_hello

def say_hello_test():
    assert say_hello == 'hello from my package!'

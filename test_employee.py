from employee import Employee
import pytest

import requests
# assert A ==B
# assert A is True
# assert A in B
# assert A != B
# assert A is False
# assert A not in B

#pytest中测试文件名要以"test_"开头或结尾，且后缀为.py
#测试文件中的测试函数名要以"test_"开头


@pytest.fixture

def example_employee():
    example_employee = Employee("xiaoming", "张", 150000)
    return example_employee

def test_give_default_raise(example_employee):
    #example_employee = Employee("xiaoming","张",150000)
    example_employee.give_raise()
    assert example_employee.salary==155000

def test_give_custom_raise(example_employee):
    #example_employee = Employee("xiaoming", "张", 150000)
    example_employee.give_raise(10000)
    assert example_employee.salary == 160000
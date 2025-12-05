import pytest 
from employee import Employee

@pytest.fixture
def employee_example():
    #instance avaialble for all tests
    return Employee('Steve', 'Howard', 50000)

def test_give_default_raise(employee_example):
    employee_example.give_raise()
    assert employee_example.annual_salary == 55000

def test_give_custom_raise(employee_example):
    employee_example.give_raise(1000)
    assert employee_example.annual_salary == 51000
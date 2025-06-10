'''from my_project.calculator import Calculator

def test_addition():
    calculetion: Calculator = Calculator(10,5)
    assert calculetion.addition() == 13, 'The sum is wrong'

def test_subtraction():
    calculetion: Calculator = Calculator(10,5)
    assert calculetion.subtraction() == 5, 'The subtraction is wrong'

def test_multiplication():
    calculetion: Calculator = Calculator(10,5)
    assert calculetion.multiplication() == 50, 'The multiplication is wrong'

def test_division():
    calculetion: Calculator = Calculator(10,5)
    assert calculetion.division() == 2.00, 'The quotient is wrong'''

from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    #creates a fresh istance of Calculator beforeach test
    return Calculator(10,5)

def test_addition(calculation):
    assert calculation.addition() == 15, 'The sum is wrong'

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, 'The subtraction in wrong'

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, 'The multiplication in wrong'

def test_division(calculation):
    assert calculation.division() == 2.00, 'The quotient in wrong'



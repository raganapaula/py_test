import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculadora import Calculadora

def test_soma():
    calc = Calculadora()
    assert calc.somar(2,2) == 4

def test_somar_negat():
    calc = Calculadora()
    assert calc.somar(-1,-1) == -2   

def test_subtrair():
    calc = Calculadora()
    assert calc.subtrair(2,2) == 0

def test_subtrair1():
    calc = Calculadora()
    assert calc.subtrair(0,5) == -5

def test_subtrair2():
    calc = Calculadora()
    assert calc.subtrair(-2,-3) == 1

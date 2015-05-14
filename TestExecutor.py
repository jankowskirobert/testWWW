'''
Created on May 13, 2015

@author: tester
'''
import pytest
from Executor import fooReturnFive, fooReturnSix



def test_five():
    assert fooReturnFive == 5
def test_six():
    assert fooReturnSix == 6

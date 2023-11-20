import pytest

from fibonacci import fibonacci_iterative
    
def test_fibonacci_1_is_1():
    assert fibonacci_iterative(1) == 1

def test_fibonacci_9_is_34():
    assert fibonacci_iterative(9) == 37

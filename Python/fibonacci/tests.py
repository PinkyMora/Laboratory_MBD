import time

from fibonacci import fibonacci_recursive_memory as fib

def test_fibonacci_0():
    assert fib(0) == 0

def test_fibonacci_1():
    assert fib(1) == 1
    
def test_fibonacci_9():
    assert fib(9) == 34

    
def test_fibonacci_12():
    assert fib(12) == 144

def test_fibonacci_222():
    assert fib(222) == 11111460156937785151929026842503960837766832936

def test_fibonacci_500():
    assert fib(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125

def test_fibonacci_1001():
    assert fib(1001) == 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501

start = time.time_ns()

test_fibonacci_0()
test_fibonacci_1()

test_fibonacci_9()
test_fibonacci_12()

test_fibonacci_222()

test_fibonacci_500()

test_fibonacci_1001()

end = time.time_ns()
print("Ha tardado: ", end-start)
print("Todo Okay!")
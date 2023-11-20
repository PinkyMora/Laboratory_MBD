import argparse
import functools

#try:
#    from super_fibonacci import fibonacci_fast 
#except Exception as err:
#    pass

def fibonacci_iterative(n: int):
    """Implementacion basica de la secuencia Fibonacci de forma iterativa

    Args:
        n (int): Elemento de la secuencia de Fibonacci a calcular

    Returns:
        int: Valor de la secuencia de Fibonacci en la posicion `n`
    """
    if n < 0:
        raise ValueError("The parameter n must be greater than 0")
    
    if n<2:
        return n
    
    n1 = 0
    n2 = 1

    for _ in range(n):
        nth = n1 + n2

        n1 = n2
        n2 = nth

    return n1

@functools.cache
def fibonacci_recursive(n):

    if n < 0:
        raise ValueError("The parameter n must be greater than 0")
    
    if n < 2:
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

cache = {}
def fibonacci_recursive_memory(n):

    if n < 0:
        raise ValueError("The parameter n must be greater than 0")
    
    if n < 2:
        return n
    
    if n in cache:
        return cache[n]
    
    nth =  fibonacci_recursive_memory(n-1) + fibonacci_recursive_memory(n-2)

    cache[n] = nth

    return nth

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="The number to retrieve in the fibonacci sequence")

    parser.add_argument("-i", "--implementation", type=str, choices=["iterative", "recursive","rcsv_memory"])

    args = parser.parse_args()

    result = None
    match args.implementation:
        case "iterative":
            result = fibonacci(args.n)
        case "recursive":
            result = fibonacci_recursive(args.n)
        case "rcsv_memory":
            result = fibonacci_recursive_memory(args.n)
        case _:
            raise ValueError("Implementation not defined", args.implementation)
    

    print(fibonacci_recursive_memory(args.n))
import multiprocessing
import time

def sum_of_squares(list_numbers):
    output =  0
    for i in list_numbers:
        output += i*i
    return output #sum(x*x for x in list_numbers)

if __name__ == "__main__":

    input_ = [range(1000000000)]

    start = time.time()

    num_processes = 4

    chunk_size = int((len(input_) / num_processes) *100)

    chunks = [input_[i:i + chunk_size] for i in range(0, len(input_), chunk_size)]

    with multiprocessing.Pool(num_processes) as pool:
        cuadrados = pool.map(sum_of_squares,input_)

    resultado = sum(cuadrados)

    print(resultado)

    end = time.time()

    print("Time spent: "+str(end - start))
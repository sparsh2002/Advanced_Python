from multiprocessing import Pool
import time

def square(numbers , queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers , queue):
    for i in numbers:
        queue.put(-i)

def cube(number):
    return number*number*number

if __name__ == '__main__':
    numbers = range(10)
    pool = Pool()
    # map, apply , join , close
    result=pool.map(cube ,numbers)
    # pool.apply(cube , numbers[0])
    pool.close()

    pool.join()

    print(result)


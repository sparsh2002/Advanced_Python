from multiprocessing import Process , Value  , Array, Lock
import time

def add_100(number , lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == '__main__':
    shared_number = Value('i', 0)
    print('Number at the beginning is' , shared_number.value)
    lock  = Lock()
    p1 = Process(target=add_100 , args=(shared_number,lock))
    p2 = Process(target=add_100 , args=(shared_number,lock))
    

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is' , shared_number.value)
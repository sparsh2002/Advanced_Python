from threading import Thread

def square_numbers():
    for i in range(100):
        i*i
        


if __name__ == "__main__":
    print('start')
    threads = []

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()

    # join threads : wait for them to complete
    for thread in threads:
        thread.join()

    print('end main')

    

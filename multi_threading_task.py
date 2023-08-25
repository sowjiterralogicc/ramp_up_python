# import time
# import multiprocessing
# start=time.perf_counter()
# def do_somthing():
#     print("sleep 1 seconds")
#     time.sleep(1)
#     print("Done sleeping")
# do_somthing()
# do_somthing()
# finish=time.perf_counter()
# print(f'finished in {round(finish-start, 2)} second(s)')



# import time
# import multiprocessing
# start=time.perf_counter()
# def do_something():
#     print("sleeping for 1 sec")
#     time.sleep(1)
#     print("sleeping Done")
# if __name__ == '__main__':
#     multiprocessing.freeze_support()  
#     start = time.perf_counter()
#     p1 = multiprocessing.Process(target=do_something)
#     p2 = multiprocessing.Process(target=do_something)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     finish = time.perf_counter()
#     print(f'finished in {round(finish - start, 2)} second(s)')

# import time
# import multiprocessing
# start=time.perf_counter()
# def do_something():
#     print("sleeping for 1 sec")
#     time.sleep(1)
#     print("sleeping Done")
# l1=[]
# for _ in range(10):
#      if __name__ == '__main__':
#         multiprocessing.freeze_support()  
#         start = time.perf_counter()
#         p1 = multiprocessing.Process(target=do_something)
#         #p2 = multiprocessing.Process(target=do_something)
#         p1.start()
#         #p1.join()
#         l1.append(p1)
# for process in l1:
#         process.join()
# finish = time.perf_counter()
# print(f'finished in {round(finish - start, 2)} second(s)')

import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue
import time

logging.basicConfig(
    format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f"{processname}\{threadname}:{msg}")

def create_work(queue, finished, max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1, 100)
        queue.put(v)
        display(f'producing {x}: {v}')
    finished.put(True)
    display("finished")

def perform_work(work, finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'consuming {counter}: {v}')
            counter += 1
        else:
            q = finished.get()
            if q == True:
                break
            display("finished")

def main():
    max = int(input("Enter the maximum value for the queue: "))
    work = Queue()
    finished = Queue()

    producer = Thread(target=create_work, args=[work, finished, max])
    consumer = Thread(target=perform_work, args=[work, finished])

    # Start threads after input is received
    producer.start()
    consumer.start()

    producer.join()
    display("producer has finished")
    consumer.join()
    display("consumer has finished")

if __name__ == "__main__":
    main()
    logging.shutdown()



#In summary,
# this code showcases the use of threads to implement a simple producer-consumer scenario,
# where the producer generates random numbers and the consumer consumes them from a shared queue.
# The logging statements provide insight into the activities of the producer and consumer threads.



# import random
# import threading
# import multiprocessing
# import logging
# from threading import Thread
# from queue import Queue
# import time
# logging.basicConfig(
#     format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',
#     datefmt='%H:%M:%S',
#     level=logging.DEBUG
# )
# lock = threading.Lock()  # Lock for shared resources
# def display(msg):
#     threadname=threading.current_thread().name
#     processname=multiprocessing.current_process().name
#     logging.info(f"{processname}\{threadname}:{msg}")
# def create_work(queue,finished,max):
#     #finished.put(False)
#     for x in range(max):
#         v=random.randint(1,100)
#         queue.put(v)   #adding random values to the queue
#         display(f'producing {x}: {v}')
#     #finished.put(True)
#     display("finished")
# def perform_work(work,finished):
#     counter=0
#     while True:
#         if not work.empty():   #checking if the queue is not emplty and consuming the items
#             v = work.get()
#             display(f'consuming {counter}: {v}')
#             counter=counter+1
#         else:
#             q = finished.get()
#             if q == True:
#                 break
#             display("finished")
# def main():     #The main function is responsible for creating and managing the producer and consumer threads.It creates queues for communication between threads.
#     max = int(input("Enter the maximum value for the queue: "))
#     num_consumers = int(input("Enter the number of consumer threads: "))
#     work = Queue()
#     finished = Queue()
#     producer = Thread(target=create_work,args=[work,finished,max])
    
#     work = Queue()
#     finished = Queue()
    
#     producer = Thread(target=create_work, args=[work, finished, max])
#     consumers = [Thread(target=perform_work, args=[work, finished]) for _ in range(num_consumers)]
    
#     producer.start()
#     for consumer in consumers:
#         consumer.start()
        
#     producer.join()
#     for consumer in consumers:
#         consumer.join()
        
#     display("producer has finished")
#     display("consumers have finished")

# if __name__=="__main__":
#     main()
#     logging.shutdown() 
    




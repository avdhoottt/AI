import threading as thread
import random
import time

queue = []
QAvail = thread.Semaphore(1)
Davail = thread.Semaphore(0)

def producer():
    nums = range(5)
    global queue
    while True:
        num = random.choice(nums)
        QAvail.acquire()
        queue.append(num)
        print("Produced", num, queue)
        Davail.release()
        time.sleep(random.randrange(0, 3))

def consumer():
    global queue
    while True:
        Davail.acquire()
        num = queue.pop(0)
        print("Consumed", num, queue)
        QAvail.release()
        time.sleep(random.randrange(0, 3))

producerThread = thread.Thread(target=producer)
consumerThread = thread.Thread(target=consumer)

producerThread.start()
consumerThread.start()
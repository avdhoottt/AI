import threading as thread
import random
import time

queue = []
Q = thread.Semaphore(1)
D = thread.Semaphore(0)

def producer():
    global queue
    nums = range(5)
    while True:
        num = random.choice(nums)
        Q.acquire()
        queue.append(num)
        print("Produced: ", num, queue)
        D.release()
        time.sleep(random.randrange(0, 3))
def consumer():
    global queue
    while True:
        D.acquire()
        num = queue.pop(0)
        print("COnsumed: ", num, queue)
        Q.release()
        time.sleep((random.randrange(0, 3)))
pthread = thread.Thread(target=producer)
cthread = thread.Thread(target=consumer)
pthread.start()
cthread.start()
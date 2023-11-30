import threading as thread
import random 

global x
x = 0
lock = thread.Lock()

def reader():
    global x
    print("reader is reading")
    lock.acquire()
    print("Shared data: ", x)
    lock.release()
    print()
    
def writer():
    global x
    print("Writer is writing")
    lock.acquire()
    x += 1
    print("Writer is realeasing the Resource")
    lock.release()
    print()
    
if __name__ == '__main__':
    for i in range(0, 10):
        rando = random.randint(0, 100)
        if(rando > 50):
            thread1 = thread.Thread(target = reader)
            thread1.start()
        else:
            thread2 = thread.Thread(target=writer)
            thread2.start()
thread1.join()
thread2.join()    
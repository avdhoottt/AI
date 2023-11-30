import threading as thread
import random 

global x
x = 0
lock = thread.Lock()

def reader():
    global x
    print("Reader is reading!!")
    lock.acquire()
    print("Shared Data: ", x)
    lock.release()
     
def writer():
    global x
    print("Writer is writing")
    lock.acquire()
    x += 1
    print("Writer is releasing")
    lock.release()
    
if __name__=='__main__':
    for i in range(0, 10):
        rando = random.randint(0, 100)
        if rando > 50:
            rthread = thread.Thread(target=reader)
            rthread.start()
        else:
            wthread = thread.Thread(target=writer)
            wthread.start()
            
rthread.join()
wthread.join()
    
    
    
from queue import Queue

def pageF(incomingStream, n, frames):
    print("Incoming \t Pages")
    s = set()
    queue = Queue()
    page_f = 0
    
    for i in range(n):
        if len(s) < frames:
            if incomingStream[i] not in s:
                s.add(incomingStream[i])
                page_f += 1
                queue.put(incomingStream[i])
        else:
            if incomingStream[i] not in s:
                val = queue.queue[0]
                queue.get()
                s.remove(val)
                s.add(incomingStream[i])
                queue.put(incomingStream[i])
                page_f += 1
        print(incomingStream[i], end="\t\t")
        for q in s:
            print(q, end="\t")
        print()
    return page_f

                

incomingStream = [1, 3, 0, 3, 5, 6, 3]
frames = 3
n = len(incomingStream)
page_faults = pageF(incomingStream, n, frames)
hits = n - page_faults

print(f"Page Faults : {page_faults}")
print(f"Hits : {hits}")
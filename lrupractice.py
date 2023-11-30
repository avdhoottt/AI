def pageF(incomingstream, n, frames):
    s = set()
    Indexes = {}
    page_f = 0
    
    for i in range(n):
        if len(s) < frames:
            if incomingstream[i] not in s:
                s.add(incomingstream[i])
                page_f += 1
                Indexes[incomingstream[i]] = i
        else:
            if incomingstream[i] not in s:
                lru = float('inf')
                victim = None
                for p in s:
                    if Indexes[p] < lru:
                        lru = Indexes[p]
                        victim = p
                s.remove(victim)
                s.add(incomingstream[i])
                page_f += 1
            Indexes[incomingstream[i]] = i
            
    return page_f

incomingStream = [1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]
frames = 3
n = len(incomingStream)
page_f = pageF(incomingStream, n, frames)
hits = n - page_f
print(f"PF: {page_f}")
print(f"Hits: {hits}")

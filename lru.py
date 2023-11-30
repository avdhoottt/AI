def pageFaults(incomingStream, n, frames):
    s = set()
    indexes = {}

    page_faults = 0
    for i in range(n):
        if len(s) < frames:
            if incomingStream[i] not in s:
                s.add(incomingStream[i])
                page_faults += 1
            indexes[incomingStream[i]] = i
        else:
            if incomingStream[i] not in s:
                lru = float('inf')
                victim_page = None
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        victim_page = page

                s.remove(victim_page)
                s.add(incomingStream[i])
                page_faults += 1

                

            indexes[incomingStream[i]] = i

    return page_faults

incomingStream = [1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]
n = len(incomingStream)
frames = 3
page_faults = pageFaults(incomingStream, n, frames)
hits = n - page_faults

print("\nPage Faults:", page_faults)
print("Hit:", hits)

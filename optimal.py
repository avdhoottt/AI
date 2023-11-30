def pageFaults(incomingStream, n, frames):
    indexes = {}
    page_faults = 0

    for i in range(n):
        if len(indexes) < frames:
            indexes[incomingStream[i]] = i
            page_faults += 1
        else:
            if incomingStream[i] not in indexes:
                farthest_future = -1
                page_to_replace = None

                for page, index in indexes.items():
                    future_occurrence = float('inf')
                    for j in range(i + 1, n):
                        if incomingStream[j] == page:
                            future_occurrence = j
                            break

                    if future_occurrence > farthest_future:
                        farthest_future = future_occurrence
                        page_to_replace = page

                indexes.pop(page_to_replace)
                indexes[incomingStream[i]] = i
                page_faults += 1

    return page_faults

incomingStream = [1, 7, 8, 3, 0, 2, 0, 3, 5, 4, 0, 6, 1]
n = len(incomingStream)
frames = 3
page_faults = pageFaults(incomingStream, n, frames)
hits = n - page_faults

print("\nPage Faults:", page_faults)
print("Hit:", hits)

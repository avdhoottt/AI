no_p = 5
no_r = 3

allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

available = [3, 3, 2]

needed = [[maximum[i][j] - allocated[i][j] for j in range(no_r)] for i in range(no_p)]
visited = [False] * no_p
safe_sequence = []
work = available[:]

while True:
    found = False
    for i in range(no_p):
        if not visited[i] and all(needed[i][j] <= work[j] for j in range(no_r)):
            work = [work[j] + allocated[i][j] for j in range(no_r)]
            safe_sequence.append(i)
            visited[i] = True
            found = True
            
    if not found:
        break


if len(safe_sequence) == no_p:
    print("The System is safe")
    print("Safe Sequence: ", safe_sequence)
    print("Available Resources: ", available)
else:
    print("The system is unsafe")
def sjf(processes):
    n = len(processes)
    processes.sort(key=lambda x:(x['arrival_time'], x['burst_time']))
    
    tats = [0] * n
    wts = [0] * n
    cts = [0] * n
    current_time = 0 
    completed = [False] * n
    Tcompletion = 0
    
    while Tcompletion < n:
        min_burst = float('inf')
        shortest = None
        
        for i in range(n):
            if not completed[i] and processes[i]['arrival_time'] <= current_time:
                if processes[i]['burst_time'] < min_burst:
                    min_burst = processes[i]['burst_time']
                    shortest = i
                    
        if shortest is None:
            current_time += 1
            continue
        
        current_time += processes[shortest]['burst_time']
        tats[shortest] = current_time - processes[shortest]['arrival_time']
        wts[shortest] = tats[shortest] - processes[shortest]['burst_time']
        cts[shortest] = current_time
        completed[shortest] = True
        Tcompletion += 1
        
    for i in range(n):
        print(f"{processes[i]['id']} \t {tats[i]} \t {wts[i]} \t {cts[i]}")
        
    avg_tat = sum(tats)/n
    avg_wts = sum(wts)/n
    
    print(f"Avg. Tats: {avg_tat}")
    print(f"Avg. Wtts: {avg_wts}")


if __name__=='__main__':
    processes= [
        {'id': '1', 'arrival_time': 1, 'burst_time': 7},
        {'id': '2', 'arrival_time': 3, 'burst_time': 3},
        {'id': '3', 'arrival_time': 6, 'burst_time': 2},
        {'id': '4', 'arrival_time': 7, 'burst_time': 10},
        {'id': '5', 'arrival_time': 9, 'burst_time': 8}
    ]
    
    sjf(processes)
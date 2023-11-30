def fifo(data):
    current_time = 0
    tats = []
    wts = []
    
    for p in data:
        wt = max(0, current_time - p['arrival_time'])
        tat = wt + p['burst_time']
        ct = current_time + p['burst_time']
        
        tats.append(tat)
        wts.append(wt)
        
        print(f"{p['id']} \t\t {tat} \t\t\t {wt} \t\t {ct}")
        current_time = ct
    avg_tat = sum(tats)/len(tats)
    avg_wt = sum(wts)/len(wts)

    print(f"AVG TAT: {avg_tat}")
    print(f"AVG WT: {avg_wt}")


if __name__=='__main__':
    data = [
        {'id': '1', 'arrival_time': 0, 'burst_time': 9},
        {'id': '2', 'arrival_time': 1, 'burst_time': 3},
        {'id': '3', 'arrival_time': 1, 'burst_time': 2},
        {'id': '4', 'arrival_time': 1, 'burst_time': 4},
        {'id': '5', 'arrival_time': 2, 'burst_time': 3},
        {'id': '6', 'arrival_time': 3, 'burst_time': 2},
    ]
    
    fifo(data)
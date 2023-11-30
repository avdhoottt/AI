def sjf_scheduler(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))

    # Initialize variables to store turnaround, waiting, and completion times
    turnaround_times = [0] * n
    waiting_times = [0] * n
    completion_times = [0] * n
    completed = [False] * n
    current_time = 0
    total_completion = 0

    while total_completion < n:
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

        # Process execution
        current_time += processes[shortest]['burst_time']
        turnaround_times[shortest] = current_time - processes[shortest]['arrival_time']
        waiting_times[shortest] = turnaround_times[shortest] - processes[shortest]['burst_time']
        completion_times[shortest] = current_time
        completed[shortest] = True
        total_completion += 1

    # Display process details including completion time and average times
    for i in range(n):
        print(f"Process {processes[i]['id']} - Turnaround Time: {turnaround_times[i]}, Waiting Time: {waiting_times[i]}, Completion Time: {completion_times[i]}")

    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n

    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")

if __name__ == "__main__":
    processes = [
        {'id': '1', 'arrival_time': 1, 'burst_time': 7},
        {'id': '2', 'arrival_time': 3, 'burst_time': 3},
        {'id': '3', 'arrival_time': 6, 'burst_time': 2},
        {'id': '4', 'arrival_time': 7, 'burst_time': 10},
        {'id': '5', 'arrival_time': 9, 'burst_time': 8}
    ]

    sjf_scheduler(processes)

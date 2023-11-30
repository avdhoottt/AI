def fifo_scheduler(data):
    current_time = 0
    turnaround_times = []
    waiting_times = []

    for process in data:
        waiting_time = max(0, current_time - process['arrival_time'])
        turnaround_time = waiting_time + process['burst_time']
        completion_time = current_time + process['burst_time']

        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

        print(f"Process {process['id']} - Turnaround Time: {turnaround_time}, Waiting Time: {waiting_time}, Completion Time: {completion_time}")
        
        current_time = completion_time

    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    avg_waiting_time = sum(waiting_times) / len(waiting_times)

    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")

if __name__ == "__main__":
    data = [
        {'id': '1', 'arrival_time': 0, 'burst_time': 9},
        {'id': '2', 'arrival_time': 1, 'burst_time': 3},
        {'id': '3', 'arrival_time': 1, 'burst_time': 2},
        {'id': '4', 'arrival_time': 1, 'burst_time': 4},
        {'id': '4', 'arrival_time': 2, 'burst_time': 3},
        {'id': '4', 'arrival_time': 3, 'burst_time': 2}
    ]

    fifo_scheduler(data)

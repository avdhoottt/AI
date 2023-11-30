def round_robin_scheduler(data, time_quantum):
    remaining_time = [process['burst_time'] for process in data]
    n = len(data)
    completion_time = [0] * n
    turnaround_times = []
    waiting_times = [0] * n

    current_time = 0
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    current_time += remaining_time[i]
                    waiting_times[i] = max(0, current_time - data[i]['arrival_time'] - data[i]['burst_time'])
                    remaining_time[i] = 0
                    completion_time[i] = current_time
                    turnaround_times.append(waiting_times[i] + data[i]['burst_time'])

        if done:
            break

    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n

    for i in range(n):
        print(f"Process {data[i]['id']} - Turnaround Time: {turnaround_times[i] + data[i]['burst_time']}, Waiting Time: {waiting_times[i]}, Completion Time: {completion_time[i]}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")

if __name__ == "__main__":
    data = [
        {'id': '1', 'arrival_time': 0, 'burst_time': 7},
        {'id': '2', 'arrival_time': 1, 'burst_time': 4},
        {'id': '3', 'arrival_time': 2, 'burst_time': 15},
        {'id': '4', 'arrival_time': 3, 'burst_time': 11},
        {'id': '5', 'arrival_time': 4, 'burst_time': 20},
        {'id': '6', 'arrival_time': 4, 'burst_time': 9}
    ]
    time_quantum = 5

    round_robin_scheduler(data, time_quantum)

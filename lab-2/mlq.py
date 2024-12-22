class Process:
    def __init__(self, id, arrival_time, burst_time, priority=0):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __repr__(self):
        return f"Process(id={self.id}, arrival_time={self.arrival_time}, burst_time={self.burst_time}, priority={self.priority})"


class CPUScheduler:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def fcfs(self):
        print("\nFCFS Scheduling")
        self.processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
        current_time = 0
        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time += process.burst_time
            self._print_process_stats(process)

    def sjn(self):
        print("\nSJN Scheduling")
        self.processes.sort(key=lambda p: (p.arrival_time, p.burst_time))  # Sort by arrival time and burst time
        current_time = 0
        completed = []
        while len(completed) < len(self.processes):
            ready_queue = [p for p in self.processes if p.arrival_time <= current_time and p not in completed]
            if not ready_queue:
                current_time += 1
                continue
            shortest_job = min(ready_queue, key=lambda p: p.burst_time)
            shortest_job.completion_time = current_time + shortest_job.burst_time
            shortest_job.turnaround_time = shortest_job.completion_time - shortest_job.arrival_time
            shortest_job.waiting_time = shortest_job.turnaround_time - shortest_job.burst_time
            current_time += shortest_job.burst_time
            completed.append(shortest_job)
            self._print_process_stats(shortest_job)

    def round_robin(self, quantum):
        print("\nRound-Robin Scheduling")
        queue = sorted(self.processes, key=lambda p: p.arrival_time)  # Sort by arrival time
        current_time = 0
        while queue:
            process = queue.pop(0)
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            time_slice = min(process.remaining_time, quantum)
            process.remaining_time -= time_slice
            current_time += time_slice
            if process.remaining_time == 0:
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                self._print_process_stats(process)
            else:
                queue.append(process)

    def priority_scheduling(self):
        print("\nPriority Scheduling")
        self.processes.sort(key=lambda p: (p.arrival_time, p.priority))  # Sort by arrival time and priority
        current_time = 0
        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time += process.burst_time
            self._print_process_stats(process)

    def _print_process_stats(self, process):
        print(f"Process {process.id}: Completion Time = {process.completion_time}, "
              f"Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")



# Example Usage
if __name__ == "__main__":
    scheduler = CPUScheduler()

    # Adding processes
    scheduler.add_process(Process(1, 0, 8, priority=3))
    scheduler.add_process(Process(2, 1, 4, priority=1))
    scheduler.add_process(Process(3, 2, 9, priority=2))
    scheduler.add_process(Process(4, 3, 5, priority=4))

    # Execute different scheduling schemes
    scheduler.fcfs()
    scheduler.sjn()
    scheduler.round_robin(quantum=3)
    scheduler.priority_scheduling()
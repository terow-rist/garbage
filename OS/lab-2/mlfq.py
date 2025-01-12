class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __repr__(self):
        return f"Process(id={self.id}, arrival_time={self.arrival_time}, burst_time={self.burst_time})"


class MLFQScheduler:
    def __init__(self, num_queues, time_quantums):
        self.queues = [list() for _ in range(num_queues)]
        self.time_quantums = time_quantums
        self.current_time = 0
        self.completed_processes = []

    def add_process(self, process):
        self.queues[0].append(process)  

    def run(self):
        print("\nMLFQ Scheduling:")
        while any(self.queues):  
            for i, queue in enumerate(self.queues):
                if queue:
                    self._execute_queue(queue, self.time_quantums[i])
                    break

    def _execute_queue(self, queue, quantum):
        process = queue.pop(0)
        time_slice = min(process.remaining_time, quantum)

        print(f"Running process {process.id} from Queue-{self.queues.index(queue) + 1} "
              f"for {time_slice} units (remaining time: {process.remaining_time})")

        self.current_time += time_slice
        process.remaining_time -= time_slice

        if process.remaining_time == 0:
            process.completion_time = self.current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            self.completed_processes.append(process)
            print(f"Process {process.id} completed at time {self.current_time}")
        else:
            if self.queues.index(queue) + 1 < len(self.queues):
                self.queues[self.queues.index(queue) + 1].append(process)
                print(f"Process {process.id} moved to Queue-{self.queues.index(queue) + 2}")
            else:
                queue.append(process)  
                print(f"Process {process.id} stays in Queue-{len(self.queues)}")

    def print_stats(self):
        print("\nProcess Stats:")
        for process in self.completed_processes:
            print(f"Process {process.id}: Completion Time = {process.completion_time}, "
                  f"Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")


if __name__ == "__main__":
    scheduler = MLFQScheduler(num_queues=3, time_quantums=[4, 8, 16])

    scheduler.add_process(Process(1, 0, 10))
    scheduler.add_process(Process(2, 1, 15))
    scheduler.add_process(Process(3, 2, 20))

    scheduler.run()
    scheduler.print_stats()
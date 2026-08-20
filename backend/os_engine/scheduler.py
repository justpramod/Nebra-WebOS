from collections import deque
from dataclasses import dataclass, field

from os_engine.process import Process


@dataclass()
class Scheduler:
    ready_queue: deque[Process] = field(default_factory=lambda: deque())

    # a dict with pid as key that maps to the process
    waiting_process: dict[int, Process] = field(default_factory=lambda: {})

    def get_next_ready(self) -> Process | None:
        """
        FCFS implementation which pops the first process from ready_queue and returns it to kernel.
        """
        if not self.ready_queue:
            # if there are not process in ready_queue return None to kernel to run a idle process
            return None

        popped_process: Process = self.ready_queue.popleft()
        return popped_process

    def enqueue_ready(self, process: Process):
        """
        Enqueues the process into the ready_queue
        """
        self.ready_queue.append(process)

    def add_waiting(self, process: Process):
        """
        Adds the blocked process into the waiting_process dict.
        """
        self.waiting_process[process.process_id] = process

    def mark_ready(self, process_id: int):
        """
        Removes the process from waiting_process and moves to ready_queue.
        """
        process: Process | None = self.waiting_process.pop(process_id, None)

        if process is None:  # handle if the blocked process is not on list.
            print("Process with that pid not found int eh waiting_process dict.")
            pass

        else:
            self.ready_queue.append(process)

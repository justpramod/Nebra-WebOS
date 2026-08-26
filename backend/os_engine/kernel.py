from os_engine.isa import Instruction, Opcode
from os_engine.process import Process, ProcessState
from os_engine.scheduler import Scheduler


class Kernel:
    def __init__(self) -> None:
        # initialize scheduler
        scheduler: Scheduler = Scheduler()

        # initialize the first process systemd
        systemd_process: Process = Process(
            process_id=1,
            process_state=ProcessState.RUNNING,
            saved_program_counter_value=0,
            saved_register_values=[0, 0, 0, 0],
            # the instructions are hardcoded now, but will be memory address later when MMU is implemented
            instructions=[
                Instruction(opcode=Opcode.ADD, operands=["R0", "R1", "R2"]),
                Instruction(opcode=Opcode.HALT, operands=[]),
            ],
        )

        self.current_process: Process = systemd_process
        self.scheduler : Scheduler = scheduler

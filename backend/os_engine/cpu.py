from dataclasses import dataclass, field

from os_engine.opcode_handlers import OPCODE_HANDLERS
from os_engine.process import Process


@dataclass()
class CPU:
    program_counter: int = 0
    registers: list = field(
        default_factory=lambda: [0, 0, 0, 0]
    )  # using field instead of = [0,0,0,0] will avoid all objects pointing to same list.

    def fetch_one_instruction(self, process):
        # for now fetch and decode are in the execute until a proper memory mangaement unit is implemented.
        pass

    def decode_one_instruction(self):
        pass

    def execute_one_instruction(self, process: Process):
        instruction = process.instructions[self.program_counter]
        handler = OPCODE_HANDLERS[instruction.opcode]
        handler(self, process, instruction.operands)

    def increment_one_tick(self):
        pass

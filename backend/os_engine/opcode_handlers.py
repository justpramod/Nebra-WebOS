from os_engine.isa import Opcode
from os_engine.process import ProcessState
from os_engine.utils import reg_index


def handle_add(cpu, process, operands: list):
    r0, r1, r2 = operands

    cpu.registers[reg_index(r0)] = (
        cpu.registers[reg_index(r1)] + cpu.registers[reg_index(r2)]
    )

    cpu.program_counter += 1


def handle_subtract(cpu, process, operands: list):
    r0, r1, r2 = operands

    cpu.registers[reg_index(r0)] = (
        cpu.registers[reg_index(r1)] - cpu.registers[reg_index(r2)]
    )

    cpu.program_counter += 1


def handle_halt(cpu, process, operands: list):
    # syscall to kernel, which reclaims its resources. implement later.
    process.transition_to(ProcessState.TERMINATED)


OPCODE_HANDLERS = {
    Opcode.ADD: handle_add,
    Opcode.HALT: handle_halt,
    Opcode.SUBTRACT: handle_subtract,
}

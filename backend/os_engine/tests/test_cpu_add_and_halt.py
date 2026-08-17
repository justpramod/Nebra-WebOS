from os_engine.cpu import CPU
from os_engine.isa import Instruction, Opcode
from os_engine.process import Process, ProcessState


def test_cpu_add_and_halt():
    proc = Process(
        process_id=1,
        process_state=ProcessState.RUNNING,
        saved_program_counter_value=0,
        saved_register_values=[0, 5, 3, 0],
        instructions=[
            Instruction(opcode=Opcode.ADD, operands=["R0", "R1", "R2"]),
            Instruction(opcode=Opcode.HALT, operands=[]),
        ],
    )

    cpu = CPU()
    # restore process values, done in kernel mode
    cpu.program_counter = proc.saved_program_counter_value
    cpu.registers = proc.saved_register_values.copy()

    cpu.execute_one_instruction(process=proc)

    assert cpu.registers[0] == 8
    assert cpu.program_counter == 1

    cpu.execute_one_instruction(process=proc)
    assert proc.process_state == ProcessState.TERMINATED

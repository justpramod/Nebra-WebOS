"""Instruction set architecture:
- commands that CPU understands.
"""

from dataclasses import dataclass
from enum import Enum, auto


class Opcode(Enum):
    ADD = auto()
    HALT = auto()
    SUBTRACT = auto()


@dataclass()
class Instruction:
    opcode: Opcode
    operands: list

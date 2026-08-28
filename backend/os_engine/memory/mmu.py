"""
A hardware which is responsible for translating virtual memory address to physical memory address.
also enforces the protection of memory by checking flag rules from page table entry.
"""

from os_engine.memory.pte import PTE
from os_engine.memory.ram import RAM


class MMU:
    @staticmethod
    def translate(
        virtual_address: int,
        page_table_pointer: int,
        ram: RAM,
    ):
        # page_table_pointer points dirextly to the RAM's physical address

        # width of each page table entry is 3 bytes
        pte_width = 3

        # get the virtual page number and page offset from the virtual_address

        virtual_page_number: int = (
            virtual_address >> 12
        )  # bitwise right shift to get first 20 bits

        mask = 111111111111  # 12 1's or 0xFFF
        page_offset = virtual_address & mask  # bitwise and to get last 12 bits

        # fetch the current page table entry from RAM
        # construct page_table_entry_address

        page_table_entry_address = page_table_pointer + virtual_page_number * pte_width

        # read the 3 bytes containing pte from RAM.

        byte_1 = ram.read(address=page_table_entry_address)
        byte_2 = ram.read(address=page_table_entry_address + 1)
        byte_3 = ram.read(address=page_table_entry_address + 2)

        # construct pte object
        pte: PTE = PTE(byte_1, byte_2, byte_3)

        # check perissions
        if not pte.present_flag:
            # page fault page not mapped
            # add custom error later
            raise Exception("Page fault : virtual page not mapped.")

        physical_memory_address = pte.physical_frame_number << 12 | page_offset
        return physical_memory_address

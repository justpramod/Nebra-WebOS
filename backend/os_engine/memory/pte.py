"""
Page table entry- how the page table is stored in the ram.

for 32 bit address registers:
20 bit-> virtual page number => converted to 20 bit physical page number
12 bit -> offset => added to above physical page to get final physical address.

PTE is the data structure which represents mapping from virtual page to physical page.
It has the mapping as wel as flags to enforce rules.

total bytes: 3 bytes -> 24 bits
20 bits -> physical page number.
1 bit -> Present flag: if the virtual page is mapped to a physical frame of RAM. 1 if loaded, 0 if not mapper.
1 bit -> Read/write flag : if the file is read only => 0 , if read and write allowed => 1
1 bit -> user/ kernel flag : if accessible to user => 1 , only kernel => 0
1 bit -> saved for later


"""


class PTE:
    def __init__(self, byte_1: int, byte_2: int, byte_3: int) -> None:
        pte_data = (
            (byte_1 << 16) | (byte_2 << 8) | byte_3
        )  # left shift and combine with bitwise OR

        flag_bits = (
            pte_data & 0xF
        )  # masking with 1111, so only the last 4 bits are preserved

        self.physical_frame_number = pte_data >> 4

        self.present_flag = bool(flag_bits >> 3)
        self.read_write_flag = bool((flag_bits >> 2) & 1)
        self.user_kernel_flag = bool((flag_bits >> 1) & 1)

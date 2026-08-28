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
    def __init__(self, byte_1: str, byte_2: str, byte_3: str) -> None:
        pte_data = byte_1 + byte_2 + byte_3

        self.physical_page_number = pte_data[:20]
        self.present_bit = pte_data[20]
        self.read_write_flag = pte_data[21]
        self.user_kernel_flag = pte_data[22]

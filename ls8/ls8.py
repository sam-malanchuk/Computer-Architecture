# !/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load()
cpu.run()

cpu.ram_write(0b00000000, 0b00010101)

print(cpu.ram_read(0b00000000))
"""CPU functionality."""

import sys

# function dispatch table
ldi = 0b10000010
prn = 0b01000111
hlt = 0b00000001
mul = 0b10100010
pop = 0b01000110
push = 0b01000101

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # initiate the RAM capable of holding 256 bytes 
        self.ram = [0] * 256
        # initiate the program counter
        self.pc = 0
        # initiate the registery to take 8 bits
        self.reg = [0] * 8
        # reserve Registry 7 for Stack Address pointer
        self.sp = 7
        # start of Stack per spec
        self.reg[self.sp] = len(self.ram) - 12
        # initiate a branch table
        self.branchTable = {}
        self.branchTable[ldi] = self.handle_ldi
        self.branchTable[prn] = self.handle_prn
        self.branchTable[hlt] = self.handle_hlt
        self.branchTable[mul] = self.handle_mul
        self.branchTable[pop] = self.handle_pop
        self.branchTable[push] = self.handle_push
        # set CPU running
        self.running = False

    # method to return a memory value at a specific address
    def ram_read(self, mar):
        return self.ram[mar]

    # method to write a memory value at a specific address
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr
        # return True
        return 0b00000001

    def load(self):
        """Load a program into memory."""

        address = 0

        # if there is an extra system variable
        if len(sys.argv) > 1:
            # load in the file at specified address
            program_file = sys.argv[1]
            # read the file from path
            program = open(program_file, "r")

            # for every line in the file
            for line in program:
                # strip empty or hashes from program
                line = line.split('#',1)[0].strip()
                # add the line to the ram
                self.ram[address] = int(f'0b{line}', 2)
                # up the address variable for next loop
                address += 1

        # otherwise, demo the default program
        else:
            program = [
                # From print8.ls8
                0b10000010, # LDI R0,8
                0b00000000,
                0b00001000,
                0b01000111, # PRN R0
                0b00000000,
                0b00000001, # HLT
            ]

            for instruction in program:
                self.ram[address] = instruction
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # LDI: save the value into the register
    def handle_ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        self.pc += 3

    # PRN: print the value from register
    def handle_prn(self, operand_a, operand_b):
        print(self.reg[operand_a])
        self.pc += 2

    # MUL: get the product of the two register values specified, save in the first
    def handle_mul(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
        self.pc += 3

    # HLT: halt the program
    def handle_hlt(self, operand_a, operand_b):
        self.running = False
        self.pc += 1

    # PUSH: get the value out of memory and into the stack
    def handle_push(self, operand_a, operand_b):
        # decrement the Stack Pointer (SP)
        self.reg[self.sp] -= 1
        # read the next value for register location
        register_value = self.reg[operand_a]
        # take the value in that register and add to stack
        self.ram_write(self.reg[self.sp], register_value)
        self.pc += 2

    # POP: get the value out of stack into memory
    def handle_pop(self, operand_a, operand_b):
        # POP value of stack at location SP
        value = self.ram_read(self.reg[self.sp])
        # store the value in register given
        self.reg[operand_a] = value
        # increment the Stack Pointer (SP)
        self.reg[self.sp] += 1
        self.pc += 2        

    def run(self):
        # start the program
        self.running = True

        while self.running:
            # get the next instruction into instruction register
            ir = self.ram_read(self.pc)

            # store the next two instruction as possibly needed variables
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            # run the next instruction from the dispatch table
            self.branchTable[ir](operand_a, operand_b)
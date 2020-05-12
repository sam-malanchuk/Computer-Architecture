import sys

# OP(operation) codes
PRINT_SAM      = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4
PRINT_REGISTER = 5
ADD            = 6
POP            = 7
PUSH           = 8

# create the memory
memory = [0] * 256

# computer is running
running = True

# initialize the memory pointer
pc = 0

# create a register
registers = [0] * 8
SP = 7 # register location that holds top of stack address
# store top of memory into Register 7
registers[SP] = len(memory) -1

# Read from file, and load into memory
# read the filename from command line arguments
# open the file, and load each line into memory
# lets try not to crash
def load_program_into_memory():
    address = 0
    # get the filename from arguments here
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Need proper file name passed")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            # print(line)
            if line == '':
                continue
            comment_split = line.split('#')
            # print(comment_split) # [everything before #, everything after #]

            num = comment_split[0].strip()

            memory[address] = int(num)
            address += 1

load_program_into_memory()

# running while loop
while running:
    # memory pointer
    command = memory[pc]

    if command == PRINT_SAM:
        # print Sam!
        print('Sam!')
        pc += 1

    elif command == HALT:
        # stop the machine
        running = False
        pc += 1

    elif command == PRINT_NUM:
        # look at the next line in memory and print the number
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        # grab the number after SAVE command
        num_to_save = memory[pc + 1]
        # grab the 2nd number after SAVE command
        register = memory[pc + 2]
        # save the number given to location in memory specified
        registers[register] = num_to_save
        pc += 3
        
    elif command == PRINT_REGISTER:
        # grab the value in memory located at memory location specified
        register = memory[pc + 1]
        # print the item specified from register memory
        print(registers[register])
        pc += 2

    elif command == ADD:
        # grab the value in memory located at memory location specified
        register1 = memory[pc + 1]
        # grab another value in memory at memory location specified
        register2 = memory[pc + 2]
        # add the two values together
        registers[register1] = registers[register1] + registers[register2]
        pc += 3

    elif command == PUSH:
        # PUSH
        # rrrrr
        # PUSH register value to the stack
        register = memory[pc + 1]
        # decrement the Stack Pointer (SP)
        registers[SP] -= 1
        # read the next value for register location
        register_value = registers[register]
        # take the value in that register and add to stack
        memory[registers[SP]] = register_value
        pc += 2

    elif command == POP:
        # POP Rrrrrrrrr
        # POP value of stack at location SP
        value = memory[registers[SP]]
        register = memory[pc + 1]
        # store the value in register given
        registers[register] = value
        # increment the Stack Pointer (SP)
        registers[SP] += 1
        pc += 2

    else:
        # if command is not recognized
        print(f'Unknown command: {command}')
        # let's crash
        sys.exit(1)
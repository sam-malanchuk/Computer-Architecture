import sys

# OP(operation) codes
PRINT_SAM      = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4
PRINT_REGISTER = 5
ADD            = 6

print_some_nums = [
    SAVE,
    12,
    1,
    SAVE,
    45,
    2,
    ADD,
    1,
    2,
    PRINT_REGISTER,
    1,
    HALT,
]

# create the memory
memory = print_some_nums

# computer is running
running = True

# initialize the memory pointer
pc = 0

# create a register
registers = [0] * 8
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

    else:
        # if command is not recognized
        print(f'Unknown command: {command}')
        # let's crash
        sys.exit(1)
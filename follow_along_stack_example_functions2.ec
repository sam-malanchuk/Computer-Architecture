# Start of our program
# load register 5 with add_two_num subroutine
4
__ # value here is not known yet
5
# store our local x, y valiables to the stack
4 # save value 10 to reg1
10
1
# push reg 1 to stack
8
1
4 # save value 20 to reg1
20
1
# push reg 1 to stack
8
1
# call our add_two_num subroutine
9
5 # register that points to start of subroutine

# call our add_two_num subroutine
9
5 # register that point to start of subroutine


# add_two_num subroutine
# get value a
# read the value in memory from SP - 2
# get value b
# read the value in memory from SP - 1
# Do the addition
# Store the result in Register 0
# Register 0 will be our return register always

10


def decrement_num(a):
    if (a == 0)
        return
    b = 1 + decrement_num(a - 1)
    c = decrement_num(a - 2)

decrement_num(3)

def add_to_num(a, b):
    c = 3
    returns a + b

def main():
    x = 10
    y = 20
    z = add_two_num(x, y)
    print(z)
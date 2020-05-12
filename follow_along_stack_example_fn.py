def mult2(x, y):
    z = x * y
    return z

def main():
    a = 2
    b = mult2(a, 7)
    print(b) # should be 14

main()

"""
Stack grows downwards

255: 0

254: 2 (a)  main's stack frame
253: 0 (b)

252: 2 (x)   mult2's stack frame
251: 7 (y)
250: 14

"""
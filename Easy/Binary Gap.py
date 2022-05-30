# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binaryN = "{:b}".format(N)
    counter, mxCounter = 0,0
    for c in binaryN:
        if c == "1":
            mxCounter = max(counter, mxCounter)
            counter = 0
        else:
            counter += 1
    return mxCounter

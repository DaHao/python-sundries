#-*- coding=utf-8 -*-
import pdb
def fill(A, val, length, level):
    if length == 1: 
        A[level][level] = val
        return val

    x = 0
    for y in range(length-1):
        A[x+level][y+level] = val
        print('x=', x+level, ',y=', y+level, ',val=', val) 
        val += 1

    y = length - 1
    for x in range(length-1):
        A[x+level][y+level] = val
        print('x=', x+level, ',y=', y+level, ',val=', val) 
        val += 1

    x = length - 1
    for y in reversed(range(1, length)):
        A[x+level][y+level] = val
        print('x=', x+level, ',y=', y+level, ',val=', val) 
        val += 1
    
    y = 0
    for x in reversed(range(1, length)):
        A[x+level][y+level] = val
        print('x=', x+level, ',y=', y+level, ',val=', val) 
        val += 1

    print('')
    return val

def simple(A, val, length, level):
    if length == 1:
        A[level][level] = val
        return val
    for times, step in enumerate((0, length-1, length-1, 0)):
        for d in range(length-1):
            if times == 0:
                x, y = step, d
            elif times == 1:
                x, y = d, step
            elif times == 2:
                x, y = step, step-d
            else:
                x, y = length-1-d, step
            print('x=',x,' y=',y,',val=',val)   
            A[x+level][y+level] = val
            val += 1
        print('')
    return val

length = 5
val = 1
level = 0
A = [[0] * length for x in range(length)]
pdb.set_trace()
while length>0:
    #val = fill(A, val, length, level)
    val = simple(A, val, length, level)
    level += 1
    length -= 2
print(A)

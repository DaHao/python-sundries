#-*- coding=utf-8 -*-
import pdb
def isBadVersion(a):
    return a >= 24

def FBV(n):
    L = 1
    R = n
    m = (L+R)//2
    if m-1 <= 0:return m
    print('L = ', L, ', R = ', R, ', m = ', m)
    pdb.set_trace()
    while isBadVersion(m) == isBadVersion(m-1):

        if isBadVersion(m):
            R = m
        else:
            L = m

        m = (L+R)//2
        if m-1 <= 0 : return m
        print('L = ', L, ', R = ', R, ', m = ', m)
    return m

print(FBV(76))

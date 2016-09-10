import pdb
import sys

class Result:
    left = 0
    right = 0
    sumValue = 0

def find_maximum_subarray(A, low, high):
    if not A : return None
    if low == high:
        result = Result()
        result.left = low
        result.right = high
        result.sumValue = A[low]
        return result
    else:
        mid = (low + high - 1) // 2
        leftResult = find_maximum_subarray(A, low, mid)
        rightResult = find_maximum_subarray(A, mid+1, high)
        crossResult = crossMid(A, low, mid, high)

        if leftResult.sumValue >= crossResult.sumValue and leftResult.sumValue >= rightResult.sumValue:
            return leftResult
        elif rightResult.sumValue >= crossResult.sumValue and rightResult.sumValue >= leftResult.sumValue:
            return rightResult
        else:
            return crossResult


def crossMid(A, low, mid, high):

    result = Result()

    leftSum = -sys.maxsize
    sumValue = 0
    for idx in range(mid, low-1, -1):
        sumValue += A[idx]
        if sumValue > leftSum:
            leftSum = sumValue
            result.left = idx

    rightSum = -sys.maxsize
    sumValue = 0
    for idx in range(mid+1, high+1):
        sumValue += A[idx]
        if sumValue > rightSum:
            rightSum = sumValue
            result.right = idx

    result.sumValue = rightSum + leftSum

    return result

a = [ -23, -44, -43, -53, -43, -66]
#pdb.set_trace()
result = find_maximum_subarray(a, 0, len(a)-1)
print('array = ', a)
print('left Index = ', result.left)
print('right Index = ', result.right)
print('Sum = ', result.sumValue)

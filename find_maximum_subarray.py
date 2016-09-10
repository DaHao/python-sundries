import pdb
import sys

class Result:
    left = 0
    right = 0
    sumValue = 0

def find_maximum_subarray(A):
    if len(A) == 1:
        result = Result()
        result.left = 0
        result.right = 0
        result.sumValue = A[0]
        return result
    else:
        mid = len(A) // 2
        leftResult = find_maximum_subarray(A[:mid])
        rightResult = find_maximum_subarray(A[mid:])
        crossResult = crossMid(A, mid)

        if leftResult >= crossResult and leftResult >= rightResult:
            return leftResult
        elif rightResult >= crossResult and rightResult >= leftResult:
            return rightResult
        else:
            return crossResult


def crossMid(A, mid):

    result = Result()

    leftSum = -sys.maxsize
    sumValue = 0
    for idx in range(mid, -1, -1):
        sumValue += A[idx]
        if(sumValue > leftSum):
            leftSum = sumValue
            result.left = idx

    rightSum = -sys.maxsize
    sumValue = 0
    for idx in range(mid+1, len(A)):
        rightSum += A[idx]
        if(rightSum > rightSum):
            rightSum = rightSum
            result.right = idx

    result.sumValue = rightSum + leftSum

    return result

a = [-1, 2, 3, 4, -5]
pdb.set_trace()
result = find_maximum_subarray(a)
print('left Index = ', result.left)
print('right Index = ', result.right)
print('Sum = ', result.sumValue)

import pdb
class Result:
    left = 0
    right = 0
    sumValue = 0

def find_maximum_subarray(A):
    if len(A) == 2:
        result = Result()
        result.left = 0
        result.right = 1
        result.sumValue = A[0] + A[1]
        return result
    else:
        mid = len(A) // 2
        leftResult = find_maximum_subarray(A[:mid])
        rightResult = find_maximum_subarray(A[mid:])
        crossResult = crossMid(A, mid)

        if leftResult > crossResult and leftResult > rightResult:
            return leftResult
        elif rightResult > crossResult and rightResult > leftResult:
            return rightResult
        else:
            return crossResult


def crossMid(A, mid):

    leftSum = 0
    leftMaxSum = -1
    leftMaxIdx = -1
    for idx in range(mid, -1, -1):
        leftSum += A[idx]
        if(leftSum > leftMaxSum):
            leftMaxSum = leftSum
            leftMaxIdx = idx
    
    rightSum = 0
    rightMaxSum = -1
    rightMaxIdx = -1
    for idx in range(mid+1, len(a)):
        rightSum += A[idx]
        if(rightSum > rightMaxSum):
            rightMaxSum = rightSum
            rightMaxIdx = idx

    result = Result()
    result.left = leftMaxIdx
    result.right = rightMaxIdx
    result.sumValue = rightMaxSum + leftMaxSum

    return result

a = [-1, 2, 3, 4, -5]
pdb.set_trace()
result = find_maximum_subarray(a)
print('left Index = ', result.left)
print('right Index = ', result.right)
print('Sum = ', result.sumValue)

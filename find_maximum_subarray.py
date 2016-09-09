class Result:
    left = 0
    right = 0
    sumValue = 0

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
result = crossMid(a, 2)
print('left Index = ', result.left)
print('right Index = ', result.right)
print('Sum = ', result.sumValue)

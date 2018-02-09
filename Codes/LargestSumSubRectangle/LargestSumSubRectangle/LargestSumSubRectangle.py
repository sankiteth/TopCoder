def Kadane(arr, n):
    maxEndHere = maxOverall = arr[0]
    startOfMaxEndHere = 0
    startOfMaxOverall = endOfMaxOverall = 0
    for i in range(1, n):
        if maxEndHere + arr[i] > arr[i]:
            maxEndHere = maxEndHere + arr[i]
        else:
            maxEndHere = arr[i]
            startOfMaxEndHere = i
        if maxOverall < maxEndHere:
            maxOverall = maxEndHere
            startOfMaxOverall = startOfMaxEndHere
            endOfMaxOverall = i
    return (maxOverall, startOfMaxOverall, endOfMaxOverall)

def main():
    m = [[1, 2, -1, -4, -20], [-8, -3, 4, 2, 1], [3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]
    rows = len(m)
    cols = len(m[0])
    maxSum, finalLeft, finalRight, finalTop, finalBottom = -9999, -1, -1, -1, -1
    print('rows = {0}, cols = {1}'.format(rows, cols))

    for left in range(cols):
        temp = [0 for i in range(rows)]
        for right in range(left,cols):
            for i in range(rows):
                temp[i] = temp[i] + m[i][right]
            sum, start, end = Kadane(temp, rows)
            if maxSum < sum:
                maxSum = sum
                finalLeft = left
                finalRight = right
                finalTop = start
                finalBottom = end
    print('Top={0} Left={1}'.format(finalTop, finalLeft))
    print('Bottom={0} Right={1}'.format(finalBottom, finalRight))
    print('The max sum is {0}'.format(maxSum))

if __name__=='__main__':
    main()
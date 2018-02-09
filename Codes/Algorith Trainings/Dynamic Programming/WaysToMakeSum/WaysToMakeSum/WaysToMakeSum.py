'''
Given K elements arr[1..K], calculate the number of ways to make various sums of 
those values
'''
from functools import reduce
if __name__ == '__main__':
    arr = [1,2,3,4]
    maxSum = reduce( (lambda x, y: x+y), arr )
    print(maxSum)

    ways = [0 for i in range(maxSum+1)]
    ways[0] = 1
    for i in arr:
        for eachSum in range(maxSum, i-1, -1):
            ways[eachSum] += ways[eachSum-i]
    print(*ways,sep=',')
'''
whether a given multiset S of positive integers can be partitioned into two subsets S1 and S2 
such that the sum of the numbers in S1 equals the sum of the numbers in S2
'''
from _functools import reduce
def main():
    arr = [3,1,1,2,2,1]
    sum = reduce((lambda x, y : x + y), arr)
    print('sum={0}'.format(sum))

    if sum % 2 != 0:
        print('Cannot be partitioned!')
        return
    part = [[None for i in range(len(arr) + 1)] for i in range(sum//2 + 1)]
    soln = [[-1 for i in range(len(arr) + 1)] for i in range(sum//2 + 1)]
    print('Before:')
    print(*part, sep='\n')

    for i in range(len(arr) + 1):#a null subset always has 0 sum
        part[0][i] = True

    for i in range(1,sum//2 + 1):#a null subset cannot have any sum
        part[i][0] = False

    for i in range(1, sum//2 + 1):
        for j in range(1, len(arr) + 1):
            part[i][j] = part[i][j-1]
            if i >= arr[j-1]:
                part[i][j] = part[i][j] or part[i-arr[j-1]][j-1]
                if part[i-arr[j-1]][j-1] == True:
                    soln[i-arr[j-1]][j-1] = arr[j-1]
    
    print('After:')
    print(*part, sep='\n')
    #if part[sum//2][len(arr)] == True:
    #    printAllSoln(soln, sum//2, len(arr)) 

if __name__ == '__main__':
    main()
'''
Sparse Table (ST) algorithm:
A better approach is to preprocess RMQ for sub arrays of length 2^k using dynamic programming. 
We will keep an array M[0, N-1][0, logN] where M[i][j] is the index of the minimum value in the 
sub array starting at i having length 2^j
'''

def main():
    arr = [2, 4, 3, 1, 6, 7, 8, 9];
    n = len(arr)
    logN=1
    while 1<<logN < n:
        logN=logN+1
    #table of size (n*(logN+1))
    table = [[-1 for i in range(logN+1)] for i in range(n)]
    #Initializing table for intervals of length 1
    for i in range(n):
        table[i][0] = i
    #Fill table from smaller to longer lengths
    for j in range(1,logN+1):
        i=0
        while (i+(1<<j)-1) < n:
            if (arr[table[i][j - 1]] < arr[table[i + (1 << (j - 1))][j - 1]]):
                table[i][j] = table[i][j - 1];
            else:
                table[i][j] = table[i + (1 << (j - 1))][j - 1];
            i=i+1
    print(*table,sep='\n')
    i, j = 0, 7
    k = j - i + 1
    lgK = 0
    pow_2_K = 1
    while (k>>lgK+1) > 0:
        lgK = lgK + 1
        pow_2_K = pow_2_K * 2

    if arr[table[i][lgK]] <= arr[table[i + pow_2_K - 1][lgK-1]]:
        rmq = arr[table[i][lgK]]
    else:
        rmq = arr[table[i + pow_2_k][lgK-1]]
    print('rmq={0}'.format(rmq))

if __name__=='__main__':
    main()


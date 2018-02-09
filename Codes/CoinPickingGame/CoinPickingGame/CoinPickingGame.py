'''
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. 
We play a game against an opponent by alternating turns. In each turn, a player selects 
either the first or last coin from the row, removes it from the row permanently, and receives 
the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
'''
print('Hello World')
def main():
    arr = [8, 15, 3, 7]
    n = len(arr)
    opt = [[0 for i in range(n)] for i in range(n)]
    for i in range(n-1):
        opt[i][i] = arr[i]
        opt[i][i+1] = max(arr[i], arr[i+1])
    opt[n-1][n-1] = arr[n-1]
    for l in range(3,n+1):
        for i in range(n-l+1):
            j = i+l-1
            opt[i][j] = max(arr[i] + min(opt[i+2][j], opt[i+1][j-1]),
                            arr[j] + min(opt[i+1][j-1], opt[i][j-2])
                           )
    print('opt table:')
    print(*opt,sep='\n')
    print('The max that the user can get is {0}'.format(opt[0][n-1]))

if __name__=='__main__':
    main()
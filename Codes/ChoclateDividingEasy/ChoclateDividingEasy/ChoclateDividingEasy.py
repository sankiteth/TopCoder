'''
http://apps.topcoder.com/wiki/display/tc/SRM+636
'''
if __name__ == '__main__':
    INF = -9999
    chocolate = [
                "9768",
                "6767",
                "5313"
                ]
    n = len(chocolate) # rows
    m = len(chocolate[0]) # columns

    table = [[0 for i in range(m+1)] for i in range(n+1)]
    # table[x][y]=sum of all elements in [rect (0,0) , (x,y)]
    for x in range(1, n+1):
        for y in range(1, m+1):
            val = int(chocolate[x-1][y-1])
            table[x][y] = val + (table[x][y-1] + table[x-1][y]) - table[x-1][y-1]

    print('Table')
    print(*table,sep='\n')
    arr = [-1 for i in range(3)]
    res = INF
    for x1 in range(1, n-1):
        for x2 in range(x1+1, n):
            for y1 in range(1, m-1):
                arr[0] = table[x1][y1]
                arr[1] = table[x2][y1] - table[x1][y1]
                arr[2] = table[n][y1] - table[x2][y1]
                minHere = min(arr[0], arr[1], arr[2])
                for y2 in range(y1+1, m):
                    x = [0, x1, x2, n]
                    y = [0, y1, y2, m]
                    for i in range(0,3):
                        for j in range(1,3):
                            val = ( table[x[i+1]][y[j+1]] -
                                    table[x[i]][y[j+1]] - 
                                    table[x[i+1]][y[j]] +
                                    table[x[i]][y[j]] )
                            minHere = min(minHere, val)
                    res = max(res, minHere)
    print(res)
                                           
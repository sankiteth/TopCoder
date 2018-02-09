'''
http://apps.topcoder.com/wiki/display/tc/SRM+636
'''
def allAtLeast(y, left, right, r):
    '''
    If the horizontal cuts are given by y[], we need to ignore the left
    left-most cols and the needed quality sum of each rectangle is r, 
    can we do it using the next "right" cols?
    '''
    for j in range(4):
        # s-> sum of all elements in present rectangle
        s = (table[ y[j + 1] ][ left + right ] - 
             table[ y[j] ][ left + right ] - 
             table[ y[j + 1] ][ left ] + 
             table[ y[j] ][ left ]
             )
        if s < r:
            return False

    return True
            
            

def isPossible(r):
    # Try all the horizontal cuts:
    for y1 in range(1, n):
        for y2 in range(y1 + 1, n):
            for y3 in range(y2 + 1, n):
                y = [0, y1, y2, y3, n]
                left = 0 # ignored left-most cols
                i = 0
                while i<3 and left<m :
                    # A binary search for the smallest number of new cols:
                    lo = 0
                    hi = m - left
                    while lo+1 < hi :
                        right = lo + (hi - lo)//2
                        if allAtLeast(y, left, right, r) :
                            hi = right
                        else:
                            lo = right
                    left += hi
                    #if it is impossible, left will become m
                    i += 1
                if left < m:
                    if allAtLeast(y, left, m - left, r):
                        return True
    return False

if __name__ == '__main__':
    chocolate = [
                "95998",
                "21945",
                "23451",
                "99798",
                "74083"
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

    # Binary search for the maximum r such that it is possible to have
    # 16 rectangles of quality >= r
    lo = 0
    hi = 9*m*n + 1

    while(lo+1 < hi):
        ha = lo + (hi-lo)//2
        if isPossible(ha):
            lo = ha
        else:
            hi = ha

    print('Max={0}'.format(lo))
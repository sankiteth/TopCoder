'''
The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to heart. 
Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the town's well than his neighbors, 
so the town has been arranged in a big circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. 
You have been hired to collect donations for the Save Our Well fund.
Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, 
which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor has 
also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last entries in donations 
are also for next-door neighbors. You must calculate and return the maximum amount of donations that can be collected.

O(n) solution
'''
def main():
    don = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    n = len(don)
    neg = -9
    fund = [[0 for i in range(n)] for i in range(3)]
    #stores the maximum element in the table
    maximum = neg
    #base cases
    for i in range(3):
        fund[i][i] = don[i]
        if maximum <= fund[i][i]:
            maximum = fund[i][i]

    print('Initial Table:')
    print(*fund,sep='\n')

    for i in range(3):
        for l in range(2,n):# that is for length = 2,3,4,...,n-3,n-1
            j = (i+l-1) % n
            if l==2:
                lst = [don[i], don[j]]
                fund[i][j] = max(lst)
            else:
                fund[i][j] = max([ fund[i][(j-1) % n], (fund[i][(j-2) % n] + don[j]) ])
            if fund[i][j] >= maximum:
                maximum = fund[i][j]

    print('\nFinal Table:')
    print(*fund,sep='\n')
    
    print('\nThe maximum donation is {0}'.format(maximum))

if __name__=='__main__':
    main()
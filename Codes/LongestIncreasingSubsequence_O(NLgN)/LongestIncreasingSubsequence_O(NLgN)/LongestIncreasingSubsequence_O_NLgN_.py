def main():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    n = len(arr)
    #store indices in table rather than values
    tbl = [-1 for i in range(n)]
    parent = [-1 for i in range(n)] #For Computing back the solution
    tbl[0] = 0
    L = 1
    for i in range(1,n):
        if arr[i] < arr[tbl[0]]:
            tbl[0] = i
        elif arr[i] > arr[tbl[L-1]]:
            parent[L] = tbl[L-1]
            tbl[L] = i
            L = L + 1
        else:
            l, m, r = -1, 0, L-1
            while(r-l >= 2):
                m = l + (r-l)//2
                if arr[tbl[m]] >= arr[i]:
                    r = m
                else:
                    l = m
            #arr[i] wants to be current end candidate of an existing subsequence
            #r is the length of the sequence whose last element is replaced by arr[i]
            tbl[r] = i
    print('Length of LIS={0}'.format(L))
    l = L-1
    p = tbl[l]
    lst = []
    while(p != -1):
        lst.append(arr[p])
        p = parent[l]
        l = l - 1
    print('An LIS is {0}'.format(lst[::-1]))

if __name__=='__main__':
    main()
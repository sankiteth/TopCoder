def PrintLongestPalindrome(arr, n, isPalin, len):
    l = n
    p = []
    maxLen = (len+1)//2
    found = False
    while(l > 0 and maxLen):
        if found == False:
            i = 0
            j = i+l-1
        while(j < n):
            if isPalin[i][j]:
                p.append(arr[j])
                found = True
                i = i+1
                j = j-1
                maxLen = maxLen - 1
                break
            i = i+1
            j = j+1
        l = l-1
    if (len % 2) != 0:
        print(*p,sep='',end='')
        p.pop()
        print(*p[::-1],sep='')
    else:
        print(*p,sep='',end='')
        print(*p[::-1],sep='')

def main():
    arr = 'qwabbazn'
    isPalin = [[None for j in range(len(arr))] for i in range(len(arr))]
    #base cases
    isPalin[len(arr)-1][len(arr)-1] = True
    maxLen = 1
    for i in range(len(arr) - 1):
        isPalin[i][i] = True
        isPalin[i][i+1] = True if (arr[i] == arr[i+1]) else False
        if isPalin[i][i+1]:
            maxLen = 2
    print('Before:')
    print(*isPalin,sep='\n')
    for l in range(3,len(arr)+1):
        for i in range(len(arr)-l+1):
            j=i+l-1
            isPalin[i][j] = True if (isPalin[i+1][j-1] and arr[i]==arr[j]) else False
            if (isPalin[i][j]):
                maxLen = l
    print('After:')
    print(*isPalin,sep='\n')
    print('Length of longest palindrome={0}'.format(maxLen))
    PrintLongestPalindrome(arr, len(arr), isPalin, maxLen)

if __name__=='__main__':
    main()
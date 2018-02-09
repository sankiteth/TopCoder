'''
We have an array arr[0 . . . n-1]. We should be able to efficiently find the minimum value from index qs (query start) 
to qe (query end) where 0 <= qs <= qe <= n-1. 
The array is static (elements are not deleted and inserted during the series of queries)
'''

def ConstructSegmentTreeUtility(arr, start, end, segmentTree, index):
    if start==end:
        segmentTree[index] = arr[start]
        return segmentTree[index]
    mid = start + (end - start)//2
    leftMin = ConstructSegmentTreeUtility(arr, start, mid, segmentTree, (2*index)+1)
    rightMin = ConstructSegmentTreeUtility(arr, mid+1, end, segmentTree, (2*index)+2)
    segmentTree[index] = leftMin if leftMin <= rightMin else rightMin
    return segmentTree[index]

def ConstructSegmentTree(arr, n):
    total = 1;
    #find the nearest power of 2 to n
    while total <= n:
        total=total*2

    segmentTree = [0]*(2*total-1)
    minInArray = ConstructSegmentTreeUtility(arr, 0, n-1, segmentTree, 0)
    return segmentTree

def GetMinUtility(arr, start, end, queryStart, queryEnd, segmentTree, index):
    if queryEnd<start or queryStart>end:
        return 9999999
    if queryStart<=start and queryEnd>=end:
        return segmentTree[index]
    mid = start + (end - start)//2
    leftMin = GetMinUtility(arr, start, mid, queryStart, queryEnd, segmentTree, 2*index+1)
    rightMin = GetMinUtility(arr, mid+1, end, queryStart, queryEnd, segmentTree, 2*index+2)
    return leftMin if leftMin <= rightMin else rightMin

def GetMin(arr, n, queryStart, queryEnd, segmentTree):
    if queryStart>queryEnd or queryStart<0 or queryEnd>n-1:
        return -1
    return GetMinUtility(arr, 0, n-1, queryStart, queryEnd, segmentTree, 0)

def main():
    arr = [1, 3, 5, 7, 9, 11];
    n = len(arr)
    segmentTree = ConstructSegmentTree(arr, n)
    print(*segmentTree, sep=',')
    min = GetMin(arr, n, 3, 5, segmentTree)
    print(min)

if __name__=='__main__':
    main()
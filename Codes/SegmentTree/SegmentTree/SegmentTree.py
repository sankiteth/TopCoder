# Segment Tree | Set 1 (Sum of given range)

def ConstructSegmentTreeUtility(arr, start, end, segmentTree, sTIndex):
    if start <= end:
        #base case
        if start == end:
            segmentTree[sTIndex] = arr[start]
            return segmentTree[sTIndex]
        
        #integer division
        mid = start + (end - start)//2
        left = ConstructSegmentTreeUtility(arr, start, mid, segmentTree, (2*sTIndex)+1)
        right = ConstructSegmentTreeUtility(arr, mid+1, end, segmentTree, (2*sTIndex)+2)
        segmentTree[sTIndex] = left + right
        return segmentTree[sTIndex]


def ConstructSegmentTree(arr, n):
    total = 1;
    #find the nearest power of 2 to n
    while total <= n:
        total=total*2

    segmentTree = [0] * (2*total - 1)
    ConstructSegmentTreeUtility(arr, 0, n-1, segmentTree, 0)
    return segmentTree

def GetSumUtility(arr, arrayStart, arrayEnd, queryStart, queryEnd, segmentTree, index):
    if queryStart<=arrayStart and queryEnd>=arrayEnd:
        return segmentTree[index]
    if queryStart>arrayEnd or queryEnd<arrayStart:
        return 0
    mid = arrayStart + (arrayEnd - arrayStart)//2
    left = GetSumUtility(arr, arrayStart, mid, queryStart, queryEnd, segmentTree, 2*index+1)
    right = GetSumUtility(arr, mid+1, arrayEnd, queryStart, queryEnd, segmentTree, 2*index+2)
    return left+right

def GetSum(arr, n, start, end, segmentTree):
    if end < start or start < 0 or end > n-1:
        return -1
    else:
        return GetSumUtility(arr, 0, n-1, start, end, segmentTree, 0)

def UpdateSegmentTreeUtility(arr, start, end, updateIndex, diff, segmentTree, index):
    segmentTree[index] = segmentTree[index] + diff
    if start==end:
        return
    mid = start + (end - start)//2
    if updateIndex<=mid:
        UpdateSegmentTreeUtility(arr, start, mid, updateIndex, diff, segmentTree, 2*index+1)
    else:
        UpdateSegmentTreeUtility(arr, mid+1, end, updateIndex, diff, segmentTree, 2*index+2)

def UpdateSegmentTree(arr, n, updateIndex, newValue, segmentTree):
    if updateIndex<0 or updateIndex>n-1:
        return
    diff = newValue - arr[updateIndex]
    arr[updateIndex] = newValue
    UpdateSegmentTreeUtility(arr, 0, n-1, updateIndex, diff, segmentTree, 0)

def main():
    arr = [1, 3, 5, 7, 9, 11];
    n = len(arr)
    segmentTree = ConstructSegmentTree(arr, n)
    print(*segmentTree, sep=',')
    sum = GetSum(arr, n, 5, 5, segmentTree)
    print(sum)
    UpdateSegmentTree(arr, n, 1, 10, segmentTree)
    print(*segmentTree, sep=',')

if __name__ == '__main__':
    main()
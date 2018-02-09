'''
http://community.topcoder.com/tc?module=Static&d1=match_editorials&d2=srm150
min[left,size,color] = the minimum number of brushes required to paint position
                       left, left+1, ... , left+size-1 of the original strip,
                       assuming these position currently has color "color".
'''

def f(left, size, color):
    global stripes
    global minim

    if minim[ord(color)][left][size] != -1:
        return minim[ord(color)][left][size]
    elif size == 0:
        minim[ord(color)][left][size] = 0
        return 0
    else:
        best = 999999
        for i in range(1,size+1):
            if stripes[left] == color:
                bestTillNow = f(left+1, size-1, color)
            else:
                bestTillNow = 1 + f(left+1, i-1, stripes[left]) + f(left+i, size-i, color)
            if bestTillNow < best:
                best = bestTillNow
        minim[ord(color)][left][size] = best
        return best

if __name__ == '__main__':
    stripes = "BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD" # "RGBGR"
    length = len(stripes)
    minim = [[[-1 for j in range(length+1)] for i in range(length+1)] for k in range(128)]
    minStrokes = f(0, length, '?')
    print(minStrokes)

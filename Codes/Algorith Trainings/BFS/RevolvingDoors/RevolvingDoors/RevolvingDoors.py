def dfs(map, start, end, res):
    if start == end:
        return res
    else:
        dir = ''
        if map[start[0],start[1]]=='|' and map[start[0]+1,start[1]]=='O' and map[start[0]+2,start[1]+2]=='|':

            res += 1

        minim = 9999
        for nbr in emptyNbrsOfStart(map, start):
            childRes = dfs(map, nbr, end, res)
            res =  min(minim, childRes)

if __name__ == '__main__':
    map = [
        "    ### ",
        "    #E# ",
        "   ## # ",
        "####  ##",
        "# S -O-#",
        "# ###  #",
        "#      #",
        "########" 
        ]
    print(*map, sep='\n')

    rows = len(map)
    cols = len(map[0])
    res = 0
    # find start and end
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 'S':
                start = (i,j)
            if map[i][j] == 'E':
                end = (i,j)
    res = dfs(map, start, end, res)
'''
http://apps.topcoder.com/wiki/display/tc/SRM+638
'''
import sys
sys.setrecursionlimit(10*10*10*10)

# check if the cube at (i,j,k) can exist given the projection images
def exists(i,j,k):
    if (0 <= i < n) and (0 <= j < n) and (0 <= k < n):
        return XY[i][j] == 'Y' and YZ[j][k] == 'Y' and ZX[k][i] == 'Y'
    else:
        return False

# A depth-first search to find the connected components
def dfs(i,j,k):
    global componentContents
    global visited
    if (i,j,k) not in visited:
        visited.add( (i,j,k) ) 
        componentContents.add( (i,j,k) )
        for (di,dj,dk) in d:
            if exists(i+di, j+dj, k+dk):
                dfs(i+di, j+dj, k+dk)

#verify if the component can make the correct projection image
def correctComponent(contents):
    for i in range(n):
        for j in range(n):
            #if any coordinate with X=i, Y=j is in the component and XY[i][j] == 'F' => this component not valid
            #if any coordinate with X=i, Y=j is not in the component and XY[i][j] == 'T' => this component not valid
            if any( ((i,j,k) in contents) for k in range(n) ) != (XY[i][j] == 'Y'):
                return False
            if any( ((j,k,i) in contents) for k in range(n) ) != (ZX[i][j] == 'Y'):
                return False
            if any( ((k,i,j) in contents) for k in range(n) ) != (YZ[i][j] == 'Y'):
                return False
    return True
     
def main(XY, YZ, ZX):
    # special case, maybe the whole thing is empty, if the empty set of cubes 
    # makes the correct projections, then that is a possible solution
    if correctComponent( set() ): 
        return "Possible"
     
    # For each connected component:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if exists(i,j,k) and (i,j,k) not in visited:
                    global componentContents
                    componentContents = set()
                    # find cubes in component
                    dfs(i,j,k)
                     
                    # check if it makes the valid shadows
                    if correctComponent( componentContents ):
                        return "Possible"
         
    return "Impossible"

if __name__ == '__main__':
    XY = ["YYY","YNY","YYY"]
    YZ = ["YYY","YNY","YYY"]
    ZX = ["YYY","YNY","YYY"]
    n = len(XY)
    visited = set()
    d = ( (1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1) ) 
    componentContents = set()
    res = main(XY, YZ, ZX)
    print(res)
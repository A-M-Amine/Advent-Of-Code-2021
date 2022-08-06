
def maxPos(inpt):
    maxX = 0
    maxY = 0

    for j in inpt:
        for i in j:
            if int(i[0]) > maxX:
                maxX = int(i[0])
            if int(i[2]) > maxX:
                maxX = int(i[2])
            if int(i[1]) > maxY:
                maxY = int(i[1])
            if int(i[3]) > maxY:
                maxY = int(i[3])

    return (maxX,maxY)


def createGrid(x,y):

    grid = [] 
    for i in range(y):
        grid.append([])
        for j in range(x):
            grid[i].append('.')

    return grid


def createLine(grid,x,y,x2,y2):
    
    if (x > x2 and y2 == y) or (x2 == x and y > y2):
    
        tmp = x
        x = x2
        x2 = tmp

        tmp = y
        y = y2
        y2 = tmp



    if x == x2:

        if grid[y][x] == '.':
            grid[y][x] = '1'
        else:
            grid[y][x] = str(int(grid[y][x]) + 1)

        for i in range(y+1,y2+1):
                if grid[i][x] == '.':
                    grid[i][x] = '1'
                else:
                    grid[i][x] = str(int(grid[i][x]) + 1)
            
    else:
        if y == y2:

            if grid[y][x] == '.':
                grid[y][x] = '1'
            else:
                grid[y][x] = str(int(grid[y][x]) + 1)

        
            for i in range(x+1,x2+1):
                if grid[y][i] == '.':
                    grid[y][i] = '1'
                else:
                    grid[y][i] = str(int(grid[y][i]) + 1)
    

inpt = [ [i.replace("->",",").replace(" ","").strip("\n").split(",")] for i in open("test.txt").readlines()]

x,y = maxPos(inpt)
grid = createGrid(x+1,y+1)

while inpt:
    vents = inpt.pop(0)
    v = [int(i) for i in vents[0]]
    line = createLine(grid,v[0],v[1],v[2],v[3])

for i in grid:
    print(i)

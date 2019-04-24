#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# You Can Go Your Own Way

lydiacells = []

def buildLydia(path, grid):
    lydiacells = [['0']*grid for _i in range(grid)]
    x,y = 0,0
    for step in path:
        lydiacells[x][y] = step
        if step == "E":
            y += 1
        else:
            x += 1
    return lydiacells

def checkCell(move, cell):
    global lydiacells
    x = cell[0]
    y = cell[1]
    lydiacell = lydiacells[x][y]
    if lydiacell == move:
        return False
    return True

def pickPath(path, grid, cell):
    # at end
    if cell[0] == grid and cell[1] == grid:
        return path
    # only move E
    elif cell[1] == grid and cell[0] != grid:
        if checkCell("E", cell):
            newpathE = path + "E"
            newcellE = [cell[0]+1, cell[1]]
            return pickPath(newpathE, grid, newcellE)
    # only move S
    elif cell[0] == grid and cell[1] != grid:
        if checkCell("S", cell):
            newpathS = path + "S"
            newcellS = [cell[0], cell[1]+1]
            return pickPath(newpathS, grid, newcellS)
    # move both
    else:
        if checkCell("E", cell):
            newpathE = path + "E"
            newcellE = [cell[0]+1, cell[1]]
            return pickPath(newpathE, grid, newcellE)
        if checkCell("S", cell):
            newpathS = path + "S"
            newcellS = [cell[0], cell[1]+1]
            return pickPath(newpathS, grid, newcellS)

def solver():
    global lydiacells
    T = int(input())
    for test_case in range(1,T+1):
        N = int(input())
        P = input()
        lydiacells = buildLydia(P, N)
        results = pickPath("", N-1, [0,0])
        print("Case #{0}: {1}".format(test_case, results))

solver()
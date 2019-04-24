#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# You Can Go Your Own Way

lydiacells = []
debug = True

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

def checkCell(move, cell, lydiacells):
    if debug: print("Checking Lydia:\n\tMove:  {0}\n\tCell:  {1}".format(move, cell))
    lydiacell = lydiacells[cell[0]][cell[1]]
    if debug: print("\tLydia: {0}".format(lydiacell))
    if lydiacell == move:
        if debug: print("\tCheck: Matches, that's bad")
        return False
    if debug: print("\tCheck: No Match, that's good")
    return True

def pick_path(path, grid, cell):
    global lydiacells
    if debug: print("Current recursion:\n\tPath: {0}\n\tCell: {1}".format(path, cell))
    # at end
    if cell[0] == grid and cell[1] == grid:
        if debug: print("Found the path! {0}".format(path))
    # only move S
    elif cell[0] == grid and cell[1] != grid:
        if debug: print("moving only S")
        if checkCell("S", cell, lydiacells):
            newpathS = path + "S"
            newcellS = [cell[0], cell[1]+1]
            return pick_path(newpathS, grid, newcellS)
    # only move E
    elif cell[1] == grid and cell[0] != grid:
        if debug: print("moving only E")
        if checkCell("E", cell, lydiacells):
            newpathE = path + "E"
            newcellE = [cell[0]+1, cell[1]]
            return pick_path(newpathE, grid, newcellE)
    # move both
    else:
        if debug: print("moving also S")
        if checkCell("S", cell, lydiacells):
            newpathS = path + "S"
            newcellS = [cell[0], cell[1]+1]
            return pick_path(newpathS, grid, newcellS)
        if debug: print("moving also E")
        if checkCell("E", cell, lydiacells):
            newpathE = path + "E"
            newcellE = [cell[0]+1, cell[1]]
            return pick_path(newpathE, grid, newcellE)
    return path

def solver():
    global lydiacells
    T = int(input())
    for test_case in range(1,T+1):
        N = int(input())
        P = input()
        lydiacells = buildLydia(P, N)
        if debug:
            print("LydiaPath:")
            for row in lydiacells:
                print("\t{0}".format(row))
        results = pick_path("", N-1, [0,0])
        if debug: print("results:", results)
        print("Case #{0}: {1}".format(test_case, results))

solver()
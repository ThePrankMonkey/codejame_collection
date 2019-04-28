#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

''' CodeJam 2019 - Round B - Manhattan Crepe Carts '''


def main():
    ''' main function '''
    T = int(input())
    for testcase in range(1, T+1):
        results = solver()
        print("Case #{0}: {1}".format(testcase, results))


def solver():
    ''' handles each test case loop '''
    P, Q = [int(x) for x in input().split(" ")]
    Q += 1
    grid = []
    for _dummy in range(Q):
        grid.append([0]*Q)
    for _dummy in range(P):
        X, Y, D = input().split(" ")
        X = int(X)
        Y = int(Y)
        grid = mark_grid(X, Y, D, Q, grid)
        # print(X, Y, D)
        # print_grid(grid)
    crepe_location = sw_grid(Q, grid)
    return crepe_location


def mark_grid(X, Y, D, Q, grid):
    ''' incredment each intersection a person could be walking to '''
    if D == "N":
        for i in range(Y+1, Q):
            for j in range(Q):
                grid[i][j] += 1
    if D == "S":
        for i in range(Y):
            for j in range(Q):
                grid[i][j] += 1
    if D == "E":
        for i in range(X+1, Q):
            for j in range(Q):
                grid[j][i] += 1
    if D == "W":
        for i in range(X):
            for j in range(Q):
                grid[j][i] += 1
    return grid


def sw_grid(Q, grid):
    ''' find the most SW intersection possible '''
    # Find max value
    max_people = 0
    for i in range(Q):
        if max(grid[i]) > max_people:
            max_people = max(grid[i])
    # First spot found going NE will be our location
    for i in range(Q):
        for j in range(Q):
            if grid[j][i] == max_people:
                return "{0} {1}".format(i, j)
    return None


def print_grid(grid):
    ''' for debugging, shows what the grid looks like '''
    for row in reversed(range(len(grid))):
        print(grid[row])


if __name__ == "__main__":
    main()

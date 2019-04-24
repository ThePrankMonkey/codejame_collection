#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

''' Kick Start 2019 - Round B - Energy Stones '''

import itertools

def main():
    T = int(input())
    for testcase in range(1,T+1):
        N = int(input())
        stones = []
        for _i in range(N):
            S, E, L = [int(x) for x in input().split(" ")]
            stones.append([S, E, L])
        results = findEnergy(stones)
        print("Case #{}: {}".format(testcase, results))


def findEnergy(stones):
    energy_results = [0]
    perms = itertools.permutations(stones)
    for perm in perms:
        time = 0
        energy = 0
        for stone in perm:
            energy += max(stone[1] - time*stone[2], 0)
            time += stone[0]
        energy_results.append(energy)
    return max(energy_results)

main()
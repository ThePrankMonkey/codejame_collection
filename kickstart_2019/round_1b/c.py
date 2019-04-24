#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

''' Kick Start 2019 - Round B - Diverse Subarray '''

import collections

def main():
    T = int(input())
    for testcase in range(1,T+1):
        N, S = [int(x) for x in input().split(" ")]
        A = [int(x) for x in input().split(" ")]
        results = findTrinkets(A, S)
        print("Case #{}: {}".format(testcase, results))


def findTrinkets(A, S):
    trinkets = [0]
    for i in range(len(A)):
        for j in range(i+1, len(A)+1):
            trinket_sum = sumTrinkets(A[i:j], S)
            print(i,j, trinket_sum)
            trinkets.append(trinket_sum)
    return max(trinkets)


def sumTrinkets(splice, S):
    trinket_counter = collections.Counter(splice)
    trinket_sum = 0
    for trinket in trinket_counter:
        if trinket_counter[trinket] <= S:
            trinket_sum += trinket_counter[trinket]
    return trinket_sum


main()
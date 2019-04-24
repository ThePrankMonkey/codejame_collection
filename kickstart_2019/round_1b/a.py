#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

''' Kick Start 2019 - Round B - Building Palindromes'''

def main():
    T = int(input())
    for testcase in range(1,T+1):
        results = 0
        N, Q = [int(x) for x in input().split(" ")]
        letters = input()
        for _question in range(Q):
            results += solver(letters)
        print("Case #{}: {}".format(testcase, results))


def solver(letters):
    start, end = [int(x)-1 for x in input().split(" ")]
    splice = letters[start:end+1]
    splice_dict = makeDict(splice)
    odds = []
    for value in splice_dict.values():
        if value % 2 != 0:
            odds.append(value)
    if len(odds) > 1:
        return 0
    return 1


def makeDict(splice):
    new_dict = {}
    for letter in splice:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict


main()
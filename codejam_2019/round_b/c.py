#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

''' CodeJam 2019 - Round B - Fair Fight '''


def main():
    ''' main function '''
    T = int(input())
    for testcase in range(1, T+1):
        results = solver()
        print("Case #{0}: {1}".format(testcase, results))


def solver():
    ''' Handles looping through testcases '''
    N, K = [int(x) for x in input().split(" ")]
    C = [int(x) for x in input().split(" ")]
    D = [int(x) for x in input().split(" ")]
    range_list = get_ranges(N)
    results = 0
    for range_item in range_list:
        c_sub = C[range_item[0]:range_item[1]]
        d_sub = D[range_item[0]:range_item[1]]
        results += compare_range(c_sub, d_sub, K)
    return results


def get_ranges(N):
    ''' gets a list of every L>R range '''
    range_list = []
    for i in range(N+1):
        for j in range(i+1, N+1):
            range_list.append((i, j))
    return range_list


def compare_range(c_sub, d_sub, K):
    ''' checks if ranges satisfy fair condition or not '''
    if abs(max(c_sub) - max(d_sub)) <= K:
        return 1
    return 0


if __name__ == "__main__":
    main()

#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Problem D. Sums of Sums
# https://code.google.com/codejam/contest/4374486/dashboard#s=p3

T = int(input())
for case_num in range(1, T + 1):
    N, Q = [int(a) for a in input().split(" ")]
    initial_array = [int(a) for a in input().split(" ")]
    # Create an array of all sums of sub arrays
    sub_sums = []
    for i in range(N):
        for j in range(i, N):
            sub_sums.append(sum(initial_array[i:j+1]))
    sub_sums.sort()
    output = []
    # Find the sum of each query
    for i in range(Q):
        L, R = [int(a) for a in input().split(" ")]
        output.append(sum(sub_sums[L-1:R]))
    Results = "\n".join([str(a) for a in output])
    print("Case #{case}: \n{answer}".format(case=case_num, answer=Results))

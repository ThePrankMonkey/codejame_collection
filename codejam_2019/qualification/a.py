#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Foregone Solution

def solver():
    T = int(input())
    for test_case in range(1,T+1):
        N = int(input())
        n_str = str(N)
        # print("n_str", n_str)
        if "4" not in n_str:
            results = [N, 0]
        else:
            M = ""
            for n_char in n_str:
                # print("nchar", n_char)
                if n_char == "4":
                    M += "1"
                else:
                    M += "0"
            M = int(M)
            results = [N-M, M]
        # print(test_case)
        # print(results)
        print("Case #{0}: {1}".format(test_case, " ".join(str(x) for x in results)))

solver()
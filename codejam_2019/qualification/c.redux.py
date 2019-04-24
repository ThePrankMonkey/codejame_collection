#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Cryptopangrams
# https://primes.utm.edu/lists/small/10000.txt

import traceback

def prime_solver(val):
    for guessA in range(2, val):
        if val % guessA == 0:
            guessB = val // guessA
            break
    return guessA, guessB

def prime_factors_other(val, a, b, maxval):
    #print("T1\n\tval: {0}\n\ta:   {1}\n\tb:   {2}\n\tmax: {3}".format(val, a, b, maxval))
    # if 0 in (a,b): print ("a is {0}\nb is {1}".format(a,b))
    guessA = val // a
    guessB = val // b
    # print ("Funky:\n\tval: {0}\n\ta:   {1}\n\tb:   {2}\n\tgA: {3}\n\tgB: {4}".format(val,a,b,guessA,guessB))
    # print("Here are the subprimes:\n\tval: {0}\n\tA: {1}\n\tB: {2}".format(val, guessA, guessB))
    
    # check for zero
    # if guessA == 0:
    #     # print("Zer Selecting:  ", guessB)
    #     return val, guessB
    # if guessB == 0:
    #     # print("Zer Selecting:  ", guessA)
    #     return val, guessA

    # check if they return floats
    if val % a != 0:
        # print("Mod Selecting:  ", guessB)
        return val, guessB
    if val % b != 0:
        # print("Mod Selecting:  ", guessA)
        return val, guessA

    # check if even:
    if guessA % 2:
        # print("Even Selecting: ", guessB)
        return val, guessB
    if guessB % 2:
        # print("Even Selecting: ", guessA)
        return val, guessA

    # check boundaries
    if guessA < 2 or maxval < guessA:
        # print("Rng Selecting:  ", guessB)
        return val, guessB
    if guessB < 2 or maxval < guessB:
        # print("Rng Selecting:  ", guessA)
        return val, guessA

    # Run through a prime solver
    A,B = prime_solver(val, maxval)
    if guessA in (A,B):
        return val, guessB
    return val, guessA

def getLetters(prime_list):
    alphas = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    # build a dict of prime to char
    prime_set = set(prime_list)
    if len(prime_set) != 26:
        print("Bad prime set.")
        print(prime_set)
    prime_dict = dict(zip(sorted(prime_set), alphas))
    # for i in prime_dict.items():
    #     print("\t{0}".format(i))
    crypt = ""
    # Loop through primes in order of finding
    for prime_num in prime_list:
        crypt += prime_dict[prime_num]
    return crypt

def solver():
    T = int(input())
    for test_case in range(1,T+1):
        N, L = [int(x) for x in input().split(" ")]
        prod_arr = [int(x) for x in input().split(" ")]
        print(prod_arr)

        first_primesA, first_primesB = prime_solver(prod_arr[0])
        last_primesA, last_primesB = prime_solver(prod_arr[1])
        # find which prime came first
        if first_primesA not in (last_primesA, last_primesB):
            prime_list = [first_primesA]
            prime_list.append(first_primesB)
        else:
            prime_list = [first_primesB]
            prime_list.append(first_primesA)
        # find which prime came thrid
        if last_primesA not in (first_primesA, first_primesB):
            prime_list.append(last_primesA)
            last_primesB, last_primesA = last_primesA, last_primesB
        else:
            prime_list.append(last_primesB)
        
        for i in range(2, len(prod_arr)):
            last_primesA, last_primesB = prime_factors_other(prod_arr[i], last_primesA, last_primesB, N)
            prime_list.append(last_primesB)
        
        results = getLetters(prime_list)
        print("Case #{0}: {1}".format(test_case, results))

solver()
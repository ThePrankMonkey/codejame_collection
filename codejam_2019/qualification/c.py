#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Cryptopangrams

# primes = [int(x) for x in "3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107".split(" ")]
prime_set = set()

def prime_factors_first(val):
    startval = 2
    while True:
        if val % startval == 0:
            split = val // startval
            break
        startval += 1
    # print("Here are the first subprimes:\n\tval: {0}\n\tA: {1}\n\tB: {2}".format(val, startval, split))
    return startval, split

def prime_factors_other(val, a, b, maxval):
    global prime_set
    guessA = val // a
    guessB = val // b
    # print("Here are the subprimes:\n\tval: {0}\n\tA: {1}\n\tB: {2}".format(val, guessA, guessB))
    
    # check boundaries
    if guessA < 2 or guessA > maxval:
        # print("Rng Selecting:  ", guessB)
        return val, guessB
    if guessB < 2 or guessB > maxval:
        # print("Rng Selecting:  ", guessA)
        return val, guessA

    # check if they return floats
    if val % a != 0:
        # print("Mod Selecting:  ", guessB)
        return val, guessB
    if val % b != 0:
        # print("Mod Selecting:  ", guessA)
        return val, guessA

    # check if in prime_set:
    if guessA in prime_set:
        # print("Set Selecting:  ", guessA)
        return val, guessA
    if guessB in prime_set:
        # print("Set Selecting:  ", guessB)
        return val, guessB

    # check if even:
    if guessA % 2:
        # print("Even Selecting: ", guessB)
        return val, guessB
    if guessB % 2:
        # print("Even Selecting: ", guessA)
        return val, guessA

    # TODO Run through a prime solver
    # print("Yolo Selecting: ", guessB)
    return val, guessB

def getLetters(prime_list):
    alphas = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    
    # build a dict of prime to char
    prime_dict = dict(zip(sorted(set(prime_list)), alphas))
    # for i in prime_dict.items():
    #     print(i)
    crypt = ""

    # Loop through primes in order of finding
    for prime_num in prime_list:
        crypt += prime_dict[prime_num]

    return crypt

def solver():
    global prime_set
    T = int(input())
    for test_case in range(1,T+1):
        prime_set = set()
        N, L = [int(x) for x in input().split(" ")]
        prime_arr = [int(x) for x in input().split(" ")]

        # print("Processing prime: {0}, {1}".format(0, prime_arr[0]))
        last_primesA, last_primesB = prime_factors_first(prime_arr[0])
        prime_set.add(last_primesA)
        prime_set.add(last_primesA)
        prime_list = [last_primesA]
        prime_list.append(last_primesB)
        for i in range(1, len(prime_arr)):
            # print("Processing prime: {0}, {1}".format(i, prime_arr[i]))
            last_primesA, last_primesB = prime_factors_other(prime_arr[i], last_primesA, last_primesB, N+1)
            prime_set.add(last_primesB)
            prime_list.append(last_primesB)
        # print(prime_list)
        results = getLetters(prime_list)
        # print(set(primes).difference(prime_set))
        print("Case #{0}: {1}".format(test_case, results))

solver()
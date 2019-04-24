''' CodeJam 2018 - Qualification - Saving the Planet Again '''

def power(s):
    charge=1
    shot=0
    for char in s:
        if char == "S":
            shot += charge
        if char == "C":
            charge *= 2
    return shot

def hack(p):
    l = list(p)
    found_charge = False
    for i in range(len(l)):
        if found_charge:
            if l[i] == "S":
                l[i-1], l[i] = l[i], l[i-1]
                break
        if l[i] == "C":
            found_charge = True
    return "".join(l)


T = int(input())
for i in range(1, T + 1):
    D, P = input().split(" ")
    D = int(D)

    first_power = power(P)
    if first_power > D and "C" not in P:
        print("Case #{case}: {answer}".format(case=i, answer="IMPOSSIBLE"))
    else:
        count = 0
        while True:
            prePower = power(P)
            if prePower <= D:
                print("Case #{case}: {answer}".format(case=i, answer=count))
                break
            oldP = str(P)
            P = hack(P)
            count += 1
            #print("on count {}, the string {}/{}".format(count, oldP, P))
            if count > len(P):
                print("Case #{case}: {answer}".format(case=i, answer="IMPOSSIBLE"))
                break


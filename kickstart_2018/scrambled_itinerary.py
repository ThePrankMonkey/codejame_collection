#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Problem C. Sort a scrambled itinerary
# https://code.google.com/codejam/contest/4374486/dashboard#s=p2

T = int(input())
for i in range(1, T + 1):
    flight_count = int(input())
    flight_sets = []
    for j in range(flight_count):
        ticket = [input(), input()]
        flight_sets.append(ticket)
    # print("test {0}: flights {1}".format(i, flight_sets))
    ordered = [flight_sets.pop()]
    while len(flight_sets) > 0:
        for k in range(len(flight_sets)):
            # Check beginning
            if ordered[0][0] == flight_sets[k][1]:
                ordered.insert(0, flight_sets.pop(k))
                break
            # Check ending
            if ordered[-1][1] == flight_sets[k][0]:
                ordered.append(flight_sets.pop(k))
                break
        # print("test {0}: ordered {1}".format(i, ordered))

    Results = ["-".join(a) for a in ordered]
    print("Case #{case}: {answer}".format(case=i, answer=" ".join(Results)))

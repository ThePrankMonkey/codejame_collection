''' CodeJam 2018 - Qualification - Trouble Sort '''

def trouble_sort(L):
    done = False
    while not done:
      done = True
      for i in range(len(L)-2):
        if L[i] > L[i+2]:
          done = False
          L[i], L[i+2] = L[i+2], L[i]
    
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    V = results = list(map(int, input().split(" ")))
    #print("pre", V)
    trouble_sort(V)
    #print("post", V)
    V_sorted = list(V)
    V_sorted.sort()

    #print("copy", V_sorted)
    if(V == V_sorted):
        print("Case #{case}: {answer}".format(case=i, answer="OK"))
    else:
        for j in range(len(V)):
            if V[j] != V_sorted[j]:
                print("Case #{case}: {answer}".format(case=i, answer=j))
                break
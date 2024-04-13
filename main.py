def input_cky():
    nCasos = int(input())
    for i in range(nCasos):
        tc = list(map(int, input().split()))
        G = {}
        terminals = 0
        while terminals < tc[0]:
            l = input().split()
            G[l[0]] = []
            for j in range(1, len(l)):
                G[l[0]].append(l[j])
            terminals+=1
            strings = 0
            while strings < tc[1]:
                string = input()
                #ans = cky(G, L)
                if 0 :
                    print("yes")
                else:
                    print("no")
                i+=1

def cky():
    i = 0
    if i == 0:
        return 0
    else:
        return
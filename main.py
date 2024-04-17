def input_cky():
    nCasos = int(input())
    for i in range(nCasos):
        l = input()
        nt_strings = [int(i) for i in l.split()]
        G = {}
        nonterminals = 0
        while nonterminals < nt_strings[0]:
            l = input()
            l = l.split()
            G[l[0]] = []
            for j in range(1, len(l)):
                G[l[0]].append(l[j])
            nonterminals += 1
        strings = 0
        while strings < nt_strings[1]:
            l = input()
            #ans = cky(G, l)
            if 0:
                print('yes')
            else:
                print('no')
            strings += 1

def cky():
    i = 0
    if i == 0:
        return 0
    else:
        return
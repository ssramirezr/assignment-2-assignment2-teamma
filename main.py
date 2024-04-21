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
            ans = cky(G, l)
            if ans == 'yes':
                print('yes')
            else:
                print('no')
            strings += 1

def cky(G, l):
    n = len(l)
    table = []
    for i in range(n+1):
        row = []
        for j in range(n+1):
            row.append([])
        table.append(row)

    for j in range(1, n+1):
        for nt in G:  #For each nonterminal in G
            for pd in G[nt]:  #For each production of a nonterminal
                if len(pd) == 1 and pd[0] == l[j - 1]:
                    table[j - 1][j].append(nt)

        for i in range(j-2, -1, -1):
            for k in range(i+1, j):
                for nt in G:   #For each nonterminal in G
                    for pd in G[nt]:  #For each production of a nonterminal
                        if len(pd) == 2 and pd[0] in table[i][k] and pd[1] in table[k][j]:
                            table[i][j].append(nt)

    return 'yes' if 'S' in table[0][n] else 'no'

input_cky()
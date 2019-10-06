def colunaPivo(fo):
    menor = 0
    indice = -1

    for i, j in enumerate(fo):
        if j < menor:
            menor = j
            indice = i

    return indice

def linhaPivo(r, c, b):
    menor = 1000000000000000000000000000000000000000000000000

    for i in range(1, len(r)):
        if (r[i][c] > 0):
            aux = b[i]/r[i][c]

            if aux < menor:
                menor = aux
                linha = i

    a = r[linha][c]
    for i in range(0, len(r[linha])):
        r[linha][i] /= a

    return (r, linha)

def novasLinhas(r, p, c):
    aux = r
    b = []

    for i, j in enumerate(r):
        n = -aux[i][c]
        for z, x in enumerate(r[i]):
            if i != p:
                r[i][z] = (r[p][z] * n) + aux[i][z]
                # r[i][z] = round(r[i][z], 1)
            if z == (len(r[i])-1):
                b.append(r[i][z])

    return (r, b)

def valores(r):
    v = []
    c = []
    l = []
    t = len(r[0])-1
    count = 0

    for z in range(0, len(r[0])-1):
        q0 = 0
        q1 = 0
        for i, j in enumerate(r):
            if r[i][z] == 0:
                q0 += 1
            elif r[i][z] == 1:
                q1 += 1
                linha = i

        if q1 == 1 and q0 == 3:
            v.append(r[linha][t])
        else:
            v.append(0)

    return v

from calcular import colunaPivo, linhaPivo, novasLinhas, valores

fo = [1, -3.0, -5.0, 0]
r = [[0, 2.0, 4.0, 10.0], [0, 6.0, 1.0, 20.0], [0, 1.0, -1.0, 30.0]]
b = [0, 10.0, 20.0, 30.0]
qtde = 3

a = int(len(r[0])-1)
for i in range(0, len(r)):
    for j in range(a, (a+qtde)):
        if a+i == j :
            r[i].insert(j, 1)
        else:
            r[i].insert(j, 0)


r.insert(0, fo)
for j in range(a, (a+qtde)):
    r[0].insert(j, 0)

while True:
    c = colunaPivo(r[0])
    if c == -1:
        break

    r, p = linhaPivo(r, c, b)
    r, b = novasLinhas(r, p, c)

v = valores(r)

for i in range(0, len(r)):
    print(r[i])

print("\nZ = ", v[0])
for i in range(1, a):
    print("x_{", i, "} =",  v[i])

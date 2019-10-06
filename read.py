# Metodo para remover os caracteres especiais
def funcaoObjetivo(texto):
    funcs = texto[0].replace('\n', '')
    funcs = funcs.split('=')[1]
    variaveis = funcs.split('x')

    funcObj = []
    funcObj.append(1)

    for i in variaveis:
        if i != '':
            if i.find('+') > 0:
                i = i.split('+')[1]

            funcObj.append(float(i) * -1)

    funcObj.append(0)

    return funcObj

def restricoes(texto):
    b = []
    b.append(0)
    colunas = []
    func = texto

    for i in range(1,len(func)):
        restricao = func[i]
        restricao = restricao.split('<=')
        b.append(float(restricao[1]))
        variaveis = restricao[0].split('x')
        linha = []
        linha.append(0)

        for j in variaveis:
            if j.strip() != '':
                if j.find('+') > 0:
                    j = j.split('+')[1]
                    linha.append(float(j))
                elif j.find('-') > 0:
                    j = j.split('-')[1]
                    linha.append(float(j) * -1)
                else:
                    linha.append(float(j))
            else:
                linha.append(float(restricao[1]))

        colunas.append(linha)
    return (colunas, b)

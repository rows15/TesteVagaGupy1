def calcPorcentagemParticipacao():
    listaFinal=[]
    total = 0
    faturamentos = [["sp",67836.43],
                    ["rj",36678.66],
                    ["mg",29229.88],
                    ["es",27165.48],
                    ["outros",19849.53]]


    for i in range(len(faturamentos)):
        total += faturamentos[i][1]

    for i in range(len(faturamentos)):
        listaFinal.append([faturamentos[i][0],(faturamentos[i][1]/total)*100])
    print(listaFinal)
    return listaFinal

calcPorcentagemParticipacao()

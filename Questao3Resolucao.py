import json
with open(r'dados.json') as file:
    data = json.load(file)


def calcMenorFaturamentoDiario(jsonData):
    diaMinimo = 0
    valorMinimo = 0
    #check pra ver se tem algum número diferente de 0
    for i in range(len(jsonData)):
        if float(jsonData[i]["valor"]) != 0:
            valorMinimo = float(jsonData[i]["valor"])
            break
    if valorMinimo == 0:
        print("retornei0")
        return 0
            
    
    for i in range(len(jsonData)):
        diaAtual = jsonData[i]["dia"]
        valorAtual = float(jsonData[i]["valor"])
        
        if (valorAtual <= valorMinimo):
            if valorAtual != 0:
                diaMinimo = diaAtual
                valorMinimo = valorAtual

    #A questão só pede o menor valor, mas dá pra incluir o dia também se descomentar abaixo
    return valorMinimo #,diaMinimo            

def calcMaiorFaturamentoDiario(jsonData):
    diaMaximo = 0
    valorMaximo = 0
##    #check pra ver se tem algum número diferente de 0
##    for i in range(len(jsonData)):
##        if float(jsonData[i]["valor"]) != 0:
##            valorMinimo = float(jsonData[i]["valor"])
##            break
##    if valorMinimo == 0:
##        print("retornei0")
##        return 0
            
    
    for i in range(len(jsonData)):
        diaAtual = jsonData[i]["dia"]
        valorAtual = float(jsonData[i]["valor"])
        
        if (valorAtual >= valorMaximo):
            #if valorAtual != 0:
            diaMaximo = diaAtual
            valorMaximo = valorAtual

    #A questão só pede o maior valor, mas dá pra incluir o dia também se descomentar abaixo
    return valorMaximo #,diaMaximo            

def media(lista):
    return sum(lista)/len(lista)

def diasFaturamentoAcimaMedia(jsonData):
    #CriarLista
    resultadoDias = 0
    listaValores = []
    #adicionar e filtrar valores 0
    for i in range(len(jsonData)):
        
        valorAtual = float(jsonData[i]["valor"])
        if valorAtual != 0:
            listaValores.append(valorAtual)
    mediaValores = media(listaValores)
    for i in range(len(listaValores)):
        if listaValores[i] > mediaValores:
            resultadoDias += 1
    return resultadoDias





























    


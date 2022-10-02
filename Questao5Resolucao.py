def inverterCaracteresString(stringOriginal):
    stringFinal = ""
    for i in range(len(stringOriginal)):
        stringFinal += stringOriginal[-(i+1)]
    return stringFinal


stringExemplo1 = "Posso ter essa vaga?"        
print(inverterCaracteresString(stringExemplo1))

stringExemplo2 = input("digite uma string para ser invertida: ")
print(inverterCaracteresString(stringExemplo2))

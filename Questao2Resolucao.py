
## Resolução da Questão 2:
def questao2():
    number = int(input("Digite um número: "))
    y= 0 
    z= 1
    while y <= number:
        if number == y:
            return True
        y, z = z, y + z
    return False

questao2()

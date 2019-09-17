
def primeira_validacao(cpf):
    cpf = cpf
    primeira_lista = cpf[:9]
    soma = 0

    multiplicador = 10
    for numero in primeira_lista:
        soma = int(soma) + int(numero) * int(multiplicador)
        multiplicador = int(multiplicador - 1)

    verificador = 11 - (soma % 11)
    verificador = 0 if verificador > 9 else verificador

    if(int(verificador) == int(cpf[9])):
        return True
    else:
        return False

def segunda_validacao(cpf):
    cpf = cpf
    segunda_lista = cpf[:10]
    soma = 0

    multiplicador = 11
    for numero in segunda_lista:
        soma = int(soma) + int(numero) * int(multiplicador)
        multiplicador = int(multiplicador - 1)

    verificador = 11 - (soma % 11)
    verificador = 0 if verificador > 9 else verificador

    if(int(verificador) == int(cpf[10])):
        return True
    else:
        return False


cpf = input("Insira o CPF *Somente números*: ")
if(primeira_validacao(cpf) and segunda_validacao(cpf)):
    print("CPF Valido")
else:
    print("CPF Falso")

#calculadora com função

#funções
def soma (a, b):
    somar = a + b
    return somar 
def subtração (a, b):
    sub = a - b
    return sub
def multiplicação (a, b):
    produto = a * b
    return produto
def divisão (a, b):
    quociente = a / b
    return quociente

#principal
resposta = "S"
while(resposta == "S"):
    menu = """
    \033[4m                                   \033[0m
    \033[4mQual a Operação que deseja realizar\033[0m:
    
    Digite 1 = Soma
    Digite 2 = Subtrair
    Digite 3 = Multiplicar
    Digite 4 = Dividir\n """

    op = input(menu)

    if op == "1":
        a = float(input("Insira o primeiro número:"))
        b = float(input("Insira o segundo número:"))
        resultado = soma(a, b)
        print (resultado)
    elif op == "2":
        a = float(input("Insira o primeiro número:"))
        b = float(input("Insira o segundo número:"))
        resultado = subtração(a, b)
        print (resultado)
    elif op == "3":
        a = float(input("Insira o primeiro número:"))
        b = float(input("Insira o segundo número:"))
        resultado = multiplicação(a , b)
        print(resultado)
    elif op == "4":
        a = float(input("Insira o primeiro número:"))
        b = float(input("Insira o segundo número:"))
        resultado = divisão(a, b)
        print(resultado)
    else:
        print("Operação Inválida!!")

    resposta = input("Deseja fazer mais alguma operação? (S/N)").upper()
    if resposta == "N":
        print("Programa Encerrado!!")
        break
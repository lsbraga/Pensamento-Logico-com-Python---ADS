#Caixa Eletrônica

#Funções
def sacar (saldo, b):
    saque = saldo - b
    return saque

def deposito (saldo, b):
    depositar = saldo + b
    return depositar

saldo = 1000

menu = """
\033[4mMenu\033[0m
1. Ver Saldo
2. Sacar
3. Depositar
4. Sair \n"""

cn = "S"

while(cn):

    res = input(menu)

    if res == "1":
        print("Saldo Disponivel: R$ {:.2f}".format(saldo))

    elif res == "2":
        print("Saldo Disponivel: R$ {:.2f}".format(saldo))
        b = float(input("Digite o valor que deseja sacar:\n"))
        resultado = sacar(saldo, b)
        saldo = resultado
        print("""
    Você sacou: R$ {:.2f}
    Saldo Disponivel: R$ {:.2f}""".format(b, resultado))

    elif res == "3":
        print("Saldo Disponivel: R$ {:.2f}".format(saldo))
        b = float(input("Digite o valor que deseja depositar:\n"))
        resultado = deposito(saldo, b)
        saldo = resultado
        print("""
    Você depositou: R$ {:.2f}  
    Saldo Disponivel: R$ {:.2f}""".format(b, resultado))
        
    elif res == "4":
        print("Programa Encerrado!!")
        break
    else:
        print("Operação Inválida!!")

    cn = input("Deseja fazer outra movimentação? (S/N)").upper()
    if cn == "N":
        print("Program Encerrado!!")
        break
#Identificador Triangulo

print("IDENTIFICADOR TRIANGULO")

lado1 = float(input("Digite o valor do primeiro lado:\n"))
lado2 = float(input("Digite o valor do segundo lado:\n"))
lado3 = float(input("Digite o valor do terceiro lado:\n"))

tri1 = lado1 + lado2
tri2 = lado2 + lado3
tri3 = lado1 + lado3

if tri1 > lado3 and tri2 > lado1 and tri3 > lado2:
    print("Você pode formar um triangulo")
else:
    print ("Você não tem um triangulo")
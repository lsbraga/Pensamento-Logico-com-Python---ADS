#Maior Número

print("DESCUBRA QUAL É O MAIOR NÚMERO")

maior = float(input("Digite o primeiro númeor:\n"))

for i in range(2, 6):
    numero = float(input("Digite o {}º número: ".format(i)))
    if numero > maior:
        maior = numero

print("O maior número é:", maior)
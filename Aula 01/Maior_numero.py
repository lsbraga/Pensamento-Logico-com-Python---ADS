#Maior Número

#Inicio
print("DESCUBRA QUAL É O MAIOR NÚMERO")
#Entrada
maior = float(input("Digite o primeiro númeor:\n"))
#Ação
for i in range(2, 6):
    numero = float(input("Digite o {}º número: ".format(i)))
    if numero > maior:
        maior = numero
#Saída
print("O maior número é:", maior)
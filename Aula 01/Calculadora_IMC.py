#Calculadora IMC

#inicio
print ("Calculador de Imc - índice de Massa Corporal")
#EntradaI
peso = float(input("Digite o seu peso: (Ex:50.0)\n"))
altura = float(input("Digite a sua altura em CM: (Ex: 170)\n"))
#Ação
imc = peso / (altura*altura) * 10000
#Saída
print ('O seu IMC é:', "{:.2f}".format(imc))
#Decisão
if imc < 18.5:
    print('Você está abaixo do seu peso ideal')
elif imc < 24.5:
    print("Você está no peso ideal")
elif imc < 39.9:
    print("Você está com obesidade")
else:
    print('Você está com obesidade mórbida')
#Fim
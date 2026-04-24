print(" ---Calculadora de IMC--- ")
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso/(altura*altura)
print(f"IMC: {round(imc,2)}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc< 30:
    print("Sobrepeso")
else:
    print("Obesidade")
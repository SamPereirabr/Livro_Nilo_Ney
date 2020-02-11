print("Vamos identificar o maior e o menos número de uma sequencia digitada. ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3= int(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num1 > num2:
    maior = num2
if num2 > num3:
    maior = num3
print(f"O maior número é: {maior}")

if num1 < num2:
    menor = num2
if num2 < num3:
    menor = num3
print(f"O menor número é: {menor}")

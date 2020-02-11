print("Vamos calcular o valor do seu salário. O valor do aumento é variável conforme os seus rendimentos. ")

salário_antigo = int(input("Digite o valor do seu salário em reais: "))

base = salário_antigo

if base >= 1250:
    base = salário_antigo + (salário_antigo * 10/100)
if base < 1250:
    base = salário_antigo + (salário_antigo * 15/100)

print(f"O seu novo salário será de R$ {base}.")
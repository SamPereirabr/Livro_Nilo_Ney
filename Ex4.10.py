#Calculo do custo de Fornecimento de Energia elétrica

qtde = int(input("Quantos kW foram consumidos durante o mês atual? "))
tipo = str(input("Sua instalação é de qual tipo? Industrial (I), Residencial (R) ou Comercial (C): "))
valor = 0

if tipo == "R" and qtde <= 500:
    valor = qtde * 0.40
if tipo == "R" and qtde > 500:
    valor = qtde * 0.65
if tipo == "C" and qtde <= 1000:
    valor = qtde * 0.55
if tipo == "C" and qtde > 500:
    valor = qtde * 0.60
if tipo == "I" and qtde <= 5000:
    valor = qtde * 0.55
if tipo == "I" and qtde >= 500:
    valor = qtde * 0.60

print(f" {valor:5.2f}")





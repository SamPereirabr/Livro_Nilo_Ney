print("Qual a distância que você deseja percorrer hoje? ")

dist = int(input("Digite o valor em km: "))
preco = 0

if dist <=200:
    preco = 0.50 * dist
else:
    preco = 0.45 * dist

print(f"O valor final da sua viagem será de R$ {preco}")
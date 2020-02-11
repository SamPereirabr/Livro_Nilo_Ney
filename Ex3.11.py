produto = int (input("Digite o preço do produto: "))
desconto = int (input("Qual o valor do desconto a ser concedido? "))

valor_desconto = (produto * desconto/100)

final = produto - valor_desconto

print(f"O valor do seu desconto foi de R$ {valor_desconto}, e o preço final do seu produto será de R$ {final}")
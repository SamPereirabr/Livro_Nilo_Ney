print("Vamos calcular a quantidade de dias que você já perdeu devido ao cigarro. ")

qtde_cigarros = int(input("Digite a quantidade de cigarros que você fuma por dia: "))
anos = int(input("Por quantos anos, você já fuma? "))

dias = (qtde_cigarros * 10 * anos * 365) / 1440

print(f"Você já perdeu {dias:1.0f} dias de vida, se considerar anos que tivemos anos bisextos, talvez um pouco mais! ")
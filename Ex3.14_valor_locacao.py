print("Bem vindo a Samuel Locações! Vamos calcular o custo de locação do seu veículo. ")

diárias = int (input("Digite o número de diárias de locação: "))
km = int( input("Qual foi a quilometragem rodade? "))

valor_locação = (diárias * 60) + (km * 0.15)

print(f"O valor final da sua locação é de R$ {valor_locação}")
print("Vamos calcular o tempo esperado para a sua viagem. Entre com a velocidade esperada, e  a distância entre as duas cidades. ")
distância = int (input("Qual a distância entre onde está agora e a cidade, para onde vai? Use quilômetros.  "))
velocidade = int (input("Qual a velocidade média se consegue fazer nesse trecho? Use km/h "))
tempo = distância / velocidade

print(f"Com esses valores, o tempo estimado da viagem é de {tempo} horas")
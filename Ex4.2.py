velocidade = int(input("Digite o valor da velocidade do veículo: "))

if velocidade > 80:
    print(f" Você foi multado devido ao excesso de velocidade, o valor da sua multa é de R$ {(velocidade - 80)*5}")
if velocidade <= 80:
    print("Continue assim! Sua velocidade está dentro do permitido")
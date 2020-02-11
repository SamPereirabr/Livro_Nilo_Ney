salário = int (input("Digite o salário do funcionário: "))
aumento = int (input("Qual o percentual de aumento do salário do mesmo? "))

montante = (salário * aumento / 100)
novo_salário = salário + montante



print(f"O novo salário do funcionário é de R$ {novo_salário}, o seu aumento foi de R$ {montante}")
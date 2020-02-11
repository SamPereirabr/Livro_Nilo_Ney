#Programa de Teste de aprovação de crédito bancário - Sem Taxa de Juros

print("Entre com os valores para simulação do financiamento")

valor = int(input("Digite o valor do imóvel pretendido: "))
salario = int (input("Qual a sua renda mensal bruta? "))
prazo = int (input("Qual o prazo para pagamento do financiamento? "))
prest = int

if (valor / prazo) >= (salario * 0.3):
    print("O valor máximo da prestação deve ser de 30% do seu rendimento mensal")

else:
    if ((valor / prazo) < (salario * 0.3)):
        prest = valor / prazo

print(f"O valor da sua prestação mensal será de R$ {prest}")
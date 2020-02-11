a = input("Digite um número qualquer entre 1 e 10")
print (f"Você digitou o número {a}, e ele é menor do que precisavamos")

#COnversão de entrada de dados
anos = int (input("Qual o seu tempo de trabalho na empresa?(use numeros inteiros)"))
valor_por_ano = float(input("Valor por ano: "))
bônus = anos * valor_por_ano
print(f"O seu bônus será de R$ {bônus:5.2f}")

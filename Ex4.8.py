print("Bem-vindo a minicalculadora digital!")

num1 = int(input("Digite o primeiro número da operação: "))
num2 = int(input("Digite o segundo número da operação: "))

res = int

oper = str (input("Qual operação deve ser realizada? Soma, multiplicação, divisão ou subtração? ")
)

if oper == "soma":
    res = num1 + num2
elif oper == "multiplicação":
    res = num1  * num2
elif oper == "divisão":
    res = num1 / num2
elif oper == "subtração":
    res = num1 - num2
else:
    print("Digite a operação conforme demonstrada. O sistema é sensível a acentuações. ")

print(f"O valor da operação é de  {res}")
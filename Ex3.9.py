from datetime import datetime

a = int (input("Vamos realizar a contagem de segundos que já se foram no seu dia. Por favor, digite somente as horas: "))
b = int (input("Agora, digite a quantidade de minutos: "))
c = int (input("E os segundos? Seja rápido!"))

s = (a*3600) + (b*60) +c
r = (3600 * 24) - s

print(f"Você já perdeu {s} segundos de vida hoje. Aproveite bem {r} segundos restantes! " )
# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))

if sinal == "+":
  c = "{} + {} = {}".format(n1, n2 , n1 + n2)
elif sinal == "-":
  c = "{} - {} = {}".format(n1, n2 , n1 - n2)
elif sinal == "*":
  c = "{} * {} = {}".format(n1, n2 , n1 * n2)
elif sinal == "/":
  c = "{} / {} = {}".format(n1, n2 , n1 / n2)
else:
  print("Invalid sinal")
  
print(c)
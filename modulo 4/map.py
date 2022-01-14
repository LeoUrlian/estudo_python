# map

def dobro(x):
  return x * 2

valor = [1, 2, 3, 4, 5]

valor_dobro = map(dobro, valor)

valor_dobro = list(valor_dobro)

print(valor_dobro)
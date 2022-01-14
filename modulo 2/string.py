# concatenar strings
a = "Leonardo\n"
b = "Sudati"

print(a + b)

# calcular qtd dos caracteres
x = "ubecyewvcybsancasoii"

print(len(x))

# imprimir letras especificas
print(a[0])
print(a[1])
print(a[2])
print(a[0:8])

# converter para minusculo = lower / converter para maiusculo = upper
print(a.lower())
print(a.upper())

# remover um caracter especial do inicio e do fim da string 
print(a.strip())

# converter uma string em uma lista
frase = "O rato roeu a roupa do rei de Roma"

print(frase.split())

# fazer uma busca dentro de um string
print(frase.find("rei"))

# substituir uma palavra por outra em uma string 
print(frase.replace("rei", "rainha"))
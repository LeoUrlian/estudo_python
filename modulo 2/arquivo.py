# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")

# READ
# texto = arquivo.read()

# texto = arquivo.readline()

# texto = arquivo.readlines()

# print(texto)

# WRITE
newArquivo = open("arquivo02.txt", "w")

newArquivo.write("Esse é o meu novo arquivo02")

newArquivo.close()
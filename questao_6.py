lista = list()
i = 0
palavra_longa = ""
escolha = int(input("Quantos elementos terá em sua lista ?\n"))
while i < escolha:
    nome = input("Digite uma palavra: ")
    lista.append(nome)
    i=i+1
  
for palavra in lista:
    if(len(palavra) > len(palavra_longa)):
        palavra_longa = palavra
print(lista)
print("a palavra mais longa é: ",palavra_longa)
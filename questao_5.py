lista = list()
contador = 0
i = 0

escolha = int(input("Quantos elementos terá em sua lista ?\n"))
while i < escolha:
    nome = input("Digite um nome: ")
    lista.append(nome)
    i=i+1
for letra in lista:
    if(letra[0]=="a" or letra[0]=="A"):
        contador+=1
print(lista)
print(contador)

lista_valores = list()
i = 0
maior = 0
escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)
for y in lista_valores:
    if(maior < y):
        maior = y
print("O maior número da lista é: ",maior)
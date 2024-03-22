lista_valores = list()
i = 0
somador = 0
escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)
for y in lista_valores:
    somador = somador+y
print("A soma de todos os elementos da lista é: ",somador)
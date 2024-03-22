lista_valores = list()
i = 0
media = 0
somador = 0
escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)
for y in lista_valores:
    somador = somador + y
media = somador/escolha        
print("O média dos números da lista é: ",media)
lista_valores = list()
lista_Srepetir = list()
i = 0

escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)

for num in lista_valores:
    if num not in lista_Srepetir:
        lista_Srepetir.append(num)

print(lista_Srepetir)



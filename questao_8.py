lista_valores = list()
lista_impar = list()
i = 0

escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)
for x in lista_valores:
    if x %2 != 0:
        lista_impar.append(x)
lista_impar.sort()
print("os numeros pares são: ", lista_impar)
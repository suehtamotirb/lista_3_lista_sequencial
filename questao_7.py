lista_valores = list()
lista_par = list()
i = 0

escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1
print(lista_valores)
for x in lista_valores:
    if x %2 == 0:
        lista_par.append(x)
lista_par.sort()
print("os numeros pares são: ", lista_par)
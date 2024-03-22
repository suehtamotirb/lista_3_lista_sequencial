lista_valores = list()
lista_valores2 = list()
ambas = list()
i = 0
z = 0
a = 0
maior = 0
escolha = int(input("Quantos elementos terá na sua lista ?\n"))
while i < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores.append(valor)
    i = i+1

escolha = int(input("Quantos elementos terá na sua segunda lista ?\n"))
while z < escolha:
    valor = int(input("Digite um valor a ser inserido na lista: "))
    lista_valores2.append(valor)
    z +=1

if len(lista_valores) > len(lista_valores2):
    maior = len(lista_valores)
else:
    maior = len(lista_valores2)
if len(lista_valores)<= len(lista_valores2):
    for a in range (maior):
        for b in lista_valores:
            if b == lista_valores2[a]:
                ambas.append(b)
else:
    for a in range (maior):
        for b in lista_valores2:
            if b == lista_valores[a]:
                ambas.append(b)              

print("Sua primeira lista: ",lista_valores)
print("Sua segunda lista: ",lista_valores2)
print("Os numeros que aparecem em ambas são: ",ambas)
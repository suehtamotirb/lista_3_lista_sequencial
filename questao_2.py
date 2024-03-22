lista = list()
i = 0

escolha = int(input("Quantos elementos terá em sua lista ?\n"))
while i < escolha:
    nome = input("Digite um nome: ")
    lista.append(nome)
    i=i+1
qnt = len(lista)    
print(lista)
print("Existem ",qnt," elementos na lista!!")

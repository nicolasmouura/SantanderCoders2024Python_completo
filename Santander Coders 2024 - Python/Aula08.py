#AULA DE ESTRUTURA DE LISTAS

# > Antes
nota1 = 10
nota2 = 9
nota3 = 4.7

# Com lista
notas = [10, 9, 4.7]

#CRIANDO LISTAS

Lista = []
lista = list()
lista = [19, "Nícolas", 3.14159, True]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [19, "Nícolas", 3.14159, False]

# Você pode printar a lista de acordo com a ordem, começando do número "0"
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Você também pode começar do último elemente da lista que é o "-1"
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])


# SLICES 

lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3]) # pega os itens da lista do 0 até o 2
print(lista[3:6]) # pega os itens da lista do 3 até o 5
print(lista[3:])  # pega os itens da lista do 3 até o final
print(lista[2:6:2]) # começa do 2 vai até o 6, mas pula de 2 em 2 (começo, final e step)


# PERCORRER ELEMENTOS DA LISTA COM "FOR"

for elemento in lista:
    print(elemento)

#UTILIZANDO OS ÍNDICES

print("comprimento da lista: ", len(lista))

for i in range(len(lista)):
    print(i)
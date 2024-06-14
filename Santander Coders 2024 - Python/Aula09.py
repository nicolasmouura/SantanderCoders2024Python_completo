#AULA DE METODOS E FUNÇÕES DE LISTAS

# MÉTODOS DE LISTAS
lista = [1, 3, 12, 8, 2]

# Append ----> Função pra adicionar elementos no final da lista

print("Antes do append: ", lista)

lista.append(3)

print("Depois do append: ", lista)

# Insert ----> Escolhe qual a posição que você quer por o elemento na lista, e escolhe o elemento

lista.insert(2, 10) # Primeiro número você escolhe a posição, em segundo o que quer adicionar

print("Lista após o insert: ", lista)

# Extend ----> Juntar 2 listas

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Lista após do extend: ", lista)

# Pop ----> Tira um elemento da lista, escolhendo pelo número da posição que ele se encontra

lista.pop()

print("Lista após o pop: ", lista)

lista.pop(0)

print("Lista após o pop: ", lista)

# Remove ----> Tira um elemento da lista especificando qual elemento deseja retirar(se tiver elementos iguais ele tira o primeiro que encontra)

lista.remove(3)

print("Lista após o remove: ")

# Count ----> Contar quantas vezes o elemento aparece na sua lista

print("Quantidade de 2 na lista: ", lista.count(2))

# Index ----> Te diz o índice de um determinado elemento dentro da lista

print("Índice do elemento 12: ", lista.index(12))

# Sort ----> Ordena sua lista da forma que você escolher

lista.sort()

print(lista)

# Ordenando sua lista de forma decrescente
lista.sort(reverse=True)

print(lista)

# FUNÇÕES PRA LISTAS

#len ---> Conta os elementos da lista
print(len(lista))

#sum ---> Soma os elementos da lista
print(sum(lista))

#max ---> Revela o maior elemento da lista
print("Maior elemento da lista: ", max(lista))

#min ---> Revela o menor elemento da lista
print("Menor elemento da lista: ", min(lista))
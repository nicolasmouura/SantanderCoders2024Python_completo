#AULA DE LAÇOS DE REPETIÇÃO (WHILE)

""" WHILE NO PORTUGUÊS SIGNIFICA "ENQUANTO"
Ou seja, enquanto tal coisa estiver acontecendo vai ser 
verdadeira ou falsa, de acordo com sua escolha """

# EXEMPLO 1 ----> Adivinhar o número sorteado

numero_sorteado = 15
numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
      numero_escolhido = int(input("Você errou, escolha um número entre 1 e 20 novamente: "))
 
print("Parabéns, você acertou o numero era", numero_sorteado)

# EXEMPLO 2 ----> Estrutura com contador

contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1 
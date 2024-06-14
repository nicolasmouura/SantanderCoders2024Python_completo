#AULA DE VARIÁVEIS

# 1. Variáveis

#Tipos de variáveis:
#   int = usada pra números inteiros (sem partes decimais)
#   float = usada pra números reais (com casas decimais)
#   str = cadeias de caracteres, ou seja, ddados textuais (string)
#   bool = valores lógicos (booleanos): True or False

#EXEMPLOS:
idade = 26
altura = 1.77
nome = "Nícolas Moura"
estudando = True

#COMO DESCOBRIR QUAL O TIPO DA VARIÁVEL SE VOCÊ NÃO SOUBER:
print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))

# OBTENDO DADOS DE USUÁRIO E SALVANDO EM VARIÁVEIS
linguagem = input("Qual é a linguagem de programação que você está estudando? ")
print('A linguagem que você está estudando é', linguagem)
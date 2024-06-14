#AULA DE FUNÇÕES

# 1. Oque são funções e como utilizá-las? 

# Funções que já usamos anteriormente...

"""
print() # Imprime uma mensagem (int, float, str) no console (terminal, cmd)
input() # Retorna um dado informado pelo usuário (entrada padrão)
len()   # Recebe uma lista e retorna o tamanho dessa lista
max() """   # Retoma o maior valor de ua lista

# 2. Criação de funções

def saudacao():
    print("Seja bem-vinda(o)! ")
    print("É um prazer ter você fazendo parte desse curso! ")
    
saudacao()    
saudacao() 
saudacao() 


# FUNÇÕES COM PARÃMETRO
def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}! ")
    print(f"É um prazer ter você fazendo parte do curso de {curso}! ")

saudacao("Nícolas", "Python")
saudacao("João", "Militar")


# FUNÇÕES COM PARÃMETRO DEFAULT
def saudacao(nome, curso= "Python"):
    print(f"Seja bem-vinda(o), {nome}! ")
    print(f"É um prazer ter você fazendo parte do curso de {curso}! ")

saudacao("Nícolas")

# FUNÇÕES COM RETORNO

# Exemplo 1
def soma(num1, num2):
    return num1+ num2

resultado = soma(5,7)

print("O resultado da soma é", resultado)

# Exemplo 2
def calculadora(num1,num2, operacao= "+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora(10,20)

print(resultado)

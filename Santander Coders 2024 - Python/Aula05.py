#AULA DE ESTRUTURAS CONDICIONAIS

idade = 20

# "if" seria o mesmo no português do que "se"
# "else" é uma instrução para caso o "if" não seja verdadeiro. Pode ser dita como "caso não"

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#EXEMPLO 1

""" Imagine que você queira imprimir "Aprovada(o)", caso o estudante tenha uma 
média superior ou igual a 7, e "Reprovada(o)", caso a média seja inferior a 7. """

media = float(input("Informe a média do estudante: "))

if media >= 7:
    print("Você foi aprovada(o)! ")
elif media >= 5:
    print("Recuperação ")
else:
    print("Voce foi reprovada(o). ")

#EXEMPLO 2

media = 10
presenca = 100

# Usando a função "and" você precisa que os dois sejam verdadeiros pra ser aprovado
if media >= 7 and presenca >= 70:
    print("Você foi aprovada(o)")
else:
    print("Você foi reprovada(o). ")

# Usando a função "or" você precisa que uma coisa ou outra seja verdadeira pra ser aprovado, nesse caso não faz sentido usa-lá
if media >= 7 or presenca >= 70:
    print("Você foi aprovada(o)")
else:
    print("Você foi reprovada(o). ")
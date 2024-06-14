#AULA DE LAÇOS DE REPETIÇÃO (FOR)

# A função "for" é a mesma coisa que "para" no português.
# Os número na função for sempre são contados até o numero antecessor do número que você escolheu. Ex: se escol10, vai ser contado até o 9

#Função "for" com o valor de início
for variavel in range(5):
    print(variavel)

#Função "for" com o valor de início e parada
for variavel in range(5,15):
    print(variavel)

#Função "for" com o valor de início, parada e um step
for variavel in range(5,15,2):
    print(variavel)

#EXEMPLO 1 ----> MÉDIA DE NOTAS
soma = 0

for i in range(1,4):
    nota = float(input(f"Informe a sua nota {i}: "))
    soma = soma + nota #soma += nota 

print(soma/3)
    
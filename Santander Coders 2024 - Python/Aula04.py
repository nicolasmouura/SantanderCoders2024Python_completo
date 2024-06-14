#AULA DE  CONVERSÃO DE TIPOS
idade = "5"
numero1 = "20"
numero2 = "10"

print(numero1 + numero2) #Junção de textos, porque as variáveis à cima estão sendo consideradas como strings(str)

#COMO CONVERTER EXEMPLO 1
idade = "26" #"STRING"
print(idade, type(idade))

idade_inteira = int(idade) #CONVERTENDO DE "STRING(STR)" PARA "INTEIRO(INT)"
print(idade_inteira, type(idade_inteira))

#COMO CONVERTER EXEMPLO 2
altura = float(input("Informe a sua altura"))
print(altura, type(altura))


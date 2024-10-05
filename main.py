#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("Os números de 1 a 7, vão de domingo até sábado em que dia você está?(Ponha em números)"))

if dia == 1:
    dia = 'Domingo'
elif dia == 2:
    dia = 'Segunda-feira'
elif dia == 3:
    dia = 'Terça-feira'
elif dia == 4:
    dia = 'Quarta-feira'
elif dia == 5:
    dia = 'Quinta-feira'
elif dia == 6:
    dia = 'Sexta-feira'
elif dia == 7:
    dia = 'Sábado'
else:
    dia = "inválido."
 
print("O dia em que você está é :", dia)

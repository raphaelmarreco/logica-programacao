"""
Projeto - Curso Analista de Dados - EBAC
#CALCULADORA INTELIGENTE
Raphael Marreco
"""

oper = 0 #Var de Seleção de Operação
num1 = 0 #Var Input 1
num2 = 0 #Var Input 2
result = 0 #Var Resultado﻿

print('Insira abaixo os números a serem utilizados:\n')

num1 = float(input("Digite o primeiro número:")) #Entrada do primeiro valor
print("O primeiro número obtido é:", num1, "\n")

num2 = float(input("Digite o segundo número:")) #Entrada do segundo valor
print("O segundo número obtido é:", num2, "\n")

while (oper != "Sair"): #Laço de repetição p/ seleção de operação e execução
	
	print(" 1.Adição, 2.Subtração, 3.Multiplicação, 4.Divisão, 5.Sair\n")
	oper = input("Escolha uma operação dentre as opções ou se deseja sair:")

	if (oper == "Adição" or oper == "adição" or oper == 1 or oper == "1"): #Condições p/ adição
		result = num1 + num2
		print(num1, "+", num2, "=", result, "\n")

	elif (oper == "Subtração" or oper == "subtração" or oper == 2 or oper == "2"):#Condições p/ subtração
		result = num1 - num2
		print(num1, "-", num2, "=", result, "\n")

	elif (oper == "Multiplicação" or oper == "multiplicação" or oper == 3 or oper == "3"):#Condições p/ multip.
		result = num1 * num2
		print(num1, "x", num2, "=", result, "\n")

	elif (oper == "Divisão" or oper == "divisão" or oper == 4 or oper == "4"): #Condições p/ divisão
		result = num1 / num2
		print(num1, "/", num2, "=", result, "\n")

	elif (oper == "Sair" or oper == "sair" or oper == 5 or oper == "5", "\n"): #Condições p/ sair
		break

	else:
		print("Não foi possível reconhecer a operação desejada. Por favor tente novamente.\n") #Condição de erro de digitação por parte do usuário, com retorno à seleção sem quebra necessária do Loop.
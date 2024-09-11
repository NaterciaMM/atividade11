# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("insira a idade: "))

if idade <= 12:
    print ("criança")

elif 13>=idade<=17:
    pint ("adolescente")

if 18>=idade<=59:
    print("adulto")

elif idade>=60:
    print("veio")
    

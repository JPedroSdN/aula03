nome = input("digite o nome do individuo: ")
idade = int(input("digite a idade do individuo: "))
salario = float(input("digite o salario do individuo: "))
aumento = float(input("porcentagem de aumento: "))
valor_real = (salario * aumento) / 100
salario_final = salario + valor_real

print(f"{nome} tem {idade} anos e ganha {salario}."
      f"Com o aumento de {aumento} % seu salario passará a ser {salario_final} ")

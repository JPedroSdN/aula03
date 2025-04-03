Tipo = input(f"Selecione o combustivel (G - gasolina ou E - etanol): ")
Quantidade = float(input("Quantos litros: "))
G = 5.8
E = 4.9
Valor = 0

if Tipo == "G" or "g":
    Valor = G * Quantidade
elif:
    Tipo == "E" or "e":
    Valor = E * Quantidade
else:
    print("Tipo de combustivel inválido")

print(f"O valor total é {Valor:.2f}")

N1 = float(input("primeira nota: "))
N2 = float(input("segunda nota: "))
N3 = float(input("terceira nota: "))
media = (N1+N2+N3)/3
if media >= 7:
    print(f"aprovado ({media})")
else:
    if media <= 4:
        print(f"reprovado ({media})")
    else:
        print(f"recuperação")
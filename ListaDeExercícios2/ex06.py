def ConverterNota(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

nota_usuario = float(input("Insira a sua nota (de 0 a 100): "))


nota_convertida = ConverterNota(nota_usuario)

print("Sua nota convertida é:", nota_convertida)
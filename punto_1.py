Elementos = int(input("Ingresa la cantidad de elementos: "))
NumerosReales= []

for total in range(Elementos):
    total = float(input("Ingresa un número real: "))
    NumerosReales.append(total)

Suma : int = 0
for i in NumerosReales:
    Suma += i
    promedio = (Suma/len(NumerosReales))
    
print()
print(f"El promedio de {NumerosReales} es {promedio}")
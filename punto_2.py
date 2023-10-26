Elementos = int(input("Ingresa la cantidad de elementos: "))
NumerosRealesA = []
NumerosRealesB = []

for TotalA in range(Elementos):
    TotalA = float(input("Ingresa un valor real para a: "))
    NumerosRealesA.append(TotalA)

for TotalB in range(Elementos):
    TotalB = float(input("Ingresa un valor real para b: "))
    NumerosRealesB.append(TotalB)
    
ProductoPunto : int = 0

for i in range(Elementos):
    ProductoPunto += (NumerosRealesA[i]*NumerosRealesB[i])
    
print()
print(f"El producto punto de la lista {NumerosRealesA} y la lista {NumerosRealesB} es {ProductoPunto}")
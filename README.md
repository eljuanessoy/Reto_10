# Reto #10 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

+ En este punto, solicité al usuario que ingresara la cantidad de datos que deseaba incluir en la lista y, a continuación, creé una lista vacía. Luego, implementé un bucle for que recorría desde 0 hasta el número de datos que el usuario deseaba ingresar, por ejemplo, si eran 5, el bucle pedía al usuario que ingresara 5 números y los añadía a la lista. Después, declaré una variable llamada "suma" y utilicé otro bucle for para recorrer cada dato de la lista, sumándolos entre sí. Al finalizar este bucle, la variable "suma" contenía la suma de todos los datos en la lista. A continuación, definí una última variable llamada "promedio", que se calculó dividiendo la variable "suma" por el número de datos en la lista

```python
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
```

### 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

+ En este caso, ambas listas debían ser idénticas, por lo que dependían del mismo valor inicial. Inicialicé una variable en 0, que fue introducida en un bucle for. Dentro de este bucle, multiplicé los elementos de ambas listas en orden. Luego, sumé todas estas multiplicaciones a medida que avanzaba a través de los datos de las listas hasta que se agotaron e imprimi el resultado.

```python
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
```

### 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

+ Dentro de la función principal, comencé por crear una lista vacía y una variable. Luego, solicité al usuario que ingresara la cantidad de valores que tendria el arreglo. Después, implementé un bucle for que funcionaría para la cantidad de elementos ingresados por el usuario, agregando los elementos ingresados por el usuario al arreglo en cada iteración. Luego conte la cantidad de elementos iguales a cero en el arreglo e imprimi la función.

```python
if __name__ == "__main__":
    lista = []
    Valores = 0
    j = int(input("Ingresa la cantidad de valores: "))
    for Valores in range (j):
        Valores = float(input("Ingrese un número real: "))
        
print()
print(f"La cantidad de ceros que aparecen son: {lista.count(0)}")
```

### 4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

+ Los algoritmos de ordenamiento (sorting) son procedimientos o conjuntos de instrucciones diseñados para organizar un conjunto de datos en un orden específico, generalmente de manera ascendente o descendente. Estos algoritmos juegan un papel esencial en el campo de la informática y la ciencia de la computación, ya que se aplican en una amplia gama de usos que abarcan desde la gestión de bases de datos hasta la búsqueda y organización de información.

+ Bubble Sort, es un algoritmo de ordenamiento sencillo que opera comparando elementos consecutivos en una lista y, si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que la lista completa esté organizada. A pesar de su facilidad de comprensión e implementación, su eficiencia es bastante limitada en comparación con otros algoritmos de ordenamiento, lo que lo convierte en una elección subóptima para listas de gran tamaño. Su complejidad temporal, tanto en promedio como en el peor de los casos, es significativamente alta, lo que implica que requiere una cantidad considerable de tiempo para ordenar listas extensas. Por lo tanto, Bubble Sort no se recomienda para aplicaciones que deben manejar conjuntos de datos extensos de manera eficiente.

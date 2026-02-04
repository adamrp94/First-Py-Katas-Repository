# 1. Función que recibe una cadena de texto y devuelve un diccionario con las frecuencias de cada letra (sin contar espacios).
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra != " ":  # No consideramos los espacios
            letra = letra.lower()  # Opcional: pasar a minúsculas para contar 'A' y 'a' igual
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias
print(frecuencia_letras("Hola Mundo"))

# 2. Dada una lista de números, obtener el doble de cada valor usando map().
numeros = [1, 5, 10, 15]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

# 3. Función que devuelve las palabras de una lista que contienen una palabra objetivo.
def buscar_palabra_objetivo(lista_palabras, objetivo):
    # Usamos una lista de comprensión para filtrar
    return [palabra for palabra in lista_palabras if objetivo in palabra]
print(buscar_palabra_objetivo(["casa", "coche", "perro", "casita"], "casa"))

# 4. Función que calcule la diferencia entre los valores de dos listas usando map().
def diferencia_listas(lista1, lista2):
    # La función map resta los elementos de ambas listas posición por posición
    return list(map(lambda x, y: x - y, lista1, lista2))
print(diferencia_listas([10, 20, 30], [2, 5, 8]))

# 5. Función para calcular la media y determinar el estado (aprobado/suspenso).
def evaluar_media(lista_notas, nota_aprobado=5):
    if not lista_notas:
        return (0, "suspenso")
    
    media = sum(lista_notas) / len(lista_notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    return (media, estado)
print(evaluar_media([4, 6, 8, 3]))

# 6. Función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: " ".join(map(str, t)), lista_tuplas))

print(tuplas_a_strings([(1, "A"), (2, "B")]))

# 8. Programa que pida al usuario dos números e intente dividirlos manejando excepciones.
def dividir():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print(f"Resultado: {num1 / num2}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error en la operación: {e}")

# dividir() # Descomentar para probar manualmente

# 9. Función que tome una lista de mascotas y excluya las prohibidas usando filter().
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))

print(filtrar_mascotas(["Perro", "Gato", "Tigre"]))

# 10. Función que calcule el promedio y lance una excepción personalizada si la lista está vacía.
class ListaVaciaError(Exception):
    pass

def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)

try:
    print(calcular_promedio([10, 20, 30]))
except ListaVaciaError as e:
    print(e)

# 11. Programa que pida la edad y maneje excepciones si está fuera de rango (0-120).
def validar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if 0 <= edad <= 120:
            print(f"Edad registrada: {edad}")
        else:
            print("Edad fuera de rango permitido.")
    except ValueError:
        print("Error: Entrada no válida.")

# validar_edad() # Descomentar para probar manualmente

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa map()
def longitud_palabras(frase):
    return list(map(len, frase.split()))

print(longitud_palabras("Python es genial"))

# 13. Genera una función que devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas (sin repetidos). Usa map()
def transformar_letras(caracteres):
    return list(map(lambda c: (c.upper(), c.lower()), set(caracteres)))

print(transformar_letras("aabbcc"))

# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra específica. Usa filter()
def filtrar_por_inicio(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

print(filtrar_por_inicio(["casa", "árbol", "coche"], "c"))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

print(sumar_tres([1, 2, 3]))

# 16. Función que devuelve palabras más largas que n usando filter().
def filtrar_palabras_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: len(p) > n, palabras))

print(filtrar_palabras_largas("Python es un lenguaje muy potente", 4))

# 17. Función que convierte una lista de dígitos en el número correspondiente usando reduce().
from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

print(lista_a_numero([5, 7, 2]))

# 18. Programa que filtra estudiantes con calificación mayor o igual a 90 usando filter().
estudiantes = [
    {"nombre": "Adam", "edad": 20, "calificación": 95},
    {"nombre": "Maria", "edad": 22, "calificación": 88},
    {"nombre": "Juan", "edad": 19, "calificación": 92}
]

estudiantes_top = list(filter(lambda e: e["calificación"] >= 90, estudiantes))
print(estudiantes_top)

# 19. Función lambda que filtra los números impares de una lista.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

print(filtrar_impares([1, 2, 3, 4, 5, 6]))

# 20. Obtener una nueva lista sólo con los valores int usando filter().
def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print(solo_enteros([1, "hola", 2, "mundo", 3]))

# 21. Función que calcula el cubo de un número mediante una función lambda.
cubo = lambda x: x ** 3

print(cubo(3))

# 22. Obtener el producto total de una lista numérica usando reduce().
def producto_total(numeros):
    return reduce(lambda x, y: x * y, numeros)

print(producto_total([1, 2, 3, 4]))

# 23. Concatenar una lista de palabras usando reduce().
def concatenar_palabras(palabras):
    return reduce(lambda x, y: x + y, palabras)

print(concatenar_palabras(["Hola", " ", "Mundo"]))

# 24. Calcular la diferencia total en los valores de una lista usando reduce().
def diferencia_total(numeros):
    return reduce(lambda x, y: x - y, numeros)

print(diferencia_total([100, 20, 10]))

# 25. Función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

print(contar_caracteres("Python"))

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda x, y: x % y

print(resto_division(10, 3))

# 27. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

print(calcular_promedio([10, 20, 30, 40]))

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def buscar_primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

print(buscar_primer_duplicado([1, 2, 3, 2, 4, 1]))

# 29. Crea una función que convierta una variable en texto y enmascare con '#' excepto los últimos cuatro.
def enmascarar_cadena(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]

print(enmascarar_cadena("123456789"))

# 30. Crea una función que determine si dos palabras son anagramas.
def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(es_anagrama("Raza", "Zara"))

# 31. Crea una función que busque un nombre en una lista ingresada por el usuario o lance una excepción.
def buscar_nombre_usuario():
    try:
        nombres = input("Ingresa nombres separados por comas: ").split(",")
        nombres = [n.strip() for n in nombres]
        busqueda = input("¿Qué nombre buscas?: ").strip()
        
        if busqueda in nombres:
            print(f"'{busqueda}' fue encontrado en la lista.")
        else:
            raise Exception(f"El nombre '{busqueda}' no está en la lista.")
    except Exception as e:
        print(e)

# buscar_nombre_usuario() # Descomentar para probar

# 32. Crea una función que busque un nombre completo en una lista de empleados y devuelva su puesto.
def buscar_puesto_empleado(nombre_completo, empleados):
    # empleados es una lista de diccionarios con {'nombre': '...', 'puesto': '...'}
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre_completo.lower():
            return empleado['puesto']
    return "Esta persona no trabaja aquí."

lista_empleados = [
    {"nombre": "Adam Perez", "puesto": "Analista de Datos"},
    {"nombre": "Lucia Fernandez", "puesto": "Desarrolladora Python"}
]
print(buscar_puesto_empleado("Adam Perez", lista_empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

print(sumar_listas([1, 2, 3], [4, 5, 6]))

# 34. Clase Arbol: Manipulación de estructura mediante métodos.
class Arbol:
    def __init__(self):
        # 1. Inicializar tronco con longitud 1 y ramas vacías.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar longitud del tronco en una unidad.
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar nueva rama de longitud 1.
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en una unidad la longitud de todas las ramas.
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar rama en una posición específica (índice).
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        # 6. Información del tronco, número de ramas y sus longitudes.
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }

#Algunso ejemplos que podemosdarle de uso
mi_arbol = Arbol()             
mi_arbol.crecer_tronco()        
mi_arbol.nueva_rama()           
mi_arbol.crecer_ramas()         
mi_arbol.nueva_rama()            
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)          
print(mi_arbol.info_arbol())     


# 36. Clase UsuarioBanco: Representa un usuario con operaciones bancarias.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # 1. Inicializar atributos básicos.
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # 2. Retirar saldo. Lanza error si no hay suficiente o es inválido.
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad

    def agregar_dinero(self, cantidad):
        # 4. Agregar dinero al saldo.
        self.saldo += cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # 3. Transferencia desde 'otro_usuario' al actual.
        try:
            otro_usuario.retirar_dinero(cantidad)
            self.agregar_dinero(cantidad)
        except ValueError as e:
            print(f"Transferencia fallida: {e}")

# vamos a srear usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

#Otras opciones
bob.agregar_dinero(20)           
alicia.transferir_dinero(bob, 80) 
alicia.retirar_dinero(50)        

print(f"Saldo Alicia: {alicia.saldo}")
print(f"Saldo Bob: {bob.saldo}")

# 37. Función procesar_texto que utiliza funciones auxiliares según la opción.

def contar_palabras(texto):
    # Cuenta la frecuencia de cada palabra y devuelve un diccionario.
    palabras = texto.lower().split()
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Reemplaza todas las ocurrencias de una palabra por otra.
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    # Elimina una palabra específica del texto.
    palabras = texto.split()
    resultado = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(resultado)

def procesar_texto(texto, opcion, *args):
    # Función principal que deriva el trabajo según la opción elegida.
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"

#Ejemplo
texto_ejemplo = "hola mundo hola python"
print(procesar_texto(texto_ejemplo, "contar"))
print(procesar_texto(texto_ejemplo, "reemplazar", "hola", "saludos"))
print(procesar_texto(texto_ejemplo, "eliminar", "mundo"))


# 38. Programa que determina si es de noche, día o tarde según la hora.
def determinar_momento_dia(hora):
    if 6 <= hora < 13:
        return "Es de día (mañana)"
    elif 13 <= hora < 20:
        return "Es tarde"
    elif (20 <= hora <= 24) or (0 <= hora < 6):
        return "Es de noche"
    else:
        return "Hora no válida"

print(determinar_momento_dia(14))


# 39. Determinar calificación de texto basada en nota numérica.
def obtener_calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota fuera de rango"

print(obtener_calificacion_texto(85))


# 40. Función para calcular el área de diferentes figuras geométricas.
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        # datos = (base, altura)
        return datos[0] * datos[1]
    elif figura == "circulo":
        # datos = (radio,)
        return math.pi * (datos[0] ** 2)
    elif figura == "triangulo":
        # datos = (base, altura)
        return (datos[0] * datos[1]) / 2
    else:
        return "Figura no reconocida"

print(f"Área rectángulo: {calcular_area('rectangulo', (10, 5))}")
print(f"Área círculo: {calcular_area('circulo', (3,))}")


# 41. Programa de cálculo de monto final con cupón de descuento.
def calcular_monto_compra():
    try:
        precio_original = float(input("Ingresa el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()
        
        precio_final = precio_original
        
        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Ingresa el valor del cupón de descuento: "))
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                # Evitamos que el precio sea negativo
                if precio_final < 0: precio_final = 0
                print(f"Descuento de {valor_cupon}€ aplicado.")
            else:
                print("Cupón no válido (debe ser mayor a cero).")
        
        print(f"El precio final de la compra es: {precio_final}€")
        
    except ValueError:
        print("Error: Por favor, ingresa valores numéricos válidos.")


# ==========================================
# Programa: Cálculo de Promedio de Notas
# Asignatura: Arquitectura y Sistemas Operativos
# Carrera: Tecnicatura Universitaria en Programación (UTN)
# ==========================================

# 1. Se define la cantidad de notas y se inicializa una lista vacía para almacenarlas
CANTIDAD_NOTAS = 3
notas = []

print('========================')
print('CALCULADORA DE PROMEDIOS')
print('========================')
print(f'Ingrese las {CANTIDAD_NOTAS} notas (del 0.0 al 10.0).')
# 2. Se utiliza un ciclo for para solicitar las notas al usuario
for i in range(CANTIDAD_NOTAS):
    # Se utiliza un bucle y un bloque try-except para repetir el proceso hasta obtener un valor válido
    while True:
        try:
            # Se solicita el dato por consola y se convierte el string a float
            print('------------------------')
            entrada = input(f'Nota {i + 1}: ')
            nota_actual = float(entrada.replace(',','.'))
            # Si la nota está fuera de rango, se vuelve a pedir la nota
            if not (0 <= nota_actual <= 10):
                print('Error: Valor fuera de rango (del 0.0 al 10.0).')
                continue
            # En caso contrario se finaliza el bucle
            break
        # Si hubo error de conversion, se muestra un mensaje por pantalla
        except ValueError:
            print('Error: Debe ingresar un número válido.')

    # Se agrega la nota ingresada a la lista utilizando el método append
    notas.append(nota_actual)

# 3. Se realiza el cálculo aritmético
suma_total = sum(notas)
promedio = suma_total / len(notas)

# 4. Se muestra el resultado en pantalla
print('========================')
print('RESULTADOS')
print('========================')
print(f'Notas registradas: {notas}')
print(f'Promedio final: {promedio:.2f}')
print('========================')
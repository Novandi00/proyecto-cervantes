# Valentín Cáceres
# Lautaro Cardozo
# Javier Soria
# Parcial de Introducción a la Programación
# Juego: Adiviná el número

import random

print("=== ADIVINÁ EL NÚMERO ===")

# Datos iniciales
nombre = input("Ingresá tu nombre: ").strip()
nombre_formateado = nombre.title()

intentos_totales = int(input("¿Cuántos intentos querés tener?: "))

# Configuración del juego
numero_secreto = random.randint(1, 100)
dificultad = "Media"

# datos de la partida
datos_partida = (nombre_formateado, intentos_totales, dificultad)

# Acá vamos guardando los números que prueba el jugador
historial_intentos = []

# Resultado que se completa al terminar
resultado_final = {
    "jugador": nombre_formateado,
    "resultado": "",
    "puntaje": 0
}

# Variables
puntaje = 0
aciertos = 0
gano = False
numero_valido = True

# Bonificación del puntaje
bonificacion = 1.5

print(f"\n¡Hola, {nombre_formateado.upper()}!")
print(f"Pensé un número entre 1 y 100. Tenés {intentos_totales} intentos.")
print(f"Tu nombre tiene {len(nombre_formateado)} caracteres.")

# Comienza el juego
for intento in range(1, intentos_totales + 1):

    try:
        numero = int(input(f"\nIntento {intento}/{intentos_totales} → Ingresá un número: ").strip())
    except ValueError:
        print("Entrada inválida. Debés ingresar un número entero.")
        numero_valido = False
        continue

    numero_valido = True
    historial_intentos.append(numero)

    # Comprobamos si acertó
    if numero == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        aciertos += 1
        gano = True

        # Calculamos el puntaje
        puntos_base = 100 - (intento - 1) * 10
        puntaje = int(puntos_base * bonificacion)
        break

    # Damos una pista
    elif numero < numero_secreto:
        print("El número secreto es MÁS ALTO.")
    else:
        print("El número secreto es MÁS BAJO.")

    # Revisa que el número esté dentro del rango
    if numero < 1 or numero > 100:
        print("Aviso: el número debería estar entre 1 y 100.")

    # Se Actualiza el puntaje
    puntaje = max(0, puntaje + 5)

    intentos_restantes = intentos_totales - intento
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Puntaje acumulado: {puntaje}")

# Mostramos el resultado final
intentos_usados = len(historial_intentos)
intentos_restantes = max(0, intentos_totales - intentos_usados)

if gano:
    resultado_final["resultado"] = "Ganó"
    resultado_final["puntaje"] = puntaje
else:
    resultado_final["resultado"] = "Perdió"
    resultado_final["puntaje"] = puntaje
    print(f"\nNo lograste adivinarlo. El número secreto era {numero_secreto}.")

# Variables booleanas
le_quedaban_intentos = intentos_restantes > 0
supera_puntaje_minimo = puntaje > 50

# Preguntamos si quiere ver todos los datos
respuesta = input("\n¿Querés ver el resumen completo? (SI/NO): ").strip().lower()

if respuesta == "si":
    print("\n=== RESULTADO DE LA PARTIDA ===")
    print(f"Jugador: {nombre_formateado}")
    print(f"Intentos usados: {intentos_usados}")
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"¿Ganó el jugador? {gano}")
    print(f"¿Le quedaban intentos? {le_quedaban_intentos}")
    print(f"¿Superó 50 puntos? {supera_puntaje_minimo}")
    print(f"Historial de intentos: {historial_intentos}")
    print(f"Datos de la partida: {datos_partida}")
    print(f"Resultado final: {resultado_final}")

    # Comprueba el resultado
    if "Ganó" in resultado_final["resultado"]:
        print("¡Felicitaciones por la partida!")

else:
    print("Resumen final omitido.")

print("\n=== FIN DEL JUEGO ===")
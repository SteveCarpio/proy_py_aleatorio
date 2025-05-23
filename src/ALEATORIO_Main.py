"""
Programa de Selección de Números Aleatorios

Este script genera simulaciones para agrupar números hasta alcanzar un importe fijado.
Valores de entrada como: 
- Importe máximo a alcanzar
- Número de simulaciones
- Diferencias mínimas esperadas

Desarrollado en Python con NumPy y Pandas para cálculos y análisis de datos.

Autor: SteveCarpio
"""

from   cfg.ALEATORIO_librerias import *
from   aleatorio.ALEATORIO_paso0     import sTv_paso0
from   aleatorio.ALEATORIO_paso1     import sTv_paso1
from   aleatorio.ALEATORIO_paso2     import sTv_paso2
from   aleatorio.ALEATORIO_paso3     import sTv_paso3
from   aleatorio.ALEATORIO_paso4     import sTv_paso4

# Inicializar colorama
init(autoreset=True)

# Fijamos el file de entrada
os.system("cls") 
print(Fore.MAGENTA + f'------------- [ Introducir el File de Entrada ]------------- \n')
v1 = input(Fore.WHITE + f"Indique el Tipo de File de Entrada (TXT=1 EXCEL=2)")
v2 = input(Fore.WHITE + f"Indique el Nombre del File Entrada (sin extensión)")

# Evaluamos Tipo File de Entrada 1 o 2
if (v1 != "1") and (v1 != "2"):
    print(f"El valor para la extensión debe ser 1 o 2 y no: {v1}")
    sys.exit(0)
if v1 == "1":
    v11 = "txt"
if v1 == "2":
    v11 = "xlsx"

# Evaluamos 
nombre_Entrada   = f"{v2}"
nombre_Salida = nombre_Entrada 

# Valores de entrada por defecto
importe_Fijado   = 600000000     # Máximo importe total acumulado
num_Simulaciones = 1000          # Número de Simulaciones 
diferencia_Menor = 20            # Es el valor más bajo para crear los Excel
diferencia_Stop  = 0.5           # Es el valor más deseable, hará un stop del proceso

# PASO 0: Solicitar Nuevos Valores de entrada
importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop = sTv_paso0(importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop)

def option_0():
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida, v1)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 3: Ejecutamos la selección Aleatoria modelo con Numpy
    sTv_paso3(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)
    
    # PASO 4: Ejecutamos la selección Aleatoria modelo con Pandas
    sTv_paso4(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_1():
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida, v1)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 3: Ejecutamos la selección Aleatoria modelo con Numpy
    sTv_paso3(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_2():
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida, v1)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 4: Ejecutamos la selección Aleatoria modelo con Pandas
    sTv_paso4(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_3():
    global importe_Fijado
    global num_Simulaciones
    global diferencia_Menor
    global diferencia_Stop
    importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop = sTv_paso0(importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop)

def option_Help():
    print(Fore.MAGENTA + "------------- [ Proceso de Selección de Números Aleatorios ] -------------  \n")
    print(Fore.YELLOW + "Valores de Ejecución: \n")
    print(Fore.CYAN + "- Importe Fijado: " + Fore.WHITE + "Es el importe máximo que podrá agrupar el modelo.")
    print(Fore.CYAN + "- Num Simulaciones: "  + Fore.WHITE + "Es la cantidad de veces que el modelo generará simulaciones para alcanzar el importe fijado.")
    print(Fore.CYAN + "- Diferencia Menor: "  + Fore.WHITE + "Es el valor mínimo esperado que puede devolver el modelo.")
    print(Fore.CYAN + "- Diferencia Stop: "  + Fore.WHITE + "Es el valor más bajo permitido que utilizará el modelo como límite.\n")
    print(Fore.YELLOW + "Nota Técnica: \n")
    print("Este programa está desarrollado en Python, utilizando dos librerías muy potentes: NumPy y Pandas, ampliamente usadas en investigación y ciencia de datos.")
    print("Ambas librerías permiten ejecutar modelos matemáticos para encontrar soluciones mediante la selección de números aleatorios, siendo NumPy especialmente eficiente por su uso de matrices.\n")
    print(Fore.CYAN + "- NumPy: " + Fore.WHITE + "Librería de Python para trabajar con arrays y realizar cálculos numéricos de forma rápida.")
    print(Fore.CYAN + "- Pandas: " + Fore.WHITE + "Librería para manipular y analizar datos estructurados, como si fueran hojas de cálculo.\n")
    print(Fore.YELLOW + "Más info: \n")
    print(Fore.CYAN + "- Python: " + Fore.WHITE + "https://es.wikipedia.org/wiki/Python")
    print(Fore.CYAN + "- NumPy: " + Fore.WHITE + "https://es.wikipedia.org/wiki/NumPy")
    print(Fore.CYAN + "- Pandas: " + Fore.WHITE + "https://es.wikipedia.org/wiki/Pandas_(software) \n")
    print(Fore.YELLOW + " \n")
    print("Si necesita más ayuda consultar con " + Fore.RED + "SteveCarpio" + Fore.WHITE + " - " + Fore.GREEN + "Python-v1.2025")

# Función para limpiar la pantalla (en sistemas basados en UNIX)
def limpiar_pantalla():
    os.system("cls")  

# Menú interactivo
def mostrar_menu():
    limpiar_pantalla()
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE + "        🖥️   MENÚ PRINCIPAL 🖥️")
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.CYAN + "- File de Entrada:  " + str(nombre_Entrada) + "." + str(v11))
    print(Fore.CYAN + "- Importe Fijado:   " + str(importe_Fijado))
    print(Fore.CYAN + "- Núm Simulaciones: " + str(num_Simulaciones))
    print(Fore.CYAN + "- Diferencia Menor: " + str(diferencia_Menor))
    print(Fore.CYAN + "- Diferencia Stop:  " + str(diferencia_Stop))
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE   + "0) ⚪ Ejecutar Modelo Numpy y Pandas")
    print(Fore.YELLOW  + "1) 🟡 Ejecutar Modelo Numpy ")
    print(Fore.YELLOW  + "2) 🟡 Ejecutar Modelo Pandas")
    print(Fore.CYAN  + "3) 🟡 Modificar Valores     ")
    print(Fore.MAGENTA + "?) 🟣 Ayuda                 ")
    print(Fore.RED     + "x) ❌ Salir del programa   " + Fore.WHITE + "    (.v3)")
    print(Fore.MAGENTA + "=" * 37)

# Función principal para gestionar el menú
def ejecutar_menu():
    while True:
        mostrar_menu()
        option = input(Fore.WHITE + "Selecciona una opción: ")
        limpiar_pantalla()
        if option   == '0':
            option_0()
        elif option == '1':
            option_1()
        elif option == '2':
            option_2()
        elif option == '3':
            option_3()            
        elif option == '?':
            option_Help()
        elif option.upper() == 'X':
            print(Fore.RED + "\n¡Saliendo del programa! \n")
            break
        else:
            print(Fore.RED + "\n ❌ Opción no válida, por favor elige una opción válida ❌\n")
        
        # Pausa para que el usuario vea los resultados
        input(Fore.MAGENTA + f'\n------------- [ Pulse una tecla para volver al menú - {dt.now()} ] -------------')

ejecutar_menu()


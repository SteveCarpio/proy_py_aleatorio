from   cfg.ALEATORIO_librerias import *
from   aleatorio.ALEATORIO_paso0     import sTv_paso0
from   aleatorio.ALEATORIO_paso1     import sTv_paso1
from   aleatorio.ALEATORIO_paso2     import sTv_paso2
from   aleatorio.ALEATORIO_paso3     import sTv_paso3
from   aleatorio.ALEATORIO_paso4     import sTv_paso4

# Inicializar colorama
init(autoreset=True)

# Valores por defecto
importe_Fijado   = 600000000     # Máximo importe total acumulado
num_Simulaciones = 5000          # Número de Simulaciones 
diferencia_Menor = 10            # Es el valor más bajo para crear los Excel
diferencia_Stop  = 0.5           # Es el valor más deseable, hará un stop del proceso

# Solicitar datos de entrada
v1 = input(Fore.WHITE + "Indique el Tipo de File de Entrada (CSV=1 EXCEL=2)")
v2 = input(Fore.WHITE + "Indique el Nombre del File Entrada (sin extensión)")
v3 = input(Fore.WHITE + "Indique el Importe Fijado:         (600.000.000  )")
v4 = input(Fore.WHITE + "Indique el Número de Simulaciones: (5000         )")
v5 = input(Fore.WHITE + "Indique la Diferencia Menor:       (10           )")
v6 = input(Fore.WHITE + "Indique la Diferencia Stop:        (0.5          )")

print(f'------------- [ Inicio - {dt.now()} ]------------- \n')
# Evaluamos el Importe Fijado.
try:
    v3_int = int(v3)
except ValueError:
    print(f"Importe Fijado: {importe_Fijado}")
else:
    print(f"Importe Fijado: {v3} - nuevo")
    importe_Fijado = int(v3)

# Evaluamos Número de Simulaciones
try:
    v4_int = int(v4)
except ValueError:
    print(f"Número Simulaciones: {num_Simulaciones}")
else:
    print(f"Número de Simulaciones: {v4} - nuevo")
    num_Simulaciones = int(v4)

# Evaluamos la Diferencia menor
try:
    v5_int = int(v5)
except ValueError:
    print(f"Diferencia Menor: {diferencia_Menor}")
else:
    print(f"Diferencia Menor: {v5} - nuevo")
    diferencia_Menor = int(v5)

# Evaluamos el Diferencia Stop
try:
    v6_int = int(v6)  # Intenta convertir a entero
    print(f"Diferencia Menor: {v6_int} - nuevo")
    diferencia_Stop = int(v6)
except ValueError:
    try:
        v6_float = float(v6)  # Si no es entero, intenta convertir a flotante
        print(f"Diferencia Menor: {v6_float} - nuevo")
        diferencia_Stop = float(v6)
    except ValueError:
        print(f"Diferencia Stop: {diferencia_Stop}")



# Evaluamos 
nombre_Entrada   = f"A_OK_20241209"
nombre_Salida    = f"{nombre_Entrada}" 

x = input(Fore.WHITE + "\n\nPulse una tecla para continuar.......")


# PASO 0: Verificar datos de entrada
#os.system("cls") 
sTv_paso0()

def option_0():
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 3: Ejecutamos la selección Aleatoria modelo con Numpy
    sTv_paso3(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)
    
    # PASO 4: Ejecutamos la selección Aleatoria modelo con Pandas
    sTv_paso4(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_1():
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 3: Ejecutamos la selección Aleatoria modelo con Numpy
    sTv_paso3(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_2():    
    # PASO 1: Importamos el txt con los prestamos a un DataFrame
    df1 = sTv_paso1(nombre_Entrada, nombre_Salida)

    # PASO 2: Elimino ID prestamos que tenemos en un excel
    df2 = sTv_paso2(df1)

    # PASO 4: Ejecutamos la selección Aleatoria modelo con Pandas
    sTv_paso4(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

def option_Help():
    print("ayuda")

# Función para limpiar la pantalla (en sistemas basados en UNIX)
def limpiar_pantalla():
    os.system("cls")  

# Menú interactivo
def mostrar_menu():
    limpiar_pantalla()
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE + "      Lanzar Modelo Aleatorios ")
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE + "        🖥️   MENÚ PRINCIPAL 🖥️")
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE   + "0) ⚪ Ejecutar Modelos Numpy y Pandas")
    print("")
    print(Fore.YELLOW  + "1) 🟡 Ejecutar Modelo Numpy")
    print(Fore.YELLOW  + "2) 🟡 Ejecutar Modelo Pandas")
    print("")
    print(Fore.MAGENTA + "?) 🟣 Ayuda                      ")
    print(Fore.RED     + "x) ❌ Salir del programa   " + Fore.WHITE + "    (.v3)")
    print(Fore.MAGENTA + "=" * 37)

# Función principal para gestionar el menú
def ejecutar_menu():
    while True:
        mostrar_menu()
        option = input(Fore.WHITE + "Selecciona una opción: ")

        if option   == '0':
            option_0()
        elif option == '1':
            option_1()
        elif option == '2':
            option_2()
        elif option == '?':
            option_Help()
        elif option.upper() == 'X':
            print(Fore.RED + "\n¡Saliendo del programa! \n")
            break
        else:
            print(Fore.RED + "\n ❌ Opción no válida, por favor elige una opción válida ❌\n")
        
        # Pausa para que el usuario vea los resultados
        input(Fore.WHITE + "\nProceso Finalizado, presione una techa para volver al Menú...")


#input(Fore.WHITE + "Presiona Enter para continuar...")
ejecutar_menu()



print(f'\n-------------[ Fin - {dt.now()} ]-------------')
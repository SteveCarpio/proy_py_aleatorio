from   cfg.ALEATORIO_librerias import *
from   aleatorio.ALEATORIO_paso0     import sTv_paso0
from   aleatorio.ALEATORIO_paso1     import sTv_paso1
from   aleatorio.ALEATORIO_paso2     import sTv_paso2
from   aleatorio.ALEATORIO_paso3     import sTv_paso3
from   aleatorio.ALEATORIO_paso4     import sTv_paso4

# Inicializar colorama
init(autoreset=True)

print(f'------------- [ Inicio - {dt.now()} ]------------- \n')
importe_Fijado   = 600000000      # Máximo importe total acumulado
num_Simulaciones = 1000          # Número de Simulaciones 
diferencia_Menor = 200             # Es el valor más bajo para crear los Excel
diferencia_Stop  = 0.5            # Es el valor más deseable, hará un stop del proceso
nombre_Entrada   = f"A_OK_20241209"
nombre_Salida    = f"{nombre_Entrada}" 

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


input(Fore.WHITE + "Presiona Enter para continuar...")
ejecutar_menu()



print(f'\n-------------[ Fin - {dt.now()} ]-------------')
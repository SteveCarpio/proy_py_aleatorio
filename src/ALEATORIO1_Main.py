from   cfg.ALEATORIO_librerias import *
from   aleatorio.ALEATORIO_paso0     import sTv_paso0
from   aleatorio.ALEATORIO_paso1     import sTv_paso1
from   aleatorio.ALEATORIO_paso2     import sTv_paso2
from   aleatorio.ALEATORIO_paso3     import sTv_paso3

print(f'------------- [ Inicio - {dt.now()} ]------------- \n')
importe_Fijado   = 600000000      # Máximo importe total acumulado
num_Simulaciones = 1000          # Número de Simulaciones 
diferencia_Menor = 20             # Es el valor más bajo para crear los Excel
diferencia_Stop  = 0.5            # Es el valor más deseable, hará un stop del proceso
nombre_Entrada   = f"A_OK_20241209"
nombre_Salida    = f"{nombre_Entrada}" 

# PASO 0: Verificar datos de entrada
sTv_paso0()

# PASO 1: Importamos el txt con los prestamos a un DataFrame
df1 = sTv_paso1(nombre_Entrada)   

# PASO 2: Elimino ID prestamos que tenemos en un excel
df2 = sTv_paso2(df1)

# PASO 3: Ejecutamos la selección Aleatoria
sTv_paso3(df2, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida)

print(f'-------------[ Fin - {dt.now()} ]-------------')
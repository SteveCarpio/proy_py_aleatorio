### Creado por: SteveCarpio-2024 ###
import pandas as pd
from datetime import datetime as dt

#### -----------------------------------------------------------------------------
print(f'{dt.now()}\n')
importe_fijado   = 600000000   # Máximo importe total acumulado
num_Simulaciones = 10000          # Número de Simulaciones 
diferencia_menor = 10           # Es el valor más bajo para crear los Excel
diferencia_stop  = 0.1         # Es el valor más desable, hará un stop del proceso 
nombre_Entrada   = f"A_OK_20241209"
nombre_Salida    = f"{nombre_Entrada}" 
#### -----------------------------------------------------------------------------

# --- Funcion que ejecuta un algoritmo y crea un DataFrame con los registos Aleatorios
def PROC_Crea_Seleccion_Aleatoria(df):
    # Baraja el DataFrame
    df = df.sample(frac=1)
    # Defino Listas y variables
    seleccionados = []
    suma = 0
    # Selección aleatoria de registros
    for index, row in df.iterrows():
        valor = row['TOTAL']  # stv: round() int()  el resultado luego es fixticio
        if valor != 0:
            if suma + valor <= importe_fijado:
                seleccionados.append(row)
                suma += valor
            if suma >= importe_fijado:
                break
    # Crea el nuevo DataFrame con los valores aleatorios
    resultados_df = pd.DataFrame(seleccionados)
    return resultados_df.reset_index(drop=True), suma


### --------------------------------- INICIO --------------------------------- ###

# Importar Excel de Fondos en un DataFrame
df_tmp = pd.read_excel(f"C:\\MisCompilados\\PRO_SABADELL_RANDOM\\{nombre_Entrada}.xlsx")

### Lanzar N Simulaciones 
for i in range(1,num_Simulaciones+1):
    #print(f"-------------- Simulacion Número: {i} -------------------")

    # Llama func, creará un DF con datos aleatorios con el importe fijado
    df_Resultado, suma=PROC_Crea_Seleccion_Aleatoria(df_tmp)

    # Exporto resultado con los valores de Salida en un CSV
    if importe_fijado - suma < diferencia_menor:
        df_Resultado.to_excel(f'C:\\MisCompilados\\PRO_SABADELL_RANDOM\\{nombre_Salida}_Sim{i}_DIF_{importe_fijado-suma}.xlsx',index=False)

        # Mostrar resultados
        print(f"-------------- Simulacion Número: {i} -------------------")
        print(f'Num Reg TEntrada: {len(df_tmp)}')
        print(f'Num Reg TSalida : {len(df_Resultado)}')
        print(f'Importe Fijado  : {importe_fijado} ')
        print(f'Importe Más Bajo: {suma}')
        print(f'Diferencia Simul: {importe_fijado - suma}\n')
    
    # Detener el bucle si la DIF es igual a CERO
    if importe_fijado - suma < diferencia_stop:
        print(f"----------------------------------------------------------------------------------")
        print(f"-------- ¡¡¡ Enhorabuena se encontró el valor más bajo en el Nº: {i} !!! ---------")
        print(f"----------------------------------------------------------------------------------")
        break

print(f'\n{dt.now()}\n')
### Creado por: SteveCarpio-2024 ###
import pandas as pd
import numpy as np
import chardet

from datetime import datetime as dt


#### -----------------------------------------------------------------------------
print(f'------------- [ Inicio - {dt.now()} ]------------- \n')
importe_Fijado   = 600000000      # Máximo importe total acumulado
num_Simulaciones = 20000           # Número de Simulaciones 
diferencia_Menor = 10             # Es el valor más bajo para crear los Excel
diferencia_Stop  = 1              # Es el valor más desable, hará un stop del proceso
ruta_Raiz        = f'C:\\MisCompilados\\PRO_SABADELL_RANDOM\\'
nombre_Entrada   = f"A_OK_20241209"
nombre_Salida    = f"{nombre_Entrada}" 
#### -----------------------------------------------------------------------------

def PROC_Ver_Tamano_Objetos(nombre,objeto,opcion):
    # Tamaño en memoria del DataFrame en bytes
    if opcion == 1:
        tamaño_df_bytes = objeto.memory_usage(deep=True).sum()
        tamaño_df_mb = tamaño_df_bytes / (1024 * 1024)  # Convertir a MB
        #print(f'Tamaño en memoria del DataFrame ({nombre}): {tamaño_df_mb:.2f} MB')
    # Tamaño en memoria del array en bytes
    if opcion == 2:
        tamaño_array_bytes = objeto.nbytes
        tamaño_array_mb = tamaño_array_bytes / (1024 * 1024)  # Convertir a MB
        #print(f'Tamaño en memoria del array ({nombre}): {tamaño_array_mb:.2f} MB')

# --- Funcion que ejecuta un algoritmo y crea un Array.Numpy con los reg Aleatorios
def PROC_Crea_Seleccion_Aleatoria3(ar):

    # Baraja el array de NumPy
    np.random.shuffle(ar)
    # Crea un Array.Numpy vacio con la longitud de 'ar'
    seleccionados = np.empty((len(ar), ar.shape[1]))
    suma = 0
    count = 0
    # Selección aleatoria de registros
    for row in ar:
        valor = row[1]  # Se asume que la segunda columna corresponde a 'TOTAL'
        if valor != 0:
            if suma + valor <= importe_Fijado:
                seleccionados[count] = row
                suma += valor
                count += 1
            if suma >= importe_Fijado:
                break
    # Redimenciona el array solo con los filas incluidas
    seleccionados = seleccionados[:count]
    # Devolvemos el Array.Numpy y la Suma acumulada
    del ar
    # Retornamos el resultado
    return seleccionados, suma 

# --- Funcion que nos sirve para importar el fichero de entrada .txt
def PROC_Importa_txt():
    
    # Inicializar listas vacías para cada campo
    campo1_list = []
    campo2_list = []
    campo3_list = []

    # Detectar la codificación del archivo
    with open(f"{ruta_Raiz}FILE_IN\\{nombre_Entrada}.txt", 'rb') as file:  # Abrir el archivo en modo binario para detectar la codificación
        raw_data = file.read(1000)     # Leer solo los primeros 1000 bytes
        result = chardet.detect(raw_data)
        encoding = result['encoding']  # utf-8, ansi, ascii, etc....

    # Abrir el archivo y leer línea por línea
    with open(f"{ruta_Raiz}FILE_IN\\{nombre_Entrada}.txt", "r", encoding=encoding, errors='replace') as file:  # utf-8

        for line in file:
            # Campo1 "NUMPRES" en la posición 8, ancho 15
            campo1 = line[7:22].strip()  # Índices 7:22 para los 15 caracteres
            campo1_list.append(campo1)
            
            # Campo2 "IMPINICIAL" en la posición 31, ancho 15 (formato doble con signo, 13 enteros, 2 decimales)
            campo2 = float(line[30:45].strip())  # Convertimos a tipo flotante
            campo2_list.append(campo2)
            
            # Campo3 "PD" en la posición 645, ancho 5 (formato doble, 3 enteros, 2 decimales)
            #campo3 = float(line[644:649].strip())  # Convertimos a tipo flotante
            #campo3_list.append(campo3)

    # Crear el DataFrame con los campos extraídos
    df = pd.DataFrame({
        'ID': campo1_list,
        'TOTAL': campo2_list #,
        #'PD': campo3_list
    })

    # Mostrar el DataFrame
    print(f"Importación del Fichero : {nombre_Entrada}.txt \nEncoding : {encoding}\n")
    return df

# --- Funcion que nos quita los prestamos que no queremos a partor de un excel
def PROC_Quita_Prestamo(df1):

    # Leemos el excel de PRESTAMOS a eliminar
    df2= pd.read_excel(f'{ruta_Raiz}CONFIG\\QUITAR_PRESTAMOS.xlsx')
    
    # Quitamos los "0" de la varable ID
    df1['ID'] = df1['ID'].astype(str)       # Convertir 'ID' de DF1 a tipo str
    df1['ID'] = df1['ID'].str.lstrip('0')   # Eliminar ceros a la izquierda de la columna 'ID'
    df2['ID'] = df2['ID'].astype(str)       # Convertir 'ID' de DF2 a tipo str
    df2['ID'] = df2['ID'].str.lstrip('0')   # Eliminar ceros a la izquierda de la columna 'ID'
    
    # Realizamos el merge para encontrar los registros comunes
    merged = pd.merge(df1, df2, on='ID', how='inner')

    # Filtrar los registros que están en A pero no en B
    df3 = df1[~df1['ID'].isin(merged['ID'])]
    df3 = df3.reset_index(drop=True)  # Reinicio indices

    print(f"Número de registros de Entrada : {len(df1)}")
    print(f"Prestamos eliminados           : {len(df2)}")
    print(f"Número de registros a Procesar : {len(df3)}\n")
    return df3

### --------------------------------------------------------------------------------------- ###
### ------------------------------------------ INICIO ------------------------------------- ###
### --------------------------------------------------------------------------------------- ###

# Importamos el txt con los prestamos a un DataFrame
df = PROC_Importa_txt()   #df = pd.read_excel(f'{ruta_Raiz}FILE_IN\\{nombre_Entrada}.xlsx')

# Elimino ID prestamos que tenemos en un excel
df_tmp = PROC_Quita_Prestamo(df)

# Exporto el DataFrame a un excel
df_tmp.to_excel(f'{ruta_Raiz}{nombre_Salida}.xlsx', index=False)

# Total del fichero de entrada
var_total = df_tmp['TOTAL'].sum()

# --- Convertir el DataFrame en un Array Numpy
ar_tmp = df_tmp.to_numpy()

# --- Bucle que nos servirá para Lanzar las N Simulaciones 
sw=0
print(f"Procesando ({num_Simulaciones}) simulaciones aleatorias\n")
for i in range(1,num_Simulaciones+1):
    # Llama func, creará un Array.Numpy con datos aleatorios con el importe fijado
    ar_Resultado, suma=PROC_Crea_Seleccion_Aleatoria3(ar_tmp)

    # Exporto resultado con los valores de Salida en un CSV
    if importe_Fijado - suma < diferencia_Menor:
        sw=1
        # Convieto el Array.Numpy en un DataFrame
        df_Resultado = pd.DataFrame(ar_Resultado, columns=['ID', 'TOTAL'])

        # Exporto el DataFrame a un excel
        df_Resultado.to_excel(f'{ruta_Raiz}{nombre_Salida}_Sim{i}_Dif_{importe_Fijado-suma}.xlsx',index=False)

        # Mostrar resultados
        print(f"--------------------- Simulacion Número: {i}")
        print(f'Num Reg TEntrada   : {len(df_tmp)}')
        print(f'Num Reg TSalida    : {len(df_Resultado)}')
        print(f'Importe Total      : {var_total}')
        print(f'Importe Fijado     : {importe_Fijado} ')
        print(f'Importe Conseguido : {suma}')
        print(f'        Diferencia : {importe_Fijado - suma}\n')
    
    # Detener el bucle si la DIF es igual a CERO
    if importe_Fijado - suma < diferencia_Stop:
        print(f"-----------------------------------------------------------------------------------")
        print(f"------ ¡¡¡ Enhorabuena se encontró el valor más bajo en la Simulación {i} !!! -------")
        print(f"-----------------------------------------------------------------------------------\n")
        break

if sw == 0:
    print(f'Importe Total     : {var_total}')  
    print(f'Importe Fijado    : {importe_Fijado}')
    print(f'Diferencia Menor  : {diferencia_Menor}')
    print(f'Diferencia Stop   : {diferencia_Stop}\n')

    print("¡Vaya no se encontró un resultado!\n")

# Invocar función para visualizar en tamaño del Objeto
PROC_Ver_Tamano_Objetos('df_tmp',df_tmp,1)
PROC_Ver_Tamano_Objetos('ar_tmp',ar_tmp,2)
PROC_Ver_Tamano_Objetos('ar_Resultado',ar_Resultado,2)

# Liberar memoria de los objetos
del ar_tmp, ar_Resultado, df_tmp
print(f'-------------[ Fin - {dt.now()} ]-------------')

### ------------------------------------------- FIN -------------------------------------- ###
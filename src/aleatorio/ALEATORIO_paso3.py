from   cfg.ALEATORIO_librerias import *
import cfg.ALEATORIO_variables as sTv

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

# --- Función que ejecuta un algoritmo y crea un Array.Numpy con los reg Aleatorios
def PROC_Crea_Seleccion_Aleatoria3(ar, importe_Fijado):

    # Baraja el array de NumPy
    np.random.shuffle(ar)
    # Crea un Array.Numpy vació con la longitud de 'ar'
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
    # Re dimensiona el array solo con los filas incluidas
    seleccionados = seleccionados[:count]
    # Devolvemos el Array.Numpy y la Suma acumulada
    del ar
    # Retornamos el resultado
    return seleccionados, suma 

def sTv_paso3(df_tmp, num_Simulaciones, importe_Fijado, diferencia_Menor, diferencia_Stop, nombre_Salida ):
    # Exporto el DataFrame a un excel
    df_tmp.to_excel(f'{sTv.var_RutaInforme}{nombre_Salida}.xlsx', index=False)

    # Total del fichero de entrada
    var_total = df_tmp['TOTAL'].sum()

    # --- Convertir el DataFrame en un Array Numpy
    ar_tmp = df_tmp.to_numpy()

    # --- Bucle que nos servirá para Lanzar las N Simulaciones 
    sw=0
    print(f"Procesando ({num_Simulaciones}) simulaciones aleatorias\n")
    for i in range(1,num_Simulaciones+1):
        # Llama func, creará un Array.Numpy con datos aleatorios con el importe fijado
        ar_Resultado, suma=PROC_Crea_Seleccion_Aleatoria3(ar_tmp, importe_Fijado)

        # Exporto resultado con los valores de Salida en un CSV
        if importe_Fijado - suma < diferencia_Menor:
            sw=1
            # Convierto el Array.Numpy en un DataFrame
            df_Resultado = pd.DataFrame(ar_Resultado, columns=['ID', 'TOTAL'])

            # Exporto el DataFrame a un excel
            df_Resultado.to_excel(f'{sTv.var_RutaInforme}{nombre_Salida}_Sim{i}_Dif_{importe_Fijado-suma}.xlsx',index=False)

            # Mostrar resultados
            print(f"--------------------- Simulación Número: {i}")
            print(f'Num Reg TEntrada   : {len(df_tmp)}')
            print(f'Num Reg TSalida    : {len(df_Resultado)}')
            print(f'Importe Total      : {var_total}')
            print(f'Importe Fijado     : {importe_Fijado} ')
            print(f'Importe Conseguido : {suma}')
            print(f'        Diferencia : {importe_Fijado - suma}\n')
        
        # Detener el bucle si la DIF es igual a CERO
        if importe_Fijado - suma < diferencia_Stop:
            print(f"---------------------------------------------------------------------------------")
            print(f"------ Enhorabuena se encontró el valor más bajo en la Simulación {i} !!! -------")
            print(f"-------------------------------------------------------------------------------\n")
            break

    if sw == 0:
        print(f'Importe Total     : {var_total}')  
        print(f'Importe Fijado    : {importe_Fijado}')
        print(f'Diferencia Menor  : {diferencia_Menor}')
        print(f'Diferencia Stop   : {diferencia_Stop}\n')

        print("Vaya no hubo un resultado!\n")

    # Invocar función para visualizar en tamaño del Objeto
    PROC_Ver_Tamano_Objetos('df_tmp',df_tmp,1)
    PROC_Ver_Tamano_Objetos('ar_tmp',ar_tmp,2)
    PROC_Ver_Tamano_Objetos('ar_Resultado',ar_Resultado,2)

    # Liberar memoria de los objetos
    del ar_tmp, ar_Resultado, df_tmp
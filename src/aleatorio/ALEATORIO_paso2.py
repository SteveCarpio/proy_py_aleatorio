from   cfg.ALEATORIO_librerias import *
import cfg.ALEATORIO_variables as sTv

# --- Función que nos quita los prestamos que no queremos a partir de un excel
def sTv_paso2(df1):

    # Leemos el excel de PRESTAMOS a eliminar
    df2= pd.read_excel(f'{sTv.var_RutaConfig}QUITAR_PRESTAMOS.xlsx')
    
    # Quitamos los "0" de la variable ID
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
from   cfg.ALEATORIO_librerias import *
import cfg.ALEATORIO_variables as sTv

def sTv_paso0(importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop):
    print(f'\n------------- [ Introducir Valores para el modelo ]------------- \n')

    # Solicitar datos de entrada
    #os.system("cls") 
    v3 = input(Fore.WHITE + f"Indique el Importe Fijado:         ({importe_Fijado})")
    v4 = input(Fore.WHITE + f"Indique el Número de Simulaciones: ({num_Simulaciones})")
    v5 = input(Fore.WHITE + f"Indique la Diferencia Menor:       ({diferencia_Menor})")
    v6 = input(Fore.WHITE + f"Indique la Diferencia Stop:        ({diferencia_Stop})")

    # Evaluamos el Importe Fijado.
    try:
        v3_int = int(v3)
    except ValueError:
        print(f"\n***\nImporte Fijado: {importe_Fijado}")
    else:
        print(f"Importe Fijado: {v3} - nuevo valor")
        importe_Fijado = int(v3)

    # Evaluamos Número de Simulaciones
    try:
        v4_int = int(v4)
    except ValueError:
        print(f"Número Simulaciones: {num_Simulaciones}")
    else:
        print(f"Número de Simulaciones: {v4} - nuevo valor")
        num_Simulaciones = int(v4)

    # Evaluamos la Diferencia menor
    try:
        v5_int = int(v5)
    except ValueError:
        print(f"Diferencia Menor: {diferencia_Menor}")
    else:
        print(f"Diferencia Menor: {v5} - nuevo valor")
        diferencia_Menor = int(v5)

    # Evaluamos el Diferencia Stop
    try:
        v6_int = int(v6)  # Intenta convertir a entero
        print(f"Diferencia Menor: {v6_int} - nuevo valor")
        diferencia_Stop = int(v6)
    except ValueError:
        try:
            v6_float = float(v6)  # Si no es entero, intenta convertir a flotante
            print(f"Diferencia Menor: {v6_float} - nuevo valor")
            diferencia_Stop = float(v6)
        except ValueError:
            print(f"Diferencia Stop: {diferencia_Stop}")

    return importe_Fijado, num_Simulaciones, diferencia_Menor, diferencia_Stop
try:
    # Abrimos el fichero en modo lectura
    # Añadimos "r" al principio para indicar que es una ruta y que sirvan las barras invertidas
    rutaFichero = r"D:\Mis documentos\ProyectoA\Python\Ficheros\facturas.txt"
    # Añadimos el argumento mode="r" para indicar que abrimos el archivo en modo lectura
    # Usamos el argumento "encoding" para indicar que el archivo tiene codificación utf-8
    # de forma que si contiene tildes, eñes, etc, las mostrará correctamente
    #fichero = open(rutaFichero, "r", encoding="utf-8")
    # Recorremos cada línea del fichero y la vamos mostrando en consola
    with open("facturas.txt", mode="r") as fichero: 
        for linea in fichero:
            print(linea, end="")
        # Cerramos el fichero
    fichero.close
except Exception as e:
    # Se se produce un error al intentar abrir el fichero, lo capturamos y lo mostramos
    print(f"Se ha producido un error al intentar abrir el fichero: {e}")
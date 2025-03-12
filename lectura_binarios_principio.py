try:
    # Abrimos el fichero en modo lectura
    # Añadimos "r" al principio para indicar que es una ruta y que sirvan las barras invertidas
    rutaFichero = r"D:\Mis documentos\ProyectoA\Python\Ficheros\fichero.pdf"
    # Añadimos el argumento mode="rb" para indicar que abrimos el archivo en modo lectura y de tipo binario
    fichero = open(rutaFichero, mode="rb")
    # Leemos los primeros 200 bytes del fichero y los almacenamos en la variable
    datosBinarios = fichero.read(200)
    # Obtenemos y mostramos el tipo de datos del fichero
    print("Los datos son de tipo: " + str(type(datosBinarios)))
    # Mostramos el contenido completo (en secuencia de datos binarios)
    print("Los 200 primeros bytes del fichero:")
    print(datosBinarios)
    # Cerramos el fichero
    fichero.close
except Exception as e:
    # Se se produce un error al intentar abrir el fichero, lo capturamos y lo mostramos
    print(f"Se ha producido un error al intentar abrir el fichero: {e}")
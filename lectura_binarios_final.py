import os

try:
    # Abrimos el fichero en modo lectura
    # Añadimos "r" al principio para indicar que es una ruta y que sirvan las barras invertidas
    rutaFichero = r"D:\Mis documentos\ProyectoA\Python\Ficheros\fichero.pdf"
    # Abrimos el fichero para lectura en modo binario
    with open(rutaFichero, "rb") as fichero:
        # Posicionamos el cursor en el último byte del fichero
        fichero.seek(0, os.SEEK_END)
        # Obtenemos el tamaño del fichero, que es la posición del cursor actual (el último byte)
        tamano = fichero.tell()
        # Si el tamaño es superior a 200 bytes, posicionamos el cursor 200 bytes antes del final
        if tamano > 200:
            fichero.seek(tamano - 200)
        else:
            # Si el tamaño es inferior a 200 bytes, mostramos los últimos 10 bytes
            fichero.seek(tamano - 10)
        # Mostramos los últimos bytes del fichero
        ultimosBytes = fichero.read()
        print(ultimosBytes)
    # Cerramos el fichero
    fichero.close
except Exception as e:
    # Se se produce un error al intentar abrir el fichero, lo capturamos y lo mostramos
    print(f"Se ha producido un error al intentar abrir el fichero: {e}")
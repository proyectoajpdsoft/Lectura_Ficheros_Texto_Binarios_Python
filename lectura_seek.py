try:
    # Abrimos el fichero facturas.txt en modo lectura
    with open("facturas.txt", mode="r") as fichero: 
        # Mostramos la primera línea (desde el principio del fichero) con readline()
        print(fichero.readline(), end="")
        
        # Cambiamos la posición del cursor a la 22
        # Que es donde se encuentra el importe de la primera línea
        fichero.seek(22)
        # Mostramos la primera línea pero a partir de la nueva posición
        print(fichero.readline(), end="")

        # Cerramos el fichero
        fichero.close()
except Exception as e:
    # Se se produce un error al intentar abrir el fichero, lo capturamos y lo mostramos
    print(f"Se ha producido un error al intentar abrir el fichero: {e}")  
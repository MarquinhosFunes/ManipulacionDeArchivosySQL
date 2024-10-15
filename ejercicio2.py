with open("notas.txt", "w") as archivo:
    archivo.write("Matemáticas: Me gusta hacer sumas y restas.\n")
    archivo.write("Literatura: Disfruto leer diferentes historias.\n")
    archivo.write("Historia: Me fascina aprender sobre la historia.\n")


with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
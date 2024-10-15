with open("mi archivo.txt", "w") as archivo:
    archivo.write("Hola, estoy aprendiendo Python")

with open("mi archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
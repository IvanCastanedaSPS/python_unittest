"Script para el manejo de archivos con extension txt"

# Leer un archivo
def read_file(path):
    with open(path,'r') as document:
        print(document.read())
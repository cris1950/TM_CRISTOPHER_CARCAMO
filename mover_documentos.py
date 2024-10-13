import os
import shutil

# Ruta origen (donde están los archivos .docx)
origen = r'C:\Users\cris\Desktop\docx'

# Ruta destino (el directorio remoto simulado, por ejemplo, una nueva carpeta llamada 'remoto')
destino = r'C:\Users\cris\Desktop\remoto'

# Crear la carpeta de destino si no existe
if not os.path.exists(destino):
    os.makedirs(destino)

# Mover archivos .docx
for archivo in os.listdir(origen):
    if archivo.endswith('.docx'):
        shutil.move(os.path.join(origen, archivo), os.path.join(destino, archivo))

print("Archivos movidos correctamente.")
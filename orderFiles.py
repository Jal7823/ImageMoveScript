import os
import shutil

# Obtener el directorio home del usuario actual
homeDir = os.getenv('HOME')

# Definir las carpetas de origen y destino utilizando el directorio home
downloadFolder = os.path.join(homeDir, "Downloads")
imageFolder = os.path.join(homeDir, "Pictures")

# Cambiar al directorio de descargas
os.chdir(downloadFolder)

# Obtener el nombre de la carpeta actual
folder = os.getcwd().split("/")[-1]

print(f"<============ ARCHIVES IN {folder.upper()} ============>")

# Listar archivos en el directorio actual
fileList = os.listdir()
extensions = {}
toSearch = ['jpg', 'jpeg', 'png']

for i in fileList:
    if "." in i:
        nombre, extension = i.rsplit(".", 1)
        extensions[nombre] = extension
    else:
        extensions[i] = None

print("Detected file extensions:")
print(extensions)

# Crear la carpeta de destino si no existe
if not os.path.exists(imageFolder):
    os.makedirs(imageFolder)

# Mover archivos con extensiones específicas a la carpeta de imágenes
for file in fileList:
    _, extension = os.path.splitext(file)
    extension = extension.lower().replace('.', '')
    
    if extension in toSearch:
        src = os.path.join(downloadFolder, file)
        dest = os.path.join(imageFolder, file)
        
        if os.path.isfile(src):
            shutil.move(src, dest)
            print(f"Moved: {file}")
        else:
            print(f"File not found: {file}")

print('-----END SCRIPT SUCCESSFULLY-----')

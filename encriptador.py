from cryptography.fernet import Fernet

# Genera una clave y la guarda en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Carga la clave desde el archivo
def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        return archivo_clave.read()

# Encripta el archivo
def encriptar_archivo(nombre_archivo):
    clave = cargar_clave()
    f = Fernet(clave)

    with open(nombre_archivo, "rb") as file:
        datos = file.read()

    datos_encriptados = f.encrypt(datos)

    with open(nombre_archivo + ".enc", "wb") as file_encriptado:
        file_encriptado.write(datos_encriptados)

    print(f"Archivo '{nombre_archivo}' encriptado exitosamente.")

# Desencripta el archivo
def desencriptar_archivo(nombre_archivo_encriptado, nombre_archivo_salida):
    clave = cargar_clave()
    f = Fernet(clave)

    with open(nombre_archivo_encriptado, "rb") as file_encriptado:
        datos_encriptados = file_encriptado.read()

    datos_desencriptados = f.decrypt(datos_encriptados)

    with open(nombre_archivo_salida, "wb") as file_salida:
        file_salida.write(datos_desencriptados)

    print(f"Archivo desencriptado como '{nombre_archivo_salida}'.")

# ----------- USO -----------
if __name__ == "__main__":
    # Solo la primera vez, generar la clave
    generar_clave()

    # Encriptar archivo
    encriptar_archivo("documento.txt")  # <- Cambia esto por tu archivo

    # Desencriptar archivo
    desencriptar_archivo("documento.txt.enc", "documento_desencriptado.txt")

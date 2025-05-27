import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# -------- Funciones de lógica --------

def cargar_clave_desde_texto(clave_texto):
    """Codifica la clave si es válida."""
    try:
        return clave_texto.encode()
    except Exception:
        messagebox.showerror("Error", "Clave inválida")
        return None

def encriptar_archivo(ruta_archivo, clave_texto, ventana):
    """Encripta un archivo con clave proporcionada o generada."""
    try:
        existe_clave = False

        if not clave_texto.strip():
            clave = Fernet.generate_key()
            
            # Extraer el nombre base del archivo original sin extensión
            nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]
            nombre_clave = f"{nombre_base}_clave.key"
            
            with open(nombre_clave, "wb") as archivo_clave:
                archivo_clave.write(clave)
            ruta_clave = os.path.abspath(nombre_clave)
            messagebox.showinfo("Clave generada", f"Se generó una clave automáticamente y se guardó en '{nombre_clave}'.")
        else:
            clave = cargar_clave_desde_texto(clave_texto)
            existe_clave = True

        if not clave:
            return

        fernet = Fernet(clave)

        with open(ruta_archivo, "rb") as archivo_entrada:
            datos_originales = archivo_entrada.read()

        datos_encriptados = fernet.encrypt(datos_originales)

        ruta_salida = ruta_archivo + ".enc"
        with open(ruta_salida, "wb") as archivo_salida:
            archivo_salida.write(datos_encriptados)

        if existe_clave:
            estado_programa.set(f"Archivo encriptado en:\n{ruta_salida}")
        else:
            estado_programa.set(
                f"Archivo encriptado en:\n{ruta_salida}\nClave generada en:\n{ruta_clave}"
            )

        ventana.destroy()

    except Exception as error:
        messagebox.showerror("Error", f"No se pudo encriptar:\n{error}")

def desencriptar_archivo(ruta_archivo, clave_texto, ventana):
    """Desencripta un archivo con la clave proporcionada."""
    try:
        fernet = Fernet(clave_texto)

        with open(ruta_archivo, "rb") as archivo_entrada:
            datos_encriptados = archivo_entrada.read()

        datos_desencriptados = fernet.decrypt(datos_encriptados)

        ruta_salida = ruta_archivo.replace(".txt.enc", "") + "_desencriptado.txt"
        with open(ruta_salida, "wb") as archivo_salida:
            archivo_salida.write(datos_desencriptados)

        estado_programa.set(f"Archivo desencriptado:\n{ruta_salida}")
        ventana.destroy()

    except Exception as error:
        messagebox.showerror("Error", f"No se pudo desencriptar:\n{error}")

# -------- Ventanas emergentes --------

def mostrar_ventana_encriptar():
    ventana = tk.Toplevel(root)
    ventana.title("Encriptar Archivo")

    tk.Label(ventana, text="Ruta del archivo:").pack()
    entrada_ruta = tk.Entry(ventana, width=50)
    entrada_ruta.pack()

    tk.Button(
        ventana,
        text="Buscar",
        command=lambda: entrada_ruta.insert(0, filedialog.askopenfilename())
    ).pack()

    tk.Label(ventana, text="Clave (Base64 - 44 caracteres):").pack()
    entrada_clave = tk.Entry(ventana, width=50)
    entrada_clave.pack()

    tk.Button(
        ventana,
        text="Encriptar",
        command=lambda: encriptar_archivo(entrada_ruta.get(), entrada_clave.get(), ventana)
    ).pack(pady=10)

def mostrar_ventana_desencriptar():
    ventana = tk.Toplevel(root)
    ventana.title("Desencriptar Archivo")

    tk.Label(ventana, text="Ruta del archivo encriptado:").pack()
    entrada_ruta = tk.Entry(ventana, width=50)
    entrada_ruta.pack()

    tk.Button(
        ventana,
        text="Buscar",
        command=lambda: entrada_ruta.insert(0, filedialog.askopenfilename())
    ).pack()

    tk.Label(ventana, text="Clave (Base64 - 44 caracteres):").pack()
    entrada_clave = tk.Entry(ventana, width=50)
    entrada_clave.pack()

    tk.Button(
        ventana,
        text="Desencriptar",
        command=lambda: desencriptar_archivo(entrada_ruta.get(), entrada_clave.get(), ventana)
    ).pack(pady=10)

# -------- Interfaz principal --------

root = tk.Tk()
root.title("Encriptador de Archivos")
root.geometry("600x300")

estado_programa = tk.StringVar()
estado_programa.set("Usa el menú para seleccionar una opción")

barra_menu = tk.Menu(root)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Encriptar Archivo", command=mostrar_ventana_encriptar)
menu_archivo.add_command(label="Desencriptar Archivo", command=mostrar_ventana_desencriptar)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=barra_menu)

tk.Label(root, textvariable=estado_programa, font=("Arial", 14)).pack(pady=50)

# -------- Inicio --------
root.mainloop()

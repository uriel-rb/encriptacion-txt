# Encriptador de Archivos (Tkinter + Fernet)

Este programa proporciona una interfaz gráfica para encriptar y desencriptar archivos `.txt` utilizando el cifrado simétrico `Fernet` de la biblioteca `cryptography`.

---

## 📦 Requisitos

- Python 3.6 o superior
- Librerías instaladas:
  - `cryptography`
  - `tkinter` (viene con Python en la mayoría de distribuciones)

Puedes instalar la dependencia faltante con:

```bash
pip install cryptography
```
## 🔧 Funcionalidad
- Se debe utilizar el menú Archivo para comenzar a encriptar o desencriptar.
- El primer campo de entrada siempre será la ruta del archivo, y el segundo la clave en texto plano.
- Al encriptar, en caso de no proporcionar una clave, esta se generará automáticamente y se guardará en la ruta del programa.
- Los archivos .key (clave generada) se guardarán en la misma ruta del programa, y los archivos encriptados .enc se guardarán en la misma ruta del archivo original.
---

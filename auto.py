import pywhatkit as kit
import pandas as pd
import time
import webbrowser

# Ruta a Chrome con el perfil correcto
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Informes Colegio Solaris" %s'
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))

# 📌 Cargar contactos desde el archivo CSV
archivo_csv = "contacto.csv"
df = pd.read_csv(archivo_csv, sep=';')

# 📌 Ruta de la imagen
imagen_path = "imag.jpg"

# 📌 Iterar sobre cada contacto y enviar el mensaje
for index, row in df.iterrows():
    nombre = row["nombre"]
    numero = str(row["telefono"]).strip()  # Elimina espacios en blanco
    
    # Asegurar formato correcto
    if not numero.startswith("+"):
        numero = "+" + numero  # Ajusta el código según tu país

    mensaje = f"""¡Hola {nombre}, tenemos una super promoción hoy!
    "¡20% DE DESCUENTO en alimento para tu mascota! 🐾

En Patas y Manchas cuidamos su salud como tú lo harías.
✅ Solo por hoy
✅ Envío GRATIS para los primeros 10 pedidos

¡No esperes, aprovecha ahora!"
    """
    print(f"📩 Enviando mensaje a {nombre} ({numero})...")

    try:
        # Enviar el mensaje con imagen
        kit.sendwhats_image(numero, imagen_path, mensaje, wait_time=30)
        
        # ⏳ Pausa larga para evitar bloqueos
        time.sleep(60)
    
    except Exception as e:
        print(f"❌ Error al enviar a {nombre}: {e}")

print("✅ Mensajes enviados correctamente.")
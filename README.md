# 🐾 WhatsApp Automatización - Promoción Personalizada

Este script permite **enviar mensajes personalizados por WhatsApp con una imagen** a una lista de contactos utilizando `pywhatkit`, todo desde un entorno virtual y con tu perfil de Chrome configurado para usar WhatsApp Web automáticamente.

> 💡 Ideal para campañas de difusión, promociones de negocio o recordatorios a clientes.

---

## 📂 Estructura del Proyecto
pract_python/ │ ├── contacto.csv # Lista de contactos con nombre y teléfono ├── imag.jpg # Imagen que se enviará junto al mensaje ├── auto.py # Script principal ├── README.md # Documentación └── .venv/ # Entorno virtual
---

## ⚙️ Requisitos

- Python 3.8 o superior
- Google Chrome instalado
- Una sesión activa de WhatsApp Web en un perfil específico de Chrome

---

## 🧪 Crear y activar entorno virtual

```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno (en PowerShell o CMD)
.\.venv\Scripts\activate

# 3. Instalar dependencias necesarias
pip install pywhatkit pandas

```

## 📦 Archivos necesarios
contacto.csv
Debe tener el siguiente formato (separado por ;):

nombre;telefono

Pedro;+51994488506

Maria;+51923660234

✅ Incluye el código de país (+51 para Perú).


## 🖼️ Imagen personalizada
Asegurate de tener en la misma carpeta el archivo imag.jpg que quieras enviar con el mensaje.




## 🔒 Usa tu perfil de Chrome con WhatsApp Web
Para asegurarte de que el mensaje se envía desde la cuenta correcta de WhatsApp:

Abre WhatsApp Web manualmente con tu perfil:

powershell
Copiar
Editar
start chrome --profile-directory="Informes Colegio Solaris" https://web.whatsapp.com
Escaneá el QR si es necesario. No cierres esa pestaña.

Luego, ejecutá el script desde tu entorno virtual.

## ▶️ Ejecución del script
Con todo listo y el entorno activado:

bash
Copiar
Editar
python auto.py

📋 Ejemplo de salida:
bash
Copiar
Editar
📩 Enviando mensaje a Juan (+51948508806)...
📩 Enviando mensaje a Jossy (+51958660734)...
✅ Mensajes enviados correctamente.

## 🛠️ ¿Qué hace el script?
Lee un archivo .csv con nombres y teléfonos

Personaliza un mensaje para cada contacto

Usa el perfil de Chrome con WhatsApp Web ya abierto

Envía un mensaje con una imagen adjunta

Agrega pausas entre cada envío para evitar bloqueos

## ❗ Consideraciones
No cierres la pestaña de WhatsApp Web mientras se ejecuta el script.

La primera pestaña puede fallar al enviar; los siguientes mensajes se envían correctamente.

pywhatkit aún no permite controlar totalmente las ventanas abiertas de Chrome (abre una nueva pestaña por mensaje).
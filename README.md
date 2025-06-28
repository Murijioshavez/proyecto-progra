# Asistente de Registro para Actividades Extracurriculares  
**Grupo 6**

## 📝 Descripción del Proyecto

El Asistente de Registro para Actividades Extracurriculares es una aplicación web desarrollada con Flask que permite a los estudiantes del Key Institute registrar y visualizar sus actividades extracurriculares de forma estructurada.  

Incluye una interfaz sencilla para publicar actividades, una vista tipo calendario interactivo para consultar el historial y una página de bienvenida informativa.

## Tecnologías utilizadas

- Python 3.13
- Flask
- HTML + Tailwind CSS
- JSON para almacenamiento de datos
- JavaScript (evo-calendar)
- Jinja2 (motor de plantillas)

## Estructura del proyecto

proyecto/
├── app.py
├── registro.py
├── actividades.json
├── templates/
│ ├── index.html
│ ├── navbar.html
│ ├── nueva.html
│ └── actividades.html
├── static/
│ ├── favicon.png
│ ├── logo_blanco.png
│ └── evo-calendar/ (estilos y scripts)
├── requirements.txt
└── README.md

bash
Copiar
Editar

## ⚙️ Instrucciones para ejecutar localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto-asistente-registro.git
cd proyecto-asistente-registro
2. Crear y activar un entorno virtual
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate      
venv\Scripts\activate         
3. Instalar las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
4. Ejecutar la aplicación
bash
Copiar
Editar
python app.py
La aplicación estará disponible en:
http://127.0.0.1:5000

📦 Librerías necesarias
Estas se instalan automáticamente desde requirements.txt, pero son:

Flask

gunicorn (opcional para servidores, no requerido en local)

🗂️ Datos de prueba
El archivo actividades.json sirve como base de datos. Si no existe, se creará automáticamente con el primer registro desde la app.

Estructura de cada entrada:

json
Copiar
Editar
{
  "categoria": "Deporte y cultura",
  "descripcion": "Torneo de ping-pong",
  "duracion": "2 horas",
  "comentario": "Competencia interna en el gimnasio",
  "fecha": "2025/06/20",
  "color": "#11FF99"
}
✅ Notas adicionales
El proyecto no requiere base de datos externa.

Los archivos .json deben tener permisos de lectura/escritura.

La fuente de la universidad Key Blue fue respetada en el diseño.

El sitio está adaptado para escritorio y móviles gracias a TailwindCSS.
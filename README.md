<<<<<<< HEAD
# Nombre del Proyecto 📚
LibraryControl
# Descripción del Proyecto 🚀
Este es un mini proyecto de Django para la gestión de préstamos de libros en una biblioteca. Incluye modelos para autores, libros, miembros y préstamos.Enfocado a practicar y consolidar Django, ya que como vera usted, unicamente se usa Django con Python y SQL lite, sin nada de HTML, etc, pero aun así un paso es un paso. Aquí tiene el mini proyecto.

## Funcionalidades 🌟

- Gestión de autores y libros.
- Control de préstamos y devoluciones.
- Optimización de consultas con `select_related`.
- Manager personalizado para consultas específicas.
    (unicamente con Book para practicar)
- Clases metas para personalizar los comportamientos y datos del modelo Book.
- Funciones strings para que los modelos se muestren de forma mas amigable.
- Prática de consultas con incluso prueba de errores y excepciones.

## Requisitos del Sistema 💻

- Python 3.10
- Django 5.0.7
- SQLite (o el sistema de base de datos que estés usando)

## Instalación 🛠️

1. Clona el repositorio:
   ```bash
    git clone https://github.com/daniilabradorr/LibraryControl.git
    cd LibraryControl

2. Configura un entorno virtual (si aún no lo has hecho):
    python -m venv venv
# Activa el entorno virtual:
# En Windows:
    venv\Scripts\activate
# En macOS o Linux:
    source venv/bin/activate

3. Instala las dependencias:
    pip install -r requirements.txt

4. Aplica las migraciones:
    python manage.py migrate

5. Crea un superusuario (para acceder al panel de administración):
    python manage.py createsuperuser
# Sigue las instrucciones para crear un nombre de usuario y contraseña.

6. Inicia el servidor de desarrollo:
    python manage.py runserver
# Abre tu navegador y ve a http://127.0.0.1:8000/ para acceder a tu aplicación.

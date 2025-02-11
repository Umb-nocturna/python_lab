<!---
Last Update : Feb 10 /2025
-->

### CAP 1: Install Django

1. Instalar la libreria desde pip
    ```
    pip install Django
    ```

2. Crear el proyecto:
    ```
    django-admin startproject <miproyecto> .  #Linux - mac
    python -m django startproject <miproyecto> .  #win
    ```

3. se crea el proyecto dentro de la carpeta donde me encuentro. 

4. Puedo probar y ver mi nuevo proyecto asi:
    ```
    python manage.py runserver
    ```

5. Me crea el server con le URL para acceder al sitio 

6. Si apaceren pendientes migraciones. Ejecuto el comando:
    ```
    python manage.py migrate
    ```

7. Ya podemos comprobar que no aparecen actualizaciones.

> Conclusión: Django instalado en nuestro entorno de desarrollo.



### CAP 2: Super User (Admin)

8. Vamos a crear un super usuario para acceder al administrador, asi:

9. En el terminal con el siguiente comando :

    ```
    python manage.py createsuperuser
    ```

10. Asignamos un "usuario", "email" y un "password"

11. Activamos de nuevo el Server y probamos las credenciales



### CAP 3: PRIMERA APP - fotos

12. Luego creamos nuestra aplicacion para nuestro proyecto, En este caso es la app de "fotos", asi:

13. Crear la carpeta que contendra todas las aplicaciones que compondran nuestro proyecto "apps/".

14. ir a la carpeta "apps/" y dentro de esta ejecutar el comando:

    ```
    django-admin startapp <nombre-app> //linux
    python -m django startapp <nombre-app>  //win
    ```

15. Aparecera dentro de nuestra carpeta "apps/<nueva-app>/" con los archivos de python.

16. Registramos la nueva app al archivo de configuracion del proyecto, asi:
 
    ```
    'apps.fotos',
    ```

17. Ahora en el archivo "apps.py" de mi aplicacion, configuramos el nombre de la aplicacion para indicar que esta dentro de la carpeta "apps/", asi:

    ```
    class FotosConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'apps.fotos'

    ```

18. Dentro de nuestra aplicacion, vamos al archivo "models.py", alli, declaramos la estructura que 
   tendra el objeto "fotos" en la Base de datos. Por ahora vamos a definir 4 campos (name, descripcion y publish).

    ```
    from django.db import models

    class Mifoto(models.Model):
        nombre = models.CharField(max_length=90)
        descripcion = models.CharField( max_length=2000 )
        imageurl = models.CharField(max_length=120)
        publish = models.BooleanField(default=True)
        date = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return self.nombre
    ```


19. Ahora vamos al archivo "admin.py", aqui le decimos Django que este modelo se va a administrar 
   desde su interfaz. asi:

    ```
    from .models import Mifoto 

    admin.site.register(Mifoto)
    
    ```

20. Ahora en la consola ejecutamos el comando, 
    ```
    python manage.py migrate
    ```
    Si no presenta errores, ejecutamos el siguiente:
    ```
    python manage.py makemigrations
    ```  

    Si el terminal reporta `(You have 1 unapplied migration(s).)`, ejecute en el terminal nuevamente:
    ```
    python manage.py migrate
    ```

21. Verificar desde la interfaz de administracion de Django, si la entidad existe e insertar unos registros de prueba.



### CAP 4: PRIMER TEMPLATE y VIEW - Pagina album
(Prerequisito: Teoria MVT, Templating)

22. Crear el folder "/templates" dentro de la app, en este caso dentro de "/apps/fotos/"

23. Dentro del folder "apps/fotos/templates" crear el archivo "album.html". Puedes colocar tu codigo HTML o usar este de ejemplo

```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Álbum de Fotos</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            .gallery { display: flex; flex-wrap: wrap; justify-content: center; }
            .photo { margin: 10px; padding: 10px; border: 1px solid #ccc; width: 200px; }
            img { width: 100%; height: auto; }
        </style>
    </head>
    <body>
        <h1>Álbum de Fotos</h1>
        <div class="gallery">
            {% for foto in fotos %}
                <div class="photo">
                    <img src="{{ foto.imagen.url }}" alt="{{ foto.nombre }}">
                    <h3>{{ foto.nombre }}</h3>
                    <p>{{ foto.descripcion }}</p>
                </div>
            {% empty %}
                <p>No hay fotos disponibles.</p>
            {% endfor %}
        </div>
    </body>
    </html>
```

24. Creamos la VIEW. Ahora vamos a generar la lista de fotos. Dentro de "views.py" de mi Aplicacion:

```
from .models import Mifoto

def album(request):
    fotos = Mifoto.objects.all()
    return render(request, "album.html", {"fotos": fotos})
```
Genero la consulta por medio del ORM, y lo envio como variable a "album.html"


25. Ahora le decimos al sistema de URLS del proyecto, que necesitamos tener una url "/album/" que renderizara el html "album.html".
Si aún no tienes un archivo "apps/fotos/urls.py", créalo y añade:

```
from django.urls import path
from .views import album

urlpatterns = [
    path('album/', album, name='album'),
]
```
Se debe importar la view de nuestra app "fotos".


26. Luego le dicimos al sistema general del proyecto de URLS, que desde la app "/apps/fotos/urls.py" se han definido unas "url´s"

```
from django.urls import path, include
    ...
    + path('fotos/', include('apps.fotos.urls')),  # Incluye las rutas de la app fotos
    ...
```


#### Django - Folders Structur Guide Lines
![Alt text](https://github.com/Umb-nocturna/python_lab/blob/main/2-django_basic/structure_files_django_example.png "a title")

my_project/
│
├── my_project/                 # Configuración principal del proyecto.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/                       # Todas las aplicaciones de Django se almacenan aquí.
│   ├── users/                  # Una aplicación para gestionar usuarios.
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── orders/                 # Otra aplicación para gestionar pedidos.
│   │   ... (estructura similar a 'users')
│   │
│   └── ...                     # Otras aplicaciones.
│
├── static/                     # Archivos estáticos globales (CSS, JS, imágenes).
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/ 
│   ├── layouts/                # Plantillas (templates) globales.
│   │   ├── base.html
│   ├── includes/
│   │   ├── header.html
│   │   ├── footer.html
│   ├── pages/
│   │   ├── inicio.html
│   │   ├── resumen.html
│   │   ├── proyectos.html
│
├── media/                      # Archivos subidos por el usuario (Si se necesita).
│
├── .gitignore
├── README.md
├── requirements.txt            # Todas las dependencias del proyecto.
└── manage.py




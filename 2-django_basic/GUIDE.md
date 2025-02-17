<!---
Last Update : Feb 16 /2025
-->

## GUIA DJANGO

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
    Si no presenta errores, ejecutamos el siguiente comando:
    ```
    python manage.py makemigrations
    ```  

    Si el terminal reporta `(You have 1 unapplied migration(s).)`, ejecute en el terminal nuevamente:
    ```
    python manage.py migrate
    ```

21. Verificar desde la interfaz de administracion de Django, si la entidad existe e insertar unos registros de prueba.



### CAP 4: PRIMER TEMPLATE - Pagina index desde el template del proyecto
(Prerequisito: Teoria MVT, Templating)

22. Crear el folder "/templates" dentro del proyecto.

23. Dentro del folder "/templates" creamos "/layouts","/pages","/includes"

24. Dentro del folder "/templates/layouts" crear el archivo "base.html" y ponga el siguiente codigo como ejemplo.

```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %} {% endblock %}</title>
        <!--<link rel="stylesheet" href="/static/styles.css">-->
    </head>
    <body>
        <header>
            <h1>Mi Proyecto</h1>
            <nav>
                <a href="/">Inicio</a>
                <a href="/admin/">Admin</a>
            </nav>
        </header>

        <main>
            {% block content %}

            {% endblock %}
        </main>

        <footer>
            <p>&copy; 2025 - Todos los derechos reservados.</p>
        </footer>
    </body>
    </html>

```

25. Dentro del folder "/templates/pages" crear el archivo "index.html" y ponga el siguiente codigo de ejemplo.

```
    {% extends "layouts/base.html" %}

    {% block title %}Title from index.html {% endblock %}

    {% block content %}
    <h2>Conenido de index.html</h2>
    <p>Esta es la página de inicio.</p>
    {% endblock %}
```

26. Dentro del archivo "settings.py", agregamos a la variable TEMPLATES, lo siguiente:

```
    ...
    'DIRS': [os.path.join(BASE_DIR, "album/templates")],
    ...
```

26. Creamos el archivo "views.py" dentro del proyecto si no existe. Agregamos el siguiente codigo, para crear la view del index

```
    from django.shortcuts import render

    def inicio(request):
        return render(request,"pages/index.html",{})
```

27. Luego, agregamos dentro del archivo "urls.py" del proyecto la nueva vista.

```
from .views import inicio
```
Agregamos tambien la url del index dentro de urlpatterns:

```
    ...
    path('', inicio, name="inicio"),
    ...
```

28. Subimos el servidor y probamos la nueva pagina de index:

```
http://127.0.0.1:8000/
```


### CAP 4.1: PRIMER TEMPLATE - Modularización del template a header y footer

29. Se procede a segmentar el codgo html correspondiente a cada una de estas areas( header, footer) del Front del proyecto.

30. Se embeben en el archivo "/templates/layouts/base.html" asi :

```
    {% include "includes/header.html" %}

    {% include "includes/footer.html" %}
```


### CAP 4.2: PRIMER TEMPLATE - Agregando nueva seccion desde una APP

31. El ejemplo se realizara sobre el proyecto del "album", en la aplicacion "fotos".

32. Se crea la vista que traera todos los registros de las fotos en "views.py". Se genera la consulta por medio del ORM, y se envio como variable a "fotos.html"

```
    from .models import Mifoto

    # Create your views here.
    def fotos(request):
        mis_fotos = Mifoto.objects.all()
        return render(request,"pages/fotos.html",{"fotos":mis_fotos})
```
Nota: a. Verificar que el archivo "fotos.html" existe dentro de la carpeta "/templates" dentro de la aplicacion. b. Tener en cuenta que la variable que envia el arreglo de registros hacia el template es la variable "fotos" en este ejemplo.

33. Dentro del archivo "urls.py" de la aplicacion definiremos la url para esta pantalla, en este caso la llamaremos "/visor"

```
    from django.urls import path
    from . import views

    urlpatterns = [ 
        path("visor", views.fotos, name="fotos"),
    ]
```

34. En el archivo "urls.py" del proyecto

```
from django.urls import path, include
    ...
    + path('fotos/', include('apps.fotos.urls')),  # Incluye las rutas de la app fotos
    ...
```

35. En el archivo del template de la aplicacion "/fotos/templates/pages/fotos.html". 
Se define como un archivo que depende de un template base, se itera la variable fotos con los registros a mostrar.


```
    {% extends "layouts/base.html" %}

    {% block title %}Mis fotos{% endblock %}

    {% block content %}
        <h1>Álbum de Fotos</h1>
        <div class="gallery">
            {% for foto in fotos %}
                <div class="photo">
                    <img src="{{ foto.imageurl }}" alt="{{ foto.nombre }}">
                    <h3>{{ foto.nombre }}</h3>
                    <p>{{ foto.descripcion }}</p>
                </div>
            {% empty %}
                <p>No hay fotos disponibles.</p>
            {% endfor %}
        </div>
    {% endblock %}   
```

36. Subimos el servidor y probamos.



## RECURSOS


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




<!---
Last Update : Marzo 16 /2025
-->

## GUIA FASTAPI

### CAP 0: INSTALL

1. Se instala la libreria de FastAPI
´´´
    pip install fastapi 
´´´

2. Se instala la libreria del servidor uvicorn. Es un servidor de tipo ASGI (Asynchronous Server Gateway Interface)
´´´
pip install 'uvicorn[standard]'

o

pip install uvicorn

´´´

3. Crea archivo main.py para trabajar

´´´
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

´´´

4. Para ejecutar el proyecto se usa:

´´´
mac
    uvicorn main:app --reload

win
    python -m uvicorn main:app --reload

´´´

### CAP 1: IMPLEMENTANDO API BASICO DESDE HTML - QRCODE

1. Se instanciara un api basico, Documentacion:
    ```
    https://api.apgy.in/qr/documentation.html?ref=freepublicapis.com
    ```

2. Crear el HTML para ver la implementacion: Formulario y Imagen 
    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UMB Generador de QR - API</title>
    </head>
    <body>
        <h2>Generador de Código QR Desde un API</h2>
        <p>Documentacion: https://api.apgy.in/qr/documentation.html?ref=freepublicapis.com</p>
        <form id="qrForm">
            <input type="text" id="nombre" placeholder="Ingrese su nombre" required>
            <button type="submit">Generar QR</button>
        </form>
        <img id="qrImage" src="https://api.apgy.in/qr/?data=UMB&size=300" alt="QR Code">
    </body>
    </html>
    ```

3. Se agregan algunos Stilos

    ```
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 50px;
            }
            input, button {
                padding: 10px;
                margin: 10px;
                font-size: 16px;
            }
            img {
                margin-top: 20px;
            }
        </style>
    ```

4. Se agrega la implementacon por JS Vanilla:
    ```
    <script>
        document.getElementById("qrForm").addEventListener("submit", function(event) {
            event.preventDefault();
            let nombre = document.getElementById("nombre").value;
            let qrImage = document.getElementById("qrImage");
            qrImage.src = "https://api.apgy.in/qr/?data=" + encodeURIComponent(nombre) + "&size=300";
        });
    </script>
    ```

5. Se hace la prueba de la implementacion.



### CAP 2: API BASICO con Respuesta en JSON

1. Se instanciara un API, que retorna un JSON. Se usara de ejemplo el api de Dragon Ball. Documentacion:

```
https://web.dragonball-api.com/documentation?ref=freepublicapis.com
```

2. Crear el HTML para ver la implementacion: 

    ```
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>UMB Planetas de Dragon Ball</title>
    </head>
    <body>
        <h2>Planetas de Dragon Ball</h2>
        <p>Documentacion: https://web.dragonball-api.com/documentation?ref=freepublicapis.com</p>
        <div id="planets" class="planet-container"></div>

    </body>
    </html>

    ```

3. Script en JS que llama al api y trae la informacion:

    ```
     <script>
            async function fetchPlanets() {
                try {
                    let response = await fetch("https://dragonball-api.com/api/planets");
                    let data = await response.json();
                    let planetsContainer = document.getElementById("planets");
                    
                    data.items.forEach(planet => {
                        let planetDiv = document.createElement("div");
                        planetDiv.classList.add("planet");
                        planetDiv.innerHTML = `
                            <h3>${planet.name}</h3>
                            <p>${planet.description}</p>
                            <img src="${planet.image}" alt="${planet.name}">
                        `;
                        planetsContainer.appendChild(planetDiv);
                    });
                } catch (error) {
                    console.error("Error al obtener los planetas:", error);
                }
            }

            fetchPlanets();
        </script>
    ```

4. Se ajustan los Styles para que se vea mejor:
    ```
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
        .planet-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .planet {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            width: 300px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        img {
            width: 100%;
            border-radius: 8px;
        }
    </style>

    ```

5. Se hace la prueba de la implementacion.


### 3. Creando una Calculadora desde FastApi

1. Crear el endpoint

´´´
//Code example en archivo '/fastapi-lab/getstart/example.py'

´´´

2. Implementarla desde HTML
´´´
//Code example en archivo '/demos-html/demo-fastapi-calculadora/example.html'

´´´





## 📂 Estructura del Proyecto FastAPI
![Alt text](https://github.com/Umb-nocturna/python_lab/blob/main/3-fastapi_basic/fastapi-folders.png?raw=true "a title")

📦 my_fastapi_project
├── 📂 app
│   ├── 📂 routes
│   │   ├── item_routes.py
│   │   ├── user_routes.py
│   │   ├── __init__.py
│   ├── 📂 schemas
│   │   ├── item_schema.py
│   │   ├── user_schema.py
│   │   ├── __init__.py
│   ├── 📂 services
│   │   ├── item_service.py
│   │   ├── user_service.py
│   │   ├── __init__.py
│   ├── 📂 models
│   │   ├── item_model.py
│   │   ├── user_model.py
│   │   ├── __init__.py
│   ├── 📂 db
│   │   ├── database.py
│   │   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── __init__.py
├── 📂 tests
│   ├── test_items.py
│   ├── test_users.py
│   ├── __init__.py
├── 📜 .env
├── 📜 .gitignore
├── 📜 requirements.txt
├── 📜 README.md



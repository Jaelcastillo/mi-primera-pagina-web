# Mi Primera Página Web con Reflex

## Jael Castillo  
### Análisis y Diseño de Reportes — 5to B de Informática  
### Colegio Apec Fernando Arturo de Meriño  

---

# Descripción del Proyecto

Este proyecto consiste en el desarrollo de una primera página web utilizando el framework *Reflex, el lenguaje de programación **Python* y el gestor de dependencias *Poetry*.

La aplicación está inspirada en la serie *Grey's Anatomy* y fue creada como una práctica académica para aprender a desarrollar una aplicación web moderna utilizando principalmente Python.

El proyecto incluye una interfaz visual personalizada, un botón interactivo, manejo de estados, contador dinámico, uso de GitHub y documentación detallada para que cualquier persona pueda ejecutar la aplicación siguiendo este README paso a paso.

---

# Objetivos del Proyecto

Los objetivos principales de este proyecto son:

- Familiarizarse con el framework Reflex.
- Comprender la estructura básica de una aplicación web.
- Crear una página web funcional utilizando Python.
- Utilizar Poetry para administrar dependencias y entornos virtuales.
- Usar GitHub como plataforma de publicación y control de versiones.
- Realizar commits durante el desarrollo del proyecto.
- Documentar el proceso completo de instalación, desarrollo y ejecución.
- Explicar los problemas encontrados y sus soluciones.

---


# Tecnologías Utilizadas

| Tecnología | Uso dentro del proyecto |
|---|---|
| Python 3.12 | Lenguaje principal del proyecto |
| Reflex | Framework utilizado para crear la página web |
| Poetry | Administración de dependencias y entorno virtual |
| Node.js | Requerido por Reflex para ejecutar el frontend |
| Git | Control de versiones |
| GitHub | Publicación del repositorio |
| Visual Studio Code | Editor de código utilizado |

---

# Requisitos Previos

Antes de ejecutar el proyecto se deben tener instaladas las siguientes herramientas.

---

## 1. Python

Versión recomendada:

txt
Python 3.12.x


Para verificar la versión instalada:

bash
python --version

Nota importante:

Durante el desarrollo se detectó que Python 3.14 podía causar problemas de compatibilidad con Reflex, por eso se utilizó Python 3.12.

---

## 2. Poetry

Poetry se utilizó para manejar el entorno virtual y las dependencias del proyecto.

Para verificar que Poetry está instalado:

bash
poetry --version

## 3. Node.js

Reflex necesita Node.js para poder ejecutar la parte frontend de la aplicación.

Versión mínima requerida:

txt
Node.js 20.19.0 o superior


Para verificar Node.js:

bash
node -v


# Guía Completa para Ejecutar el Proyecto

Esta sección explica paso a paso cómo el profesor puede abrir y ejecutar el proyecto desde cero.

---

# Paso 1 — Clonar el Repositorio

Abrir CMD o PowerShell y ubicarse en la carpeta donde se desea guardar el proyecto.

Ejemplo si se desea guardar en el escritorio:

bash
cd Desktop


Si Windows está en español:

bash
cd Escritorio


Si el escritorio está dentro de OneDrive:

bash
cd OneDrive\Escritorio


Luego clonar el repositorio:

bash
git clone https://github.com/Jaelcastillo/mi-primera-pagina-web


Este comando descargará el proyecto desde GitHub.

---

# Paso 2 — Entrar a la Carpeta del Proyecto

Ejecutar:

bash
cd mi-primera-pagina-web


La terminal debe quedar ubicada dentro de la carpeta del proyecto.

---

# Paso 3 — Abrir el Proyecto en Visual Studio Code

Ejecutar:

bash
code .


Este comando abrirá el proyecto completo en Visual Studio Code.

---

# Paso 4 — Revisar el Archivo pyproject.toml

Antes de instalar las dependencias es importante revisar el archivo:

txt
pyproject.toml


Debe contener una versión de Python compatible.

Ejemplo correcto:

toml
requires-python = ">=3.10,<4.0"


Si aparece algo como:

toml
requires-python = ">=3.14"


puede causar errores al intentar usar Python 3.12.

---

# Paso 5 — Configurar Poetry con Python 3.12

En este proyecto se utilizó Python 3.12.

Comando utilizado en mi computadora:

bash
poetry env use "C:\Users\jaelc\AppData\Local\Programs\Python\Python312\python.exe"

# Paso 6 — Instalar Reflex con Poetry

En este proyecto Reflex fue instalado usando Poetry, no usando pip.

Comando utilizado:

bash
poetry add reflex


Este comando instala Reflex y sus dependencias necesarias.

Durante el desarrollo se instaló Reflex correctamente y se generó el archivo:

txt
poetry.lock


El archivo poetry.lock guarda las versiones exactas de las librerías para que el proyecto pueda ejecutarse igual en otra computadora.

---

# Paso 7 — Inicializar Reflex

Ejecutar:

bash
poetry run reflex init


Reflex mostrará opciones de plantilla.

Seleccionar:

txt
0 - A blank Reflex app


Esta opción permite iniciar una aplicación en blanco para desarrollar la página manualmente.

Resultado esperado:

txt
Success: Initialized mi_primera_pagina_web using the blank template.


---

# Paso 8 — Ejecutar la Aplicación

Ejecutar:

bash
poetry run reflex run


Si todo funciona correctamente, la terminal debe mostrar algo parecido a:

txt
App running at: http://localhost:3000/
Backend running at: http://0.0.0.0:8000


---

# Paso 9 — Abrir la Página Web

Abrir el navegador y entrar a:

txt
http://localhost:3000/


Ahí se visualizará la página web desarrollada con Reflex.



# Estructura del Proyecto

bash
mi-primera-pagina-web/
│
├── .venv/
├── .web/
├── assets/
│
├── mi_primera_pagina_web/
│   └── mi_primera_pagina_web.py
│
├── pyproject.toml
├── poetry.lock
├── rxconfig.py
├── README.md
└── .gitignore


---

# Explicación de los Archivos Principales

## mi_primera_pagina_web.py

Este archivo contiene el código principal de la aplicación.


# Comandos Utilizados Durante el Desarrollo

A continuación se muestran los comandos más importantes utilizados durante el desarrollo del proyecto.

---

## Clonar repositorio

bash
git clone https://github.com/Jaelcastillo/mi-primera-pagina-web


---

## Entrar al proyecto

bash
cd mi-primera-pagina-web


---

## Inicializar Poetry

bash
poetry init


---

## Configurar Python 3.12 con Poetry

bash
poetry env use "C:\Users\jaelc\AppData\Local\Programs\Python\Python312\python.exe"


---

## Instalar Reflex

bash
poetry add reflex


---

## Inicializar Reflex

bash
poetry run reflex init


---

## Ejecutar Reflex

bash
poetry run reflex run

# Problemas Encontrados y Soluciones

Durante el desarrollo aparecieron varios errores reales. A continuación se documentan junto con sus soluciones.

## Problema 1 — Python 3.14 no era conveniente para Reflex

### Descripción

La computadora tenía instalada la versión Python 3.14. Sin embargo, Reflex podía presentar problemas de compatibilidad con esa versión.

### Solución

Se instaló Python 3.12 y se configuró Poetry para usar esa versión.

bash
poetry env use "C:\Users\jaelc\AppData\Local\Programs\Python\Python312\python.exe"

## Problema 2 — Poetry rechazaba Python 3.12

### Descripción

El archivo pyproject.toml estaba configurado para Python 3.14.

Ejemplo del problema:

toml
requires-python = ">=3.14"

### Solución

Se modificó la restricción de Python a:

toml
requires-python = ">=3.10,<4.0"

Después de ese cambio, Poetry pudo crear el entorno virtual con Python 3.12.

## Problema 3 — Node.js no estaba instalado o no era reconocido

### Descripción

Al inicializar Reflex apareció el mensaje:

txt
Reflex requires node version 20.19.0 or higher to run

Esto ocurrió porque Reflex necesita Node.js para ejecutar el frontend.

### Solución

Se instaló Node.js desde la página oficial:

txt
https://nodejs.org/


Luego se verificó con:

bash
node -v
npm -v

# Verificación Final

Para confirmar que el proyecto funciona correctamente se debe ejecutar:

bash
poetry run reflex run


Luego abrir:

txt
http://localhost:3000/


# Recursos Oficiales
## Reflex
## Documentación Oficial de Reflex
## Poetry
## Node.js
## GitHub



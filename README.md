# Validador de Partidas de Ajedrez en SAN con Árbol Binario
Este repositorio contiene un programa orientada a objetos desarrollada en Python, que permite validar sintácticamente una partida de ajedrez escrita en notación algebraica estándar (SAN) y representarla como un árbol binario intercalado por turnos.

---

## Descripción del Proyecto

El sistema analiza una partida de ajedrez completa línea por línea, verificando que cada jugada cumpla con las reglas definidas en una gramática BNF simplificada. Si la partida es válida, construye un árbol binario donde cada nodo contiene una jugada, y los hijos izquierdo y derecho representan las jugadas de las blancas y negras, respectivamente.

---

## Funcionamiento

Si la partida es válida:

- Se parsea en estructuras de datos (`Partida`, `Turno`, `Jugada`).
- Se construye un árbol binario donde:
  - El nodo raíz representa el inicio de la partida.
  - Cada nivel contiene un turno.
  - Los nodos hijo representan las jugadas blanca (izquierda) y negra (derecha) de cada turno.
  - Se puede visualizar el arbol creado por medio de una interfaz gráfica interactiva. 

---

## Integrantes del proyecto
- Ana Sofía Angarita 
- Isabella Cadavid Posada
- Wendy Vanessa Atehortua Chaverra

  ---

## Video sustentación del programa

---
## Contenido del repositorio 
- Archivos código fuente del programa en Python
  - `Main.py`: Ejecuta el programa principal.
  - `parser.py`: Contiene el analizador sintáctico (`ParserSAN`).
  - `jugada.py`, `turno.py`, `partida.py`: Definen las clases base de la estructura de la partida.
  - `tree.py`: Contiene la clase
  - `VisualizadorAjedrez` que dibuja el árbol binario.
  - `README.md`: Este archivo.
- Archivo README.md
- Link al video de sustentación

  ---

## Entorno de desarrollo usado para el proyecto

El proyecto fue desarrollado utilizando:

- **Lenguaje**: Python 3.10+
- **Editor**: Visual Studio Code
- **Librerías utilizadas**:
  - `re`: Validación de sintaxis de movimientos con expresiones regulares.
  - `matplotlib.pyplot`: Visualización gráfica del árbol de jugadas.
  - `matplotlib.widgets`: Interacción con botones en el gráfico.
  - `networkx`: Construcción y visualización de grafos dirigidos (el árbol de la partida).
  - `typing`: Tipado estático para listas y tipos opcionales.

  ---

## ¿Cómo ejecutar el programa?

1. Descarga o clona este repositorio
2. Asegurate de tener el lenguaje de Python en tu computadora, en caso contrario descargarlo desde: https://www.python.org/
3. Instalar Visual Studio Code
4. Instalar la extensión para Python
5. Instalar las dependencias y librerias necesarias
6. Asegúrate de tener `matplotlib` y `networkx` instaladas
7. Ejecuta el programa

   ##### Nota Importante: En caso de que no se deje ejecutar el programa por el boton de ejecución, ejecutelo por terminal escribiendo Python Main.py

## Gracias por visitar este proyecto

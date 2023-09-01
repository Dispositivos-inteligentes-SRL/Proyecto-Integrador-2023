![logo](/src/ISPC_portada.png)

## Objetivo del Proyecto
La empresa "Dispositivos Inteligentes SRL" nos ha encomendado la tarea
de diseñar y desarrollar un nodo IoT (Internet de las Cosas) capaz de
registrar al menos una variable importante en una base de datos. Este
proyecto tiene como objetivo aplicar tus conocimientos en electrónica y
programación de microcontroladores para crear un dispositivo inteligente
que sea capaz de recopilar y almacenar datos relevantes.

**El esquema general del sistema a desarrollar se muestra en la siguiente imagen:**

![esquema](/src/esquema.jpg)


1. Se dispondrá de un sensor que mida una variable de interés.
2. Este sensor será conectado a un microcontrolador (Arduino o
similar), el cual enviará datos por puerto serie a una PC. Adicional a
esto, cuando la variable medida supere cierto umbral, se accionará
un actuador.
3. En esta PC correrá un programa, a desarrollar, en Python que leerá
el puerto serie, y enviará datos a un Sistema Gestor de Base de
Datos local.
4. Por último, nuestro SGDB, almacenará los datos recibidos desde el
programa Python cliente.
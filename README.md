# Gestion Visualizacion Del Programa EGC 17/18
Repositorio para llevar a cabo el trabajo sobre Gestión de visualización del programa, de la asignatura de EGC 17/18

Integrantes del grupo:
- Juan Pablo Argote Ortiz
- Jesús Enrique Bozada Márquez
- Alejandro Gallego Segura
- Anastasio Rafael Leon Gonzalez
- Jesus Sosa Sánchez

Para instalar dependecias necesarias: 
```
pip install -r requirements.txt
```
### Entorno de desarrollo
A continuación se describen los entornos de desarrollo utilizados por el equipos. Se presentan dos diferentes debido a las necesidades del proyecto.

En primer lugar, se describe el entorno utilizado para desarrollar las funcionalidades la aplicación en python:
- **JetBrains PyCharm:** versión 2017.2.4 x64.
- **Python:** versión 2.7.
- **SQLite:** versión 3.10.1.
- **Django:** versión 1.11.8.
- **Docker**.
- **TravisCI**.
	
Por último, se describe el entorno utilizado para desarrollar la aplicación en android:
- **Android Studio:** versión 3.0.1 build #AI-171.4443003.
- **JRE:** 1.8.0_152-release-915-b01 amd64.
- **JVM:** OpenJDK 64-Bit.
- **SQLite:** versión 3.10.1.
- **Jenkins**.

### Gestión de la construcción e integración continua
Para la gestión de la construcción no hemos basado en el gestor de paquetes y librerias de python ***pip*** en su versión **9.0.1**. Con lo que si necesitabamos alguna librería ejecutabamos el siguiente código ```pip install <nombre de la librería>```, con esto ya la tendríamos disponible para usarla.

En cuanto a la gestión de la integración continua hemos utilizado ***Travis Cl*** iteraccionando con nuestro repositorio de ***GitHub*** de tal manera que el proceso utilizado es el siguiente:
- Creación del fichero **.travis.yml**.
- Trabajar en dicha rama y hacer commit.
- Travis se encarga de bajarse es último commit.
- Le ejecuta los correspondientes tests.
- Por último, vuelve a arrancar servidor de nuestra aplicación.

También mencionar que nuestra aplicación es arrancada en **Docker**, que se configura en el **.travis.yml** para que este funcione correctamente.

### Gestión de liberaciones, despliegue y entregas

**Gestión de liberaciones**

La liberación continua la gestionamos mediante el servicio ***Travis CI***, utilizado para probar nuestro proyecto alojado en el repositorio de GitHub. Para ello hacemos un fork al repositorio de ***GitHub*** y en Travis CI sincronizamos el mismo. Una vez hecho esto, automatizadas las pruebas del código, procedemos a ejecutarlas. ***Travis CI*** nos notifica por correo electrónico el resultado de la prueba, tanto si haya tenido éxito como con la aparición de un fallo. Si ha tenido éxito lo consideraremos como una nueva versión del código.

**Gestión de Despliegue**

El despliegue se hará mediante una imagen creada de Docker que será subida al repositorio general proporcionado por el equipo de integración. Una vez la imagen haya pasado las pruebas de ***Travis CI***, el archivo .travis.yml establecerá la nueva versión y se actualizará en la nueva imagen de ***Docker***.
**Política de nombrado e identificación de los entregables**

El entregable completo se realizará en nuestro repositorio de ***GitHub***, donde el documento podrá encontrarse en el archivo ***README.md***


# Gestion Visualizacion Del Programa EGC 17/18
Repositorio para llevar a cabo el trabajo sobre Gesti√≥n de visualizaci√≥n del programa, de la asignatura de EGC 17/18

Integrantes del grupo:
- Juan Pablo Argote Ortiz
- Jes√∫s Enrique Bozada M√°rquez
- Alejandro Gallego Segura
- Anastasio Rafael Leon Gonzalez
- Jesus Sosa S√°nchez

Para instalar dependecias necesarias: 
```
pip install -r requirements.txt
```
### Entorno de desarrollo
A continuaci√≥n se describen los entornos de desarrollo utilizados por el equipos. Se presentan dos diferentes debido a las necesidades del proyecto.

En primer lugar, se describe el entorno utilizado para desarrollar las funcionalidades la aplicaci√≥n en python:
- **JetBrains PyCharm:** versi√≥n 2017.2.4 x64.
- **Python:** versi√≥n 2.7.
- **SQLite:** versi√≥n 3.10.1.
- **Django:** versi√≥n 1.11.8.
- **Docker**.
- **TravisCI**.
	
Por √∫ltimo, se describe el entorno utilizado para desarrollar la aplicaci√≥n en android:
- **Android Studio:** versi√≥n 3.0.1 build #AI-171.4443003.
- **JRE:** 1.8.0_152-release-915-b01 amd64.
- **JVM:** OpenJDK 64-Bit.
- **SQLite:** versi√≥n 3.10.1.
- **Jenkins**.

### GestiÛn del cambio, incidencias y depuraciÛn
Para la gestiÛn de incidencias se realiza mediante **issues** de **Github**. Se crear·n en caso de que se vaya a realizar un avance o cambio en el proyecto, incluido los errores que aparezcan o tareas que se vayan a desempeÒar.
Para la creaciÛn de Èstas no hemos utilizado plantillas y se lleva a cabo el siguiente esquema: se pone un tÌtulo breve y descriptivo mediante el cual se identifique bien el contenido que va a tener esa incidencia y una descripciÛn en la que se explique el problema que ha tenido o la tarea realizada. Adem·s, se le aÒadir· una etiqueta, el proyecto asociado, el hito correspondiente y al miembro o miembros que la han creado, en el caso de que se tenga alguna duda o encuentre un problema se asignar· a todos los miembros del grupo ya sea para que se resuelva con la mayor rapidez posible o bien por si alguien en concreto no supiera resolverlo.  En caso de que se encuentre un ìbugî se adjuntar· el error encontrado en la descripciÛn de la incidencia.
La incidencia solo se cerrar· en el caso de que se estÈ seguro que se ha terminado o se haya solucionado, todos los miembros podr·n aÒadir comentarios si lo ven oportuno.
Etiquetas utilizadas:
Desarrollo
DocumentaciÛn
PlanificaciÛn
Despliegue
Bug
Otros
FormaciÛn
ReuniÛn

Tareas:
La gestiÛn de las tareas se controlar· mediante el tablero proporcionado por **Github**, por lo que estas pasar·n por tres estados que se ir·n modificando manualmente seg˙n sea oportuno: **To Do**, **In Progress** y **Done**.

 

### GestiÛn del cÛdigo fuente
Para la gestiÛn del cÛdigo se usa la herramienta Git, utiliz·ndola para realizar commits en el repositorio situado en la plataforma **Github**.

Commit
Se realizar· un **commit** cuando se obtenga un avance importante en el proyecto o se solucione alg˙n error. Para esto se utilizar· los siguientes comandos (se tendr· en cuenta la rama en la que se est· situado):
**git status** 				 # detectar modificaciÛn de archivos
**git add** <nombre del fichero modificado> o git add.
**git commit -a -m** ìcomentario de la nueva modificaciÛnî
**git push origin** <rama>  		#publicar el commit en el repositorio Github
**git checkout** <nombreArchivo> 	#para revertir un cambio antes de haber hecho un push
**git log -p**				#listar todos los commits realizados

Ramas
Para tener un mejor control de las funcionalidades, se ha creado una rama por cada una, existiendo en total 4 ramas secundarias y 1 rama principal:
master (principal)
twitter
pdf
telegram
aplicaciÛn Android (puesto que se desarrolla en otro lenguaje y no tiene nada que ver con las dem·s funcionalidades se encuentra en un repositorio aparte.

Comandos utilizados en las ramas:
**git branch** 			#ver la rama en la que est·s situado
**git branch** <nombreRama>	# crear una nueva rama
**git checkout** <nombreRama> 	# para cambiar de rama
**git merge** <nombreRama>	#unir la rama que se le pasa a la que estas situado
No se realizar· ning˙n **merge** a la rama principal (master) hasta que no estÈ totalmente completa la funcionalidad y haya pasado todas las pruebas necesarias.

ConexiÛn entre incidencias y commits
Cada vez que se lleva a cabo un commit importante sobre alguna de las ramas, este ser· aÒadido en la incidencia, ya que **Github** permite localizar los commits mediante su ëIDí y si este se copia en la **issue** correspondiente, se enlazan ambos.


### Gesti√≥n de la construcci√≥n e integraci√≥n continua
Para la gesti√≥n de la construcci√≥n no hemos basado en el gestor de paquetes y librerias de python ***pip*** en su versi√≥n **9.0.1**. Con lo que si necesitabamos alguna librer√≠a ejecutabamos el siguiente c√≥digo ```pip install <nombre de la librer√≠a>```, con esto ya la tendr√≠amos disponible para usarla.

En cuanto a la gesti√≥n de la integraci√≥n continua hemos utilizado ***Travis Cl*** iteraccionando con nuestro repositorio de ***GitHub*** de tal manera que el proceso utilizado es el siguiente:
- Creaci√≥n del fichero **.travis.yml**.
- Trabajar en dicha rama y hacer commit.
- Travis se encarga de bajarse es √∫ltimo commit.
- Le ejecuta los correspondientes tests.
- Por √∫ltimo, vuelve a arrancar servidor de nuestra aplicaci√≥n.

Tambi√©n mencionar que nuestra aplicaci√≥n es arrancada en **Docker**, que se configura en el **.travis.yml** para que este funcione correctamente.

### Gesti√≥n de liberaciones, despliegue y entregas

**Gesti√≥n de liberaciones**

La liberaci√≥n continua la gestionamos mediante el servicio ***Travis CI***, utilizado para probar nuestro proyecto alojado en el repositorio de ***GitHub***. Para ello hacemos un fork al repositorio de ***GitHub*** y en ***Travis CI*** sincronizamos el mismo. Una vez hecho esto, automatizadas las pruebas del c√≥digo, procedemos a ejecutarlas. ***Travis CI*** nos notifica por correo electr√≥nico el resultado de la prueba, tanto si haya tenido √©xito como con la aparici√≥n de un fallo. Si ha tenido √©xito lo consideraremos como una nueva versi√≥n del c√≥digo.

**Gesti√≥n de Despliegue**

El despliegue se har√° mediante una imagen creada de ***Docker*** que ser√° subida al repositorio general proporcionado por el equipo de integraci√≥n. Una vez la imagen haya pasado las pruebas de ***Travis CI***, el archivo ***.travis.yml*** establecer√° la nueva versi√≥n y se actualizar√° en la nueva imagen de ***Docker***.

**Pol√≠tica de nombrado e identificaci√≥n de los entregables**

El entregable completo se realizar√° en nuestro repositorio de ***GitHub***, donde el documento podr√° encontrarse en el archivo ***README.md***


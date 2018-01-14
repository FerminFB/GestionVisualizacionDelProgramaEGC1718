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
### Planificaci√≥n del proyecto

La planificaci√≥n realizada en este proyecto ha estado orientada al seguimiento por parte de los profesores en los diferentes Milestones, por tanto, se presentar√° dividida en secciones siguiendo el orden de √©stos.

#### Milestone 1 - Ecosistema preparado.

El objetivo principal que se propone cumplir antes de este milestone es la realizaci√≥n de una o m√°s reuniones con objetivo de conocernos como equipo, llegar a un acuerdo de la idea a desarrollar y de las trazas generales que se deben seguir para este cometido.

En el trascurso de estas reuniones se ha decido utilizar un grupo de Telegram como canal principal de comunicaci√≥n debido a la situaci√≥n laboral de tres componentes del grupo. Adicionalmente se decidi√≥ que la gestion de tareas se realice a trav√©s de GitHub, como se detallar√° m√°s adelante.

Dentro de las tareas a realizar durante este periodo de tiempo, se debe destacar la de conocimiento de dependencias con otros subsistemas del proyecto general. Esperando recabar dicha informaci√≥n a trav√©s del equipo de integraci√≥n.

#### Milestone 2 - Sistema funcionando con incremento.

Se aprovecha la revisi√≥n del Milestone 1 para aclarar cuales son las l√≠neas que debe seguir el proyecto para adaptarse a las dependencias encontradas.

Se prevee la utilizaci√≥n de una API aportada por otro equipo de trabajo, por tanto, se decide realizar durante este periodo de tiempo labores de estudio sobre las tecnolog√≠as, mientras el otro equipo aporta mayor informaci√≥n en cuanto a dicha API.

Se realizar√° una instanciaci√≥n base de un proyecto de Python sobre Django por Alejandro, debido a sus conocimientos, para que los dem√°s compa√±eros puedan avanzar en un futuro en las siguientes funcionalidades:
- Mostrar programa por Twitter. (Jes√∫s)
- Mostrar programa por Telegram. (Anastasio)
- Mostrar programa en formato pdf. (Alejandro)
- Mostrar programa como Calendar de Google. (Enrique)
- Mostrar programa en un aplicaci√≥n Android. (Juan Pablo)

En cuanto a la gesti√≥n de tareas se decide utilizar las issues de GitHub que ser√°n gestionadas como cards desde la vista de Proyecto del repositorio, una tarea podr√° encontrarse en tres fases diferentes:

- **ToDo:** aquellas tareas que est√©n pendientes de su comienzo.

- **In progress:** aquellas tareas que ya han comenzado.

- **Done:** aquellas tareas que han sido terminadas. 

#### Milestone 3 - Taller de automatizaci√≥n.

De cara a este Milestone, debido a un gran retraso en las funcionalidades, causado por la ausencia de la API que debe ser proporcionada por el equipo de programa, se decide implementar las funcionalidades en torno a ficheros de hoja de c√°lculo de excel.

Las principales tareas planificadas para este periodo de tiempo ser√°n la implementaci√≥n de una base de datos SQLite, en la que introducir la informaci√≥n del programa que se obtendr√° de dichos ficheros de hoja de c√°lculo. El estudio de que herramientas utilizar para la automatizaci√≥n de la construcci√≥n, la ejecuci√≥n de pruebas y la integraci√≥n.

#### Milestone 4 - Entrega y defensa de trabajos.

Para este Milestone, tras la revisi√≥n del anterior con el profesor, se llega a la conclusi√≥n de que se debe comenzar a realizar las labores de pruebas, integraci√≥n y automatizaci√≥n sin dejar atras la funcionalidad, debido al retraso existente. Por tanto, se decide que los componentes del grupo continuen el desarrollo de sus funcionalidades hasta la realizaci√≥n de una reuni√≥n una semana del Milestone para comenzar en com√∫n las tareas mencionadas anteriormente.

Debido a una interacci√≥n con el grupo de programa en el que se aporta, por parte de ellos, una posible soluci√≥n a la ausencia de API que consumir, se estudia la posibilidad de cambiar el desarrollo para adaptarlo a la propuesta, debido a la falta de tiempo y el retraso acumulado se decide ignorar la propuesta y continuar con la planificaci√≥n actual.

Por √∫ltimo, de cara a la entrega se decide avanzar lo m√°ximo posible en las tareas comunes para el beneficio de todos los componentes del grupo por encima del avance en las tareas individuales

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


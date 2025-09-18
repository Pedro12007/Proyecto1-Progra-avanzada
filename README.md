<img src="https://scontent.fgua3-5.fna.fbcdn.net/v/t39.30808-6/326497446_2360569570772075_4671112995358082924_n.png?_nc_cat=101&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=s5tQDeqKwlcQ7kNvwHKHEFc&_nc_oc=AdmJGZqPd3tSvT39Ozwa8kfKG4LgmkmqZZd4-kV4YvyHBWH8IYDV9ROOJHffoLnOU7e2X0XGLSEOhH1UluFrAb2u&_nc_zt=23&_nc_ht=scontent.fgua3-5.fna&_nc_gid=vGT1ijyXsqJfU7Q3-DUkOA&oh=00_AfZ_b7-HBEeRjsqqfIlVx3uxzxWbczE-kh33VS3gKs2beA&oe=68D11B7C" width="150">

### Proyecto 1 Programación avanzada
### Introducción
El programa es un gestionador de cursos. tareas. evaluaciones, estudiantes e instructores de forma virtual que tiene como base la programación orientada a objetos usando sus 4 pílares como guia, este sistema debe permitir registrar cursos, inscribir estudiantes, crear evalucaiones y almacenar calificaciones.

# Manual de usuario
El menú principal está conformado por 4 opciones:
1. Registrar usuario
2. Ingresar al sistema
3.  Administrar cursos
4. Salir



	
 ```
----------REGISTRO ESTUDIANTES----------
1. Registrar usuario 
2. Ingresar al sistema 
3. Administrar cursos 
4. Salir
Ingrese una opción:

``` 

Aqui el usuario decide que opción elegir para comenzar a usar el programa.

------------

Si  el usuario elige la opción 1, muestre el siguiente mensaje:

```
                    ----------REGISTRO DE USUARIO----------
1. Estudiante
2. Instructor
Ingrese una opción:  
```
En este apartado, el usuario debe elegir si desea registrar un estudiante o un instructor
ya que cada uno tiene opciones diferentes.
En este caso, el usuario eligio la opción número 1:

```
----------REGISTRAR ESTUDIANTES----------
Ingrese nombre: Rodrigo
Ingrese correo: RLopez@correo.url.edu.gt
Ingrese el año de nacimiento: 2000
Ingrese carnet: 1507525
Ingrese carrera: Ingenieria en Sistemas
Usuario agregado correctamente.
```
El usuario guarda al estudiante "Rodrigo" y llena todos los campos que requiere.
Ahora bien, si el usuario elije la opción número 2:
```
Ingrese nombre: Ricardo
Ingrese correo: RJurado@correo.url.edu.gt
Ingrese el año de nacimiento: 1990
Ingrese el codigo de empleado del instructor: 155332
Usuario agregado correctamente.
```
En este caso, el usuario registró al catedratico "Ricardo" y que ha sido guardado.

------------

Ahora si el usuario elije la opcion 2 "Instructor": 

```
Lista de usuarios:
ESTUDIANTE: |Nombre: Rodrigo|Correo: RLopez@correo.url.edu.gt|Año de nacimiento: 2000|Carnet: 1507525|Carrera: Ingenieria en Sistemas|
INSTRUCTOR: |Nombre: Ricardo|Correo: RJurado@correo.url.edu.gt|Año de nacimiento: 1990||Codigo de empleado: 155332|
Ingrese el id del usuario (carnet o código de empleado): 
```
El programa muestra los estudiantes/instructor que han sido agregados al programa, en este ejemplo, fue agregado 1 estudiante y 1 instructor.

------------

Si el usuario ingresa el carnet del estudiante:
```
Ingrese el id del usuario (carnet o código de empleado): 1507525
----------ACCESO AL SISTEMA DE ESTUDIANTE----------
1. Inscribirse en un curso.
2. Consultar mis cursos.
3. Ver mis evaluaciones.
4. Consultar mis calificaciones.
5. Volver a menu principal
Ingrese una opción: 
```

El usuario podra mostrar estas opciones, hay que tomar en cuenta que para inscribirse o consultar los cursos, se tiene que crear un curso previamente, por lo que pasaremos a la tercera opción de nuestro menu principal

------------

```
Ingrese una opción: 3
----------ADMINISTRAR CURSOS----------
1. Crear curso
2. Asignar curso a instructor
3. Consultar cursos
4. Generar reportes
5. Volver a menu principal
Ingrese una de las opciones: 
```
En esta opcion, veremos que sucede si el usuario elige la opción 1 "Crear curso":
```
Ingrese una de las opciones: 1
Ingrese código del curso: 123
Ingrese el nombre del curso: Calculo II
Ingrese el codigo del instructor: Jorge Molina
Curso agregado correctamente
```
El usuario creó un nuevo curso

------------
Si el usuario elige la opción 2"Asignar un curso a instuctor":
```
Ingrese una de las opciones: 2
Ingrese el id del curso: 123
Ingrese el codigo del instructor: 155332
Curso 123 asignado a instructor 155332
```
El curso  "Calculo II" que se creó previamente ahora fue asignado al instructor "Ricardo"

------------
Si el usuario elige la opcion 3:
```
Lista de cursos
1. |Id: 1|Nombre: precalculo|Instructor: 1|
2. |Id: 123|Nombre: Calculo II|Instructor: 155332|
```
Muestra la lista de los cursos que han sido asignados, arriba hay algunos ejemplos.

------------
Si el usuario elige la opcion 4:
```
--------Reporte de estudiantes con promedio bajo----------

No hay estudiantes con promedio bajo.
```
Esta opcion muestra estudiantes que tengan el promedio bajo, por el momento al no tener estudiantes, muestra el mensaje "No hay estudiantes con promedio bajo"

------------
Si el usuario elije la opcion 5:
```
----------REGISTRO ESTUDIANTES----------
1. Registrar usuario 
2. Ingresar al sistema 
3. Administrar cursos 
4. Salir
Ingrese una opción: 
```
Regresa al menu principal.

------------
Retomando la opcion 2, luego de crear cursos y asignarlos a los instructores, aparecerá estas opciones:
Lista de usuarios:
```
ESTUDIANTE: |Nombre: Rodrigo|Correo: RLopez@correo.url.edu.gt|Año de nacimiento: 2000|Carnet: 1507525|Carrera: Ingenieria en Sistemas|
INSTRUCTOR: |Nombre: Ricardo|Correo: RJurado@correo.url.edu.gt|Año de nacimiento: 1990||Codigo de empleado: 155332|
Ingrese el id del usuario (carnet o código de empleado):
```
El usuario ingreso el carnet de estudiante 1507525, por lo que tiene estas opciones para elegir y su rol es de estudiante:
```
----------ACCESO AL SISTEMA DE ESTUDIANTE----------

1. Inscribirse en un curso.
2. Consultar mis cursos.
3. Ver mis evaluaciones.
4. Consultar mis calificaciones.
5. Volver a menu principal
Ingrese una opción: 
```

------------
Ingresando la opcion 1: "Inscribirse en un curso"
```
Lista de cursos
1. |Id: 1|Nombre: precalculo|Instructor: 1|
2. |Id: 123|Nombre: Calculo II|Instructor: 155332|
Ingrese el id del curso al que desea inscribirse: 
```
El usuario ahora si puede inscribrse al curso que prefiera, en este caso sera con el id '123' por lo que se vera de esta manera:
```
Te has inscrito al curso con id: 123
1. Inscribirse en un curso.
2. Consultar mis cursos.
3. Ver mis evaluaciones.
4. Consultar mis calificaciones.
5. Volver a menu principal
```

------------
Ahora si el estudiante elige la opcion 2: "Consultar mis cursos:"
```
Ingrese una opción: 2
Cursos en los que estás inscrito:
1. |Id: 123|Nombre: Calculo II|Instructor: 155332|
```
Vemos en que cursos esta inscrito el estudiante

------------
Ahora si  el estudiante elije la opcion 3 "Ver mis evaluaciones"
```
Ingrese una opción: 3
No tienes ninguna evaluación asignada.
```
El estudiante no tiene ninguna evaluacion asignada, debido que el instructor a cargo de los cursos en que esta inscrito aun no ha asignado alguna evaluacion próxima.

------------
Si el estudiante ingresa la opcion 4 "Consultar mis calificaciones":
```
Ingrese una opción: 4
No tienes ninguna evaluación asignada.
```
El instructor aun no ha asignado una evaluacion pero a continuacion se vera la perspectiva del instructor y como será su menu:
tomando en cuenta que el usuario entro como instructor, su menu será así:
```
----------ACCESO AL SISTEMA DE INSTRUCTOR----------

1. Consultar mis cursos asignados
2. Ver estudiantes inscritos
3. Crear evaluaciones
4. Registrar calificaciones
5. Volver a menu principal
Ingrese una de las opciones: 
```
En caso de que el instructor eliga la opcion 1 "Consultar mis cursos asignados":
```
----------MIS CURSOS ASIGNADOS----------
1. |Id: 123|Nombre: Calculo II|Instructor: 155332|
```
Vemos que tiene un curso asignado, por lo que es capaz de crear evaluaciones y mostrar notas.

Si el instructor elige la opción 2 "Ver estudiantes inscritos":
```
--- Selecciona un curso para ver los estudiantes inscritos ---
1. Calculo II
Elige el número del curso: 1
Estudiantes inscritos en el curso 'Calculo II':
1. ESTUDIANTE: |Nombre: Rodrigo|Correo: RLopez@correo.url.edu.gt|Año de nacimiento: 2000|Carnet: 1507525|Carrera: Ingenieria en Sistemas|
```
Se muestra el o los estudiantes inscritos al curso asignado

------------
Si el instructor elige la opcion 3 "Crear evaluaciones":
```
Ingrese una de las opciones: 3
----------Mis Cursos Asignados----------
1. |Id: 123|Nombre: Calculo II|Instructor: 155332|
Ingrese el id del curso: 123
Ingrese el id de la evaluación: 1
Ingrese la descripción de la evaluación: Primer parcial
Ingrese el punteo (1-100): 15
Evaluación agregada correctamente.
```
El instructor ha asignado la evaluacion correctamente, ahora le aparece en "Ver mis evaluaciones" a los estudiantes.

------------

Si el instructor elige la opcion 4 "Registrar calificaciones":
```
Ingrese una de las opciones: 4
----------MIS CURSOS ASIGNADOS----------
1. |Id: 123|Nombre: Calculo II|Instructor: 155332|
Ingrese el id del curso: 123
Evaluaciones del curso 'Calculo II':
1. |Id: 1|Descripción: Primer parcial|Punteo: 15|
Ingrese el id de la evaluación: 1
Estudiantes inscritos en el curso 'Calculo II':
1. ESTUDIANTE: |Nombre: Rodrigo|Correo: RLopez@correo.url.edu.gt|Año de nacimiento: 2000|Carnet: 1507525|Carrera: Ingenieria en Sistemas|
Ingrese el id del estudiante deseado: 1507525
Ingrese la nota del estudiante (0-15): 10
```
El instructor le ha dado al estudiante "Rodrigo" una nota de 10/15 en "Primer parcial" del curso "Calculo II"

En dado que el usuario quiera salir del programa:
```
----------REGISTRO ESTUDIANTES----------
1. Registrar usuario 
2. Ingresar al sistema 
3. Administrar cursos 
4. Salir
Ingrese una opción: 4
Saliendo del programa...
```
El programa cierra exitosamente, terminando asi el ciclo.

### Final 

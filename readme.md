#  SISTEMA DE GESTION DE TORNEO DE FUTBOL

####  INTEGRANTES
Juan Jose Osorio Isaza
Santiago Umbarila


#### INSTRUCCIONES DE EJECUCION
Para poder ejecutar el proyecto es necesario irnos al modulo main y saber que hay que llamar las funciones mediante el from y el import. 
Teniendo en cuenta que hay que llamar una funcion colocamos "from" despues de este colocamos algun modulo(Arbitros, Equipos., Jugadores, Partidos, Sanciones) posteriormente colocamos "import" y ahora si el nombre de la funcion.
Luego en la linea de abajo colocamos la funcion junto a los parametros necesarios
EJEMPLO:
from partidos import actualizar_resultado
actualizar_resultado("PAR001", 3, 2)

Tener en cuenta que en estructuras del proyecto encontraremos las funciones junto a sus parametros



#### ESTRUCTURA DEL PROYECTO
El proyecto cuenta con 7 modulos:

Arbitros, Equipos., Jugadores, Partidos, Sanciones, main y borrador.

#####  ARBITROS:
En su interior podemos encontar una lista de diccionarios con los datos que se requieren de un arbitro, en este caso: id, nombre, experiencia, categoria y partidos dirigidos.
Posteriormente encontraremos las siguientes funciones:
###### registrar_arbitro(id_arbitro, nombre, experiencia, categoria)
Esta primera que se va a encargar de registrar un nuevo arbitro
###### asignar_arbitro(id_partido, id_arbitro, fecha_asignacion)
Esta se encargaria de asignar un arbitro ya registrado a un partido ya existente

#####  EQUIPOS:
En su interior podemos encontrar una lista de diccionarios que ya posee algunos equipos existentes con sus datos necesarios, en este caso: id, nombre, ciudad, dt,  y otra lista con las estadisticas de estos mismos equipos pero en este caso en 0.
ademas encontramos una lista de las capitales de colombia necesaria para verificar la ciudad del equipo:
posteriormente encontraremos las siguinetes funciones:
###### registrar_equipo(nombre,ciudad,dt,id)
esta seria la encargada de registrar un equipo nuevo al torneo
###### buscar_equipo(criterio,valor)
esta se utilizaria para buscar un equipo existente mediante el nombre del dt o la ciudad
###### actualizar_estadisticas(nombre_equipo, goles_favor, goles_contra)
y por ultimo esta que seria necesaria para el momento que necesitemos actualizar las estadisticas de un equipo

##### JUGADORES:
En este encontraremos una gran lista de diccionarios de jugadores que ya estan registrados con sus respectivos equipos y con su informacion necesaria en este caso: nombre, numero, posicion, equipo y otro diccionario en el interior de sus estadisticas
luego encontraremos las siguientes funciones:
###### registrar_jugador(nombre, numero, posicion, equipo)
que se encargara de registrar un nuevo jugador a un equipo ya existente
###### buscar_jugador(criterio,valor)
esta se utilizaria al momento de necesitar buscar un jugador mediante su nombre
###### actualizar_estadisticas_jug(nombre, goles, asistencias)
por ultimo la que se encargaria de actualizar las estadisticas de un jugador ya existente

##### PARTIDOS:
Que en su interior tendra una lista de diccionario con un partido ya estipulado que servira de referencia para los siguintes partidos y la informacion que estos necesitaran en este caso: id, id arbitro,fecha, equipo local,equipo visitante,goles local, goles visitante.
despues de esto encontaremos la funciones:
###### registrar_partido(id_partido, fecha, nombre_equipo_local, nombre_equipo_visitante)
que se encargara de registrar un nuevo partido entre dos equipos existente
###### actualizar_resultado(id_partido, goles_local, goles_visitante)
que se encargara de subir el resultado de un partido previamente registrado
###### registrar_evento(id_partido, minuto, tipo_evento, nombre_equipo, nombre_jugador)
y por ultimo este que se encargaria de registrar algun evento ocurrido durante un partido

##### SANCIONES:
tiene una lista de diccionario con una sancion ya estipulada para tomar como referencia al momento de otras sanciones y la informacion necesaria, ente caso: id, tipo , id del sancionado, motivo, duracion, fecha de inicio y estado.
posteriormente tiene funciones como:
###### registrar_sancion(id_sancion, tipo, id_sancionado, motivo, fecha_inicio, duracion)
que se usara para registrar una sancion a un jugador o equipo
###### actualizar_estado_sancion(id_sancion, fecha_cumplimiento)
esta se usa para cambiar el estado de la sancion de activa a cumplida

##### MAIN
que sera nuestro tablero sobre el cual vamos a trabajar, donde llamaremos a las funciones que necesitemos mediante el FROM y el IMPORT

###### BORRADOR
donde se encuentra todo el codigo junto y completo en modo spaghetti, antes de que fuera divido en modulos para una mejor solucion



#### FUNCIONALIDADES IMPLEMENTADAS
En nuestro proyecto usamos:
###### listas vacias
se utilizo para al momento de que se cumpla alguna condicion poder agregarle elementos
###### listas de diccionarios 
en todos los modulos hay listas de diccionarios utilizadas para poder agregarles sanciones nuevas, arbitros nuevos, equipos nuevos, jugadores nuevos y partidos nuevos
###### lower
en todo momento utlizamos lower para las cadenas de textos, para poder volver todo a minusculas y que sean mas faciles las comparaciones y encontar algo ya existente
###### none
en algunas funciones se uso el none para que algo inicialmente inciara sin valor y con forme se fueran cumpliendo condiciones tomara un valor o no
###### append
en la mayoria de los casos se utilizo para agregar los nuevos valores ingresados a la lista principal que contiene todo
from partidos import actualizar_resultado
actualizar_resultado("PAR001", 3, 2)

from sanciones import actualizar_estado_sancion
actualizar_estado_sancion("san009","1234")

from jugadores import actualizar_estadisticas_jug
actualizar_estadisticas_jug("dayro moreno",3,1)
actualizar_estadisticas_jug("dayro moreno",5,6)

from jugadores import buscar_jugador
buscar_jugador("nombre","dayro moreno")
buscar_jugador("nombre","j")

from partidos import registrar_partido
registrar_partido("PAR002",12,"once caldas","america")

from partidos import registrar_evento
registrar_evento("PAR001", 45, "gol", "once caldas", "Dayro Moreno" )
registrar_evento("par002", 12, "tarjeta amarilla", "america", "carlos sierra")


from equipos import registrar_equipo
registrar_equipo("cal","Cali","bal","234")

from equipos import buscar_equipo
buscar_equipo("ciudad", "cali")
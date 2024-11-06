partidos = [
    {
        "id": "PAR001",
        "fecha": "2024-11-01",
        "id_arbitro": "ARB001",
        "equipo_local": "once caldas",
        "equipo_visitante": "junior",
        "goles_local": 2,
        "goles_visitante": 1,
        "alineacion_local": [],
        "alineacion_visitante": [],
        "eventos": [
            {
                "minuto": 30,
                "tipo": "gol",
                "jugador": "once caldas",
                "equipo": "EQP001"
            }
        ]
    }
]
from equipos import equipos
from jugadores import jugadores


def registrar_partido(id_partido, fecha, nombre_equipo_local, nombre_equipo_visitante):
    """
    Esta funcion se utiliza para registrar un nuevo partido, teniendo en cuenta validaciones como:
    -los equipos deben existir
    -el equipo local no puede ser el mismo que el visitante
    -el id del partido debe ser nuevo

    y tiene como parametros:
    nombre_equipo_local(str): nombre del equipo local
    nombre_equipo_visitante(str): nombre del equipo visitante
    id_partido(str): identificar del partido
    """
    equipo_local = None    #inicia sin valor
    equipo_visitante = None    #inicia sin valor

    for equipo in equipos:
        if equipo["nombre"].lower() == nombre_equipo_local.lower():  #buscar equipo
            equipo_local = equipo  #toma el valor del equipo del nombre ingresaddo
            break

    if not equipo_local:  #si no toma valor
        print(f"Error: El equipo local '{nombre_equipo_local}' no está registrado.")
        return

    for equipo in equipos:
        if equipo["nombre"].lower() == nombre_equipo_visitante.lower():   #buscar equipo
            equipo_visitante = equipo   #toma el valor del equipo del nombre ingresado
            break

    if not equipo_visitante:  #si no toma valor
        print(f"Error: El equipo visitante '{nombre_equipo_visitante}' no está registrado.")
        return

    if equipo_local == equipo_visitante:    # equipo local y visitante no pueden ser el mismo
        print("Error: El equipo local y el equipo visitante no pueden ser el mismo.")
        return

    for partido in partidos:     
        if partido["id"] == id_partido: # verificar que el id del partido no exista
            print(f"Error: El ID del partido '{id_partido}' ya existe.")
            return

    nuevo_partido = {
        "id": id_partido,
        "fecha": fecha,
        "id_arbitro": None,  
        "equipo_local": equipo_local["nombre"],
        "equipo_visitante": equipo_visitante["nombre"],
        "goles_local": 0,  
        "goles_visitante": 0,
        "alineacion_local": [],
        "alineacion_visitante": [],
        "eventos": []
    }
    
    partidos.append(nuevo_partido)
    print(f"Partido con ID '{id_partido}' entre '{equipo_local['nombre']}' y '{equipo_visitante['nombre']}' registrado para la fecha {fecha}.")


def actualizar_resultado(id_partido, goles_local, goles_visitante):
    """
    Esta funcion se utiliza para actualizar resulato de un partido

    y tiene como parametros:
    goles_local(int): goles del equipo local
    goles_visitante(int): goles del equipo visitante
    id_partido(str): identificador del partido
    """
    partido_encontrado = None   #inicia sin valor
    for partido in partidos:
        if partido["id"].lower() == id_partido.lower():   #verificar que id no exista
            partido_encontrado = partido     #toma el valor de partido
            break

    if not partido_encontrado:   # no tomo ningun valor
        print(f"Error: El partido con ID '{id_partido}' no está registrado.")
        return

    partido_encontrado["goles_local"] = goles_local   
    partido_encontrado["goles_visitante"] = goles_visitante

    print(f"Resultados actualizados para el partido ID '{id_partido}': {goles_local} - {goles_visitante}.")



def registrar_evento(id_partido, minuto, tipo_evento, nombre_equipo, nombre_jugador):
    """
    Esta funcion se utiliza para registrar un nuevo evento en el partido, teniendo en cuenta validaciones como:
    -el tipo de evento debe ser valido(gol, tarjeta amarilla, tarjeta roja)

    y tiene como parametros:
    tiop_evento: evento ocurrido
    nombre_equipo(str): nombre del equipo
    nombre_jugador(str): nombre del jugador
    minuto(int): monuto del evento ocurrido
    id_partido(str): identificador de partido
    """
    tipos_validos = ["gol", "tarjeta amarilla", "tarjeta roja"]
    if tipo_evento.lower() not in tipos_validos:   #verificar que evento sea valido
        print(f"Error: El tipo de evento '{tipo_evento}' no es válido. Debe ser uno de los siguientes: {', '.join(tipos_validos)}.")
        return

    partido_encontrado = None
    for partido in partidos:          
        if partido["id"].lower() == id_partido.lower():   #verificar que el id (partido) ya exista
            partido_encontrado = partido #toma el valor de partido
            break

    if not partido_encontrado: #no tomo ningun valor
        print(f"Error: El partido con ID '{id_partido}' no está registrado.")
        return

    equipo_local = partido_encontrado["equipo_local"]  #toma el valor del equipo local
    equipo_visitante = partido_encontrado["equipo_visitante"]   #toma el valor del equipo visitante del partido

    if nombre_equipo.lower() not in [equipo_local.lower(), equipo_visitante.lower()]:  #verifica que el equipo ingresado sea alguno del partido
        print(f"Error: El equipo '{nombre_equipo}' no está registrado en el partido con ID '{id_partido}'. Deben ser '{equipo_local}' o '{equipo_visitante}'.")
        return

    jugador_encontrado = None
    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre_jugador.lower() and jugador["equipo"].lower() == nombre_equipo.lower(): #verifica jugador pertenezca al equipo
            jugador_encontrado = jugador
            break

    if not jugador_encontrado:
        print(f"Error: El jugador '{nombre_jugador}' no pertenece al equipo '{nombre_equipo}'.")
        return

    nuevo_evento = {
        "minuto": minuto,
        "tipo": tipo_evento,
        "jugador": nombre_jugador, 
        "equipo": nombre_equipo  
    }  #diccionario completado que se agregara a los eventos del partido
    
    partido_encontrado["eventos"].append(nuevo_evento)
    print(f"Evento registrado: {tipo_evento} del equipo '{nombre_equipo}' por el jugador '{nombre_jugador}' en el minuto {minuto} para el partido ID '{id_partido}'.")
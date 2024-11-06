arbitros = [{
 "id": "ARB001", 
 "nombre": "Carlos Rodríguez", 
 "experiencia": 5, 
 "categoria": "FIFA", 
 "partidos_dirigidos": 0
}
]

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

def registrar_arbitro(id_arbitro, nombre, experiencia, categoria):
    """
    Esta funcion se utiliza para registrar un nuevo arbitro, teniendo en cuenta validaciones como:
    -la categoria debe ser valida (FIFA,naciona,regional)
    -el id no debe existir

    y tiene como parametros:
    nombre(str): nombre del nuevo arbitro
    experiencia(int): años de experiencia como arbitro
    categoria(str): categoria que tiene como arbitro
    id_arbitro(str): identificar del arbitro
    """
    categorias_validas = ["FIFA", "nacional", "regional"]
    
    if categoria not in categorias_validas:   #verificar que las categorias sean validas
        print(f"La categoría '{categoria}' no es válida. Debe ser una de: {categorias_validas}")
        return
    
    for arbitro in arbitros:
        if arbitro["id"] == id_arbitro:       #verificar que el id no exista
            print(f"El ID del árbitro '{id_arbitro}' ya está registrado.")
            return
    
    nuevo_arbitro = {
        "id": id_arbitro,
        "nombre": nombre.lower(), 
        "experiencia": experiencia,
        "categoria": categoria.lower(),  
        "partidos_dirigidos": 0
    } #diccionario completado que se agregara a la lista arbitros
    
    arbitros.append(nuevo_arbitro)
    print(f"Árbitro con ID '{id_arbitro}', nombre '{nombre.lower()}' y categoría '{categoria.lower()}' registrado exitosamente.")



def asignar_arbitro(id_partido, id_arbitro, fecha_asignacion):
    """
    Esta funcion se utiliza para asiganar un arbitro a un partido, teniendo en cuenta validaciones como:
    -tanto el arbitro como el partido deben existir

    y tiene como parametros:
    fecha_asignacion(str): fecha que se asigno el arbitro
    id_arbitro(str):identificador del arbitro
    id_partido(str): identificar del partido
    """
    arbitro_encontrado = None
    for arbitro in arbitros:    
        if arbitro["id"] == id_arbitro: #verificar que el arbitro exista
            arbitro_encontrado = arbitro
            break
    
    if not arbitro_encontrado:
        print(f"El árbitro con ID '{id_arbitro}' no está registrado.")
        return
    
    partido_encontrado = None
    for partido in partidos:         #verificar que el partido exista
        if partido["id"] == id_partido:
            partido_encontrado = partido
            break
    
    if not partido_encontrado:
        print(f"El partido con ID '{id_partido}' no está registrado.")
        return
    
    asignacion = {
        "id_partido": id_partido,
        "id_arbitro": id_arbitro,
        "fecha_asignacion": fecha_asignacion
    }
    
    partido_encontrado["id_arbitro"] = id_arbitro
    
    arbitro_encontrado["partidos_dirigidos"] += 1
    
    print(f"Árbitro con ID '{id_arbitro}' asignado al partido '{id_partido}' el {fecha_asignacion}.")
    
    return asignacion
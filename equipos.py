equipos = [
    {
        "id": "EQP001",  
        "nombre": "once caldas",
        "ciudad": "manizales",  
        "dt": "hernan dario herrera",  
        "jugadores": [],  
        
    },
    {
        "id": "EQP002", 
        "nombre": "deportivo pereira",  
        "ciudad": "pereira",  
        "dt": "luis fernando suarez",  
        "jugadores": [],  
        
    },
    {
        "id": "EQP003",  
        "nombre": "independiente medellin",  
        "ciudad": "medellin",  
        "dt": "alejandro restrepo",  
        "jugadores": [],  
        
    },
    {
        "id": "EQP004",  
        "nombre": "junior",  
        "ciudad": "barranquilla",  
        "dt": "cesar farias",  
        "jugadores": [],  
        
    },
    {
        "id": "EQP005",  
        "nombre": "america",  
        "ciudad": "cali",  
        "dt": "polilla",  
        "jugadores": [],  
        
    }
]
estadisticas = [
    {
        "nombre": "once caldas",
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    },
    {
        "nombre": "deportivo pereira",
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    },
    {
        "nombre": "independiente medellin",
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    },
    {
        "nombre": "junior",
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    },
    {
        "nombre": "america",
        "estadisticas": {
            "puntos": 0,
            "partidos_jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    }
]


capitales_colombia = [
    "bogotá", "medellin", "cali", "barranquilla", "cartagena", "cucuta", "bucaramanga", "ibague",
    "pereira", "manizales", "villavicencio", "neiva", "valledupar", "monteria", "santa marta", 
    "armenia", "popayan", "sincelejo", "quibdo", "florencia", "tunja", "mocoa", "pasto", 
    "riohacha", "leticia", "san andres", "yopal", "mitu", "puerto carreño", "inírida"
]


def registrar_equipo(nombre,ciudad,dt,id):
    """
    Esta funcion se utiliza para registrar un nuevo equipo, teniendo en cuenta validaciones como:
    -no puede existir dos equipos con el mismo nombre ni el mismo ID
    -la ciudad del equipo debe ser una capital de colombia

    y tiene como parametros:
    nombre(str): nombre del nuevo equipo
    ciudad(str): ciudad del equipo a registrar
    dt(str): nombre del director tecnico del equipo
    id(str): identificar del equipo
    """
    for equipo in equipos:
        if equipo["nombre"].lower() == nombre.lower():  #verificar que el nombre del equipo no exista
            print(f"el nombre '{nombre}' ya existe")
            return
        if ciudad.lower() not in capitales_colombia:  #verificar que la ciudad del equipo sea una ciudad
            print(f"error: La ciudad '{ciudad}' no esta permitida")
            return
        if equipo["id"].lower() == id.lower():  #verificar que el id del equipo no exista
            print(f"el numero '{id}' ya existe")
            return
    nuevo_equipo = {
        "id": id,
        "nombre": nombre,
        "ciudad": ciudad,
        "dt": dt,
        "jugadores": [],
    }           #nuevo diccionario con los datos ingresados para posteriormente agregar a la lista ppal
    equipos.append(nuevo_equipo)
    print(f"Equipo '{nombre}' de la ciudad '{ciudad}'registrado")


def buscar_equipo(criterio,valor):
    """
    Esta funcion se utiliza para buscar un equipo existente, teniendo en cuenta validaciones como:
    -se debe buscar el dt o la ciudad del equipo

    y tiene como parametros:
    ciudad(str): ciudad del equipo 
    dt(str): nombre del director tecnico del equipo
    """
    if criterio not in ["ciudad", "dt"]:       #verificar que el parametro ingresado sea valido
        print("error: El criterio debe ser 'ciudad' o 'dt'.")
        return
    equipos_encontrados = []  #lista vacia para poder agregar el equipo que coincida con el parametro
    for equipo in equipos:
        if equipo[criterio].lower() == valor.lower():   #encontar coincidendias con el parametro ingresado
            equipos_encontrados.append(equipo)
    if equipos_encontrados:   #si hubo equipos que se agregaron a la lista
        print(f"Equipos encontrados con el {criterio} '{valor}':")
        for equipo in equipos_encontrados:    #el equipo agregado a la lista que antes estaba vacia
            print(f"ID: {equipo['id']}, Nombre: {equipo['nombre']}, Ciudad: {equipo['ciudad']}, DT: {equipo['dt']}")
    else:
        print(f"No se encontraron equipos que coincidan con el {criterio} '{valor}'.")


def actualizar_estadisticas(nombre_equipo, goles_favor, goles_contra):
    """
    Esta funcion se utiliza para actualizar estadisticas de un equipo existente

    y tiene como parametros:
    nombre_equipo(str): nombre del equipo
    goles_favor(int): goles a favor del equipo 
    goles_contra(int): goles en contra del equipo
    """
    equipo_encontrado = None      #inicialmente sin valor
    estadisticas_encontradas = None   #inicialmente sin valor
    for equipo in equipos:
        if equipo["nombre"].lower() == nombre_equipo:     # encontar el equipo 
            equipo_encontrado = equipo      # equipo encontrado toma el valor de equipo
            break
    for est in estadisticas:        
        if est["nombre"].lower() == nombre_equipo:   #en la  lista de estadisticas encontar el equipo
            estadisticas_encontradas = est    #estadisticas encontradas toma el valor de est
            break
    if not equipo_encontrado or not estadisticas_encontradas:   # si equipo_encontrado y estadistica_encontradas siguen sin valor
        print("Equipo no encontrado.")
        return
    
    est = estadisticas_encontradas["estadisticas"] #agregar goles y puntos a las estadisticas  
    est["partidos_jugados"] += 1
    est["goles_favor"] += goles_favor
    est["goles_contra"] += goles_contra

    if goles_favor > goles_contra:
        est["puntos"] += 3
        est["ganados"] += 1
        resultado = "ha ganado"
    elif goles_favor == goles_contra:
        est["puntos"] += 1
        est["empatados"] += 1
        resultado = "empató"
    else:
        est["perdidos"] += 1
        resultado = "perdió"

    print(f"{equipo_encontrado['nombre']} {resultado} el partido.")
    print("Estadísticas actualizadas:")
    for clave, valor in est.items():
        print(f"{clave}: {valor}")
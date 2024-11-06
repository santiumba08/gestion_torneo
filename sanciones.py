sanciones = [{
 "id": "SAN001", 
 "tipo": "jugador", 
 "id_sancionado": "JUG001", 
 "motivo": "Acumulación de tarjetas amarillas",
 "fecha_inicio": "2024-11-10",
 "duracion": 1, 
 "estado": "activa" 
}
]
from equipos import equipos
from jugadores import jugadores

def registrar_sancion(id_sancion, tipo, id_sancionado, motivo, fecha_inicio, duracion):
    """
    Esta funcion se utiliza para registrar una sancion, teniendo en cuenta validaciones como:
    -el tipo de sancion debe existir(jugador,equipo)

    y tiene como parametros:
    duracion(int): duracion en fechas de la sancion 
    fecha_inicio(str): fecha inicio de la sancion 
    motivo(str): motivo de la sancion
    tipo(str): a quien va la sancion(equipo,jugador)
    id_sancionado(str): identificador de jugador o equipo
    id_sancion(str): identificar de la sancion
    """
    tipos_validos = ["jugador", "equipo"]
    if tipo.lower() not in tipos_validos:  #verificar que la sancion sea a equipo o jugador
        print(f"El tipo de sanción '{tipo}' no es válido. Debe ser 'jugador' o 'equipo'.")
        return

    encontrado = False
    if tipo.lower() == "jugador":
        for jugador in jugadores:
            if jugador["id"] == id_sancionado:   #verificar que el jugador exista
                encontrado = True
                break
    else:  
        for equipo in equipos:
            if equipo["id"] == id_sancionado:    #verificar que el equipo exista
                encontrado = True
                break

    if not encontrado:
        print(f"El ID sancionado '{id_sancionado}' no existe en los registros de {tipo}.")
        return

    for sancion in sanciones:
        if sancion["id"] == id_sancion:   #verificar que el id no exista
            print(f"El ID de la sanción '{id_sancion}' ya está registrado.")
            return
        
    nueva_sancion = {
        "id": id_sancion,
        "tipo": tipo.lower(),  
        "id_sancionado": id_sancionado,
        "motivo": motivo,
        "fecha_inicio": fecha_inicio,
        "duracion": duracion,
        "estado": "activa"  
    } #diccionario completado que posteriormente se agragara a la lista sanciones

    sanciones.append(nueva_sancion)
    print(f"Sanción con ID '{id_sancion}' registrada exitosamente.")

def actualizar_estado_sancion(id_sancion, fecha_cumplimiento):
    """
    Esta funcion se utiliza para actualizar el estado de la sancion

    y tiene como parametros:
    fecha_cumplimiento(str): fecha cuando se cumplio la sancion
    id_sancion(str): identificar de la sancion
    """
    for sancion in sanciones:
        if sancion["id"] == id_sancion:  #verifica que la sancion exista
            if sancion["estado"] == "activa":  #verifica que la sancion este activa
                sancion["estado"] = "cumplida"   #pasa la sancion a cumplida 
                sancion["fecha_cumplimiento"] = fecha_cumplimiento
                print(f"Sanción con ID '{id_sancion}' actualizada a 'cumplida' con fecha de cumplimiento '{fecha_cumplimiento}'.")
                return
            else:
                print(f"La sanción con ID '{id_sancion}' ya está en estado '{sancion['estado']}'.")
                return
            
    print(f"No se encontró la sanción con ID '{id_sancion}'.")
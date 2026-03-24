define p10_09    = Character("[prota] (10-09)")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg oficina Stuard
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.
    python:
        prota = renpy.input("Ingresa tu nombre", length=32)
        prota = prota.strip()
    
        if not prota:
            prota = "Ty Rei (10-09)"

    "Acabas de despertar, no sabes dónde estás, es un lugar desconocido para ti.
    
    No recuerdas tu pasado ni qué pasó, lo único que recuerdas es tu nombre: [p10_09].
    
    Entonces, escuchas una voz"

    xd "Bienvenido…"

    p10_09 "¿Huh?"

    xd "¿Cómo te llamas?"

    menu:
        "Presentarte":
            "Por un momento, lo piensas hasta tener claro lo único que recuerdas."

label name:

    p10_09 "Me llamo…"

    "Tomas un suspiro antes de presentarte."

    p10_09 "…Me llamo [p10_09]."

    xd "Bienvenido al laboratorio, [p10_09]. De ahora en adelante, este es tu nuevo hogar."
    
    menu:
        "Un momento… ¿Ahora puedo saber quién eres?":
            jump respuesta2

label respuesta2:

    xd "Qué curiosa pregunta…"

    xd "No necesitas saber quién soy."

    menu:

        "¿Qué respondes?"

        "Respuesta lógica":
            p10_09 "Si voy a estar aquí mucho tiempo, debería conocer a quien me habla, supongo."

        "Respuesta directa":
            p10_09 "Quiero verte la cara."
label presentacion:

    xd "Bueno…"

    scene 

    xd "…Si tanto insistes."

    show Stuard serio

    stuard "Soy el comandante Stuard Wishmonger, yo me encargo de los protoripos"

    menu:
        "¿Qué preguntarás?"

        "Entender sobre los prototipos":
            p10_09 "¿Qué es un prototipo?"

label respuestaenigma:
    
    stuard "Ah, los prototipos…"

    stuard "Ya lo entenderás…"

    scene bg black

    "Prototipo 10-09"

    scene bg oficina stuard

    stuard "En fin, ¿le apetece un recorrido por nuestra asociación?"
    stuard "El protocolo indica interactuar con otros prototipos"

    p10_09 "…"
    menu:
        "Tu respuesta será…"

        "Aceptar":
            p10_09 "Bien, vamos con ellos."
            jump avance
        
        "Negarse":
            p10_09 "No sé si quiera conocerlos"
            jump espera
label avance:

    stuard "Entonces, sígame, [p10_09]."

label espera: 

    stuard ""
    # Finaliza el juego:

    return

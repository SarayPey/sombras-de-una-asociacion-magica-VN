# Coloca el código de tu juego en este archivo.

define p10_09   = Character("[Prota]")
define jacob    = Character("Jacob (10-01)")
define ra       = Character("ra (10-02)")
define kaede    = Character("Kaede (10-03)")
define kayne    = Character("Kayne (10-04)")
define stacy    = Character("Stacy (10-05)")
define daisy    = Character("Daisy (10-06)")
define marcus   = Character("Marcus (10-07)")
define cara     = Character("Cara (10-08)")
define jeanette = Character("Cdte Jeanette Balerdoi")
define stuard   = Character("Comandante Stuard Wishmonger")
define kya      = Character("Dra. Kya Calkyuri")
define cameron  = Character("Cdte Cameron Hadarla")
define eider    = Character("Dr. Eider Farhestix")
define nira     = Character("Nira Kireasli")
define xd       = Character("???")
define fallyn   = Character("Fallyn Olssen")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.
    python:
        p10_09 = renpy.input("Ingresa tu nombre", length=32)
        p10_09 = p10_09.strip()
    
        if not p10_09:
            p10_09 = "Ty Rei (10-09)"

    "Acabas de despertar, no sabes dónde estás, es un lugar desconocido para ti.
    
    No recuerdas tu pasado ni qué pasó, lo único que recuerdas es tu nombre: [p10_09].
    
    Entonces, escuchas una voz"

    xd "Bienvenido…"

    p10_09 "¿Huh?"

    xd "¿Cómo te llamas?"

    menu:
        "Presentarte":
            jump respuesta1
label respuesta1:

    p10_09 "Me llamo…"

    "Por un momento, lo piensas hasta tener claro lo único que recuerdas.
    
    Tomas un suspiro antes de presentarte."

    p10_09 "…Me llamo [p10_09]."

    xd "Bienvenido al laboratorio, [p10_09]. De ahora en adelante, este es tu nuevo hogar."
    
    menu:
        "Un momento… ¿Ahora puedo saber quién eres?":
            jump respuesta2

label respuesta2:

    xd "Qué curiosa pregunta…"

    menu:

        "¿Qué digo?"

        "Muéstrate":
            jump respuesta3

        "Quiero verte la cara":
            jump respuesta3
label respuesta3:

    xd "Bueno…"

    scene 

    xd "…Si tanto insistes."

    show Stuard serio

    stuard "Soy el comandante Stuard Wishmonger, yo me encargo de los protoripos"

    menu:
        "¿Qué preguntarás?"

        "¿Prototipos?":
            jump respuesta4

        "¿A qué te refieres con… prototipos?":
            jump respuesta4

label respuesta4:
    
    stuard "Ah, los prototipos…"

    stuard "Ya lo entenderás…"

    scene

    "Prototipo 10-09"

    scene

    stuard "En fin, ¿le apetece un recorrido por nuestra asociación?"

    # Finaiza el juego:

    return

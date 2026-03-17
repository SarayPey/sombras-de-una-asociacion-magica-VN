# Coloca el código de tu juego en este archivo.

# Personajes

define p10_09    = Character("[prota] (10-09)")
define xd        = Character("???")
define jacob     = Character("Jacob (10-01)")
define Naira     = Character("Naira (10-02)")
define kaede     = Character("Kaede (10-03)")
define kayne     = Character("Kayne (10-04)")
define stacy     = Character("Stacy (10-05)")
define daisy     = Character("Daisy (10-06)")
define marcus    = Character("Marcus (10-07)")
define cara      = Character("Cara (10-08)")
define jeanette  = Character("Cdte Jeanette Balerdoi")
define stuard    = Character("Comandante Stuard Wishmonger")
define kya       = Character("Dra. Kya Calkyuri")
define cameron   = Character("Cdte Cameron Hadarla")
define eider     = Character("Dr. Eider Farhestox")
define nira      = Character("Nira Kireasli")
define charlotte = Character("Charlotte")
define fallyn    = Character("Fallyn Olssen")

# Otras variables
define lealtadA = 0 # Lealtad a la asociación, va entre -100 y a 100 y esto define las probabilidades de entregar a los otros prototipos o escapar
define kaedeRemor = 0 # Remordimiento futuro de Kaede, va de 0 a 100 y es parte del final
define jacobConf = 0 # Confianza de Jacob hacia el jugador, va de -100 a 100 y es parte del final

define control2FJacob = -100 # Control de la 2da forma de Jacob, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FNaira = 0 # Control de la 2da forma de Naira, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FKaede = 0 # Control de la 2da forma de Kaede, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FKayne = 0 # Control de la 2da forma de Kayne, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FStacy = 0 # Control de la 2da forma de Stacy, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FDaisy = 0 # Control de la 2da forma de Daisy, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FMarcus = 0 # Control de la 2da forma de Marcus, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2FCara = 0 # Control de la 2da forma de Cara, va de -100 a 100 y esto define las opciones emocionales futuras del personaje.
define control2F = 0 # Control de la 2da forma del jugador, va de -100 a 100 y esto define las opciones emocionales futuras.

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

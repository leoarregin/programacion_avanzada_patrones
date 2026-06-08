# programacion_avanzada_patrones
patrones de diseno


Trabajo práctico: actividad clase 10

Materia: Programación avanzada

Docente: Ingeniero Diego Luparello

Alumnos: 
Pablo Leonardo Arregín
Gonzalo Nicolas Arregín
Mariana Gimenez


Ejercicio 1: Investigar y documentar críticas a los patrones de diseño. Mencione ejemplos concretos. 

Si bien los patrones de diseño son herramientas para resolver problemas recurrentes, su uso incorrecto o desmedido puede perjudicar la calidad del software.
A continuación, se enumeran y explican algunas de las desventajas de aplicar patrones de diseño cuando no se justifique su uso:
Sobreingeniería
Es el riesgo más común y ocurre cuando se aplican patrones para prever problemas futuros que quizás nunca existan, o en situaciones donde una solución simple (lineal o procedimental) era más que suficiente.
El impacto: Se termina diseñando un sistema sobredimensionado, difícil de leer y mantener, solo por el hecho de usar un patrón.
Proliferación de Clases y Código Redundante
Muchos patrones exigen la creación de múltiples interfaces, clases abstractas y subclases adicionales para lograr el desacoplamiento.
El impacto: El volumen de archivos y líneas de código aumenta, por lo que para entender una sola funcionalidad, se podría tener que navegar a través de cinco o seis clases distintas (fábricas, estrategias, adaptadores), lo que fragmenta la lectura del código.
Degradación del Rendimiento (Performance)
Al introducir capas de abstracción, intermediarios o envoltorios (wrappers), el flujo de ejecución se vuelve más largo.
El impacto: Patrones como Proxy, Decorator o Facade añaden llamadas de métodos adicionales y consumo de memoria por la creación de objetos intermedios. En aplicaciones críticas donde cada milisegundo cuenta (como videojuegos o sistemas embebidos), este costo de abstracción puede ser extremadamente perjudicial.
Curva de Aprendizaje Elevada
Para que un patrón funcione como una ventaja comunicativa en el equipo, todos los miembros deben entenderlo a la perfección.
El impacto: Si alguien ajeno al patrón original asume el mantenimiento del código, podría malinterpretar la arquitectura, romper el flujo diseñado o introducir errores graves al intentar forzar modificaciones que no respetan la estructura del patrón.
Falta de Flexibilidad ante Cambios Imprevistos
Los patrones de diseño hacen que el código sea flexible en la dirección que el patrón predice, pero lo vuelven sumamente rígido en cualquier otra dirección.
El impacto: Si el negocio cambia de una manera que el patrón no anticipó, reestructurar esa arquitectura abstracta puede ser muchísimo más costoso que modificar un código más simple y plano.
Duplicación de Esfuerzos con Lenguajes Modernos
Varios de los patrones clásicos fueron diseñados en los años 90 para compensar las limitaciones de lenguajes utilizados en esa época.
El impacto: En lenguajes modernos (como Python o JavaScript), muchas de estas soluciones ya vienen integradas de forma nativa en la sintaxis. Por ejemplo, implementar un patrón Strategy tradicional mediante pesadas jerarquías de clases en Python suele ser innecesario, ya que se pueden pasar funciones directamente como argumentos de primera clase.

En resumen: La regla de oro con los patrones de diseño es justificar su uso. No se deben usar para ver si encajan, sino únicamente cuando el dolor de no usarlos (código acoplado, repetición de lógica) sea mayor que el costo de introducir su complejidad.

Si enfocamos las desventajas de acuerdo al tipo de patrón utilizado, es muy útil analizar cómo afectan de forma específica a cada una de las tres familias clásicas de patrones.
A continuación, se detallan las desventajas particulares por tipo de patrón y se justifica su necesidad en el desarrollo de software actual.
Patrones Creacionales (Singleton, Factory, Builder, etc.)
Desventajas específicas
Ocultamiento de dependencias: Patrones como el Singleton o el Abstract Factory pueden actuar como variables globales encubiertas. Esto hace que las dependencias de una clase no sean evidentes a simple vista, dificultando el rastreo del flujo de datos.
Dificultad en pruebas unitarias (Testing): El Singleton mantiene un estado global mutable. Si un test modifica ese estado, afecta a los tests siguientes, rompiendo el principio de aislamiento de las pruebas unitarias.
Acoplamiento a fábricas: Para evitar acoplarse a un objeto concreto, te terminás acoplando a la fábrica que lo crea. Si la lógica de creación cambia drásticamente, la estructura de la fábrica también sufre.
¿Son necesarios actualmente?
Parcialmente sustituidos, pero conceptualmente vigentes.
Hoy en día, la mayoría de los frameworks modernos resuelven la creación y el ciclo de vida de los objetos mediante la Inyección de Dependencias (DI). Ya no se crea un Singleton a mano; el framework se encarga de instanciar y proveer la clase como una única instancia.
Patrones Estructurales (Adapter, Decorator, Facade, Composite, etc.)
Desventajas específicas
Explosión de envolturas (Wrapper Hell): Patrones como Decorator o Adapter envuelven un objeto dentro de otro. Si se encadenan demasiados decoradores (ej. un lector de archivos, envuelto en un buffer, envuelto en un desencriptador, envuelto en un compresor), el código se vuelve muy difícil de depurar.
Pérdida de identidad del objeto: Al envolver un objeto en un adaptador o decorador, el objeto contenedor tiene una interfaz o tipo distinto al objeto original, lo que puede romper validaciones de tipo estrictas (typeof o isinstance).
¿Son necesarios actualmente?
Sí, son indispensables para la integración de sistemas.
Muchos desarrollos de software consisten en conectar servicios de terceros, APIs, librerías, etc. Los patrones estructurales son el puente que permite que estas piezas encajen sin corromper la lógica central de tu negocio.
Patrones de Comportamiento (Observer, Strategy, State, Command, etc.)
Desventajas específicas
Flujo de control fragmentado y difícil de seguir: Al desacoplar fuertemente la emisión de una acción de su ejecución (como en Observer o Command), el código se vuelve "asincrónico" en su lógica, dificultando el debugging paso a paso.
Fugas de memoria: En el patrón Observer, si un objeto "sujeto" mantiene una lista de "observadores", estos no serán recolectados por el Garbage Collector aunque ya no se usen, a menos que se den de baja explícitamente.
¿Son necesarios actualmente?
Sí, pero su implementación ha evolucionado radicalmente.
Actualmente la Programación Funcional y la Programación Reactiva han absorbido gran parte de estas soluciones de una manera mucho más limpia.
En qué casos sí se justifican:
State: Es fundamental para sistemas que dependen críticamente de máquinas de estado complejas, como el flujo de un carrito de compras (Vacío -> Pendiente de Pago -> Pagado -> Enviado) o la lógica de un bot de atención automatizada. Evita llenar el código de condicionales if/else anidados.
Strategy: Sigue siendo muy útil para intercambiar algoritmos sobre la marcha (por ejemplo, cambiar la estrategia de cálculo de impuestos según el país del usuario), aunque hoy en lenguajes modernos se suele resolver pasando funciones como argumentos en lugar de crear jerarquías completas de clases.
Observer: Es la base de toda la web moderna (arquitecturas orientadas a eventos, o el manejo de estados en frameworks de UI).

Ejercicio 2: En archivo practica10.py

Ejercicio 3: Piense en 3 problemas habituales de su vida diaria en los cuales podría aplicar patrones de diseño. 
El indicador de combustible de un auto es una representación física de uno de los patrones de diseño más famosos del software: el Patrón Observer (Observador). También funciona en la vida real como un Facade (Fachada).
El Indicador como Patrón Observer (El Observador)
En el software, este patrón se usa cuando un objeto (el "Sujeto") cambia de estado y necesita avisar automáticamente a otros objetos (los "Observadores") sin estar fuertemente acoplado a ellos.
El Sujeto (El Tanque): Dentro del tanque de nafta hay un flotante conectado a un sensor que varía la resistencia eléctrica según la altura del líquido. Al tanque no le importa quién está mirando; él solo mide su estado.
El Observador (La Aguja o Pantalla): El indicador del tablero está "suscrito" a los cambios de ese sensor. Cuando el nivel del líquido baja, la señal eléctrica cambia y el indicador se mueve en tiempo real.
El desacoplamiento: Se podría cambiar el tablero analógico de agujas por una pantalla digital. Al tanque no le importa; el nuevo "observador" simplemente se conecta a la misma señal y reinterpreta los datos.
El Indicador como Patrón Facade (Fachada)
Una fachada oculta una complejidad detrás de una interfaz simple.
La complejidad oculta: Saber cuánta nafta queda en un auto en movimiento no es fácil. El líquido se mueve constantemente cuando doblas, aceleras, subís o bajas una pendiente. El sistema del auto tiene que promediar las lecturas, filtrar el "ruido" del movimiento del líquido y estabilizar la señal.
La interfaz simple: Como conductor, no interesa ver la telemetría cruda ni los voltajes del sensor. Solo es necesario una interfaz que nos diga que cantidad de combustible tenemos. El indicador es esa fachada que te ahorra tener que bajarte a medir el nivel de nafta manualmente.
El Patrón Creacional en un vehículo
Siguiendo con el ejemplo del auto y el combustible, vayamos al momento en que el auto se fabrica o se enciende.
El patrón creacional perfecto para este escenario es el Abstract Factory (Fábrica Abstracta) combinado con el patrón Builder (Constructor).
En la automotriz que fabrica vehículos: un auto económico urbano (con tablero analógico, agujas físicas y un tanque de combustible chico de 40 litros) y un auto de alta gama (con pantallas digitales, telemetría avanzada y un tanque de 70 litros).
Aquí es donde entran los patrones creacionales para resolver el problema de cómo crear el indicador y el tanque correcto para cada auto sin que el sistema se entere de los detalles.
1. Abstract Factory: Familias de Componentes Compatibles
El patrón Abstract Factory permite crear familias de objetos relacionados (el Tanque y su Indicador) sin especificar sus clases concretas. Garantiza que el indicador en el tablero sea compatible con el tipo de tanque que lleva el auto.
La Fábrica de Autos Económicos (FabricaAutoUrbano): Cuando el sistema le pide componentes, esta fábrica sabe que tiene que instanciar un TanqueNafta40L y una AgujaAnaloga. Ambos están hechos para trabajar juntos a un voltaje específico.
La Fábrica de Autos Premium (FabricaAutoAltaGama): Esta fábrica crea un TanqueNafta70L y un IndicadorDigitalPantalla.
El sistema central del auto solo interactúa con las interfaces genéricas (Tanque e Indicador). No le importa si son analógicos o digitales; la fábrica se encargó de crear la pareja compatible.
2. Builder: El Proceso de Ensamblaje Paso a Paso
Mientras que la Fábrica te da las piezas correctas, el patrón Builder se encarga del orden y la lógica del ensamblaje complejo del auto, paso a paso.
Para que el indicador de combustible funcione (el Observer mencionado anteriormente), alguien tiene que conectar el indicador al tanque en el momento de la creación.
El proceso de construcción (Director) sigue estos pasos estructurados:
construirChasis()
instalarTanque() (obtenido de la Abstract Factory)
instalarTablero() (obtenido de la Abstract Factory)
conectarIndicadorAlTanque() (aquí el Builder hace el "subscribe" del Observer)
En Resumen
Abstract Factory: Asegura que si el auto lleva un tanque de nafta moderno, el indicador del tablero sea el digital y no una aguja vieja que no entienda la señal.
Builder: Se encarga de poner el tanque en su lugar, el tablero en el suyo, y "cablear" el indicador al sensor del tanque para que el patrón Observer pueda funcionar.

Ejercicio 4: Los patrones de diseño suelen poseer distintos nombres o denominaciones. Busque y arme una tabla con los posibles distintos nombres usados. 

Nombre más usado
Tipo
Sinónimos / Nombres Alternativos
Abstract Factory
Creacional
Fábrica Abstracta, Kit
Builder
Creacional
Constructor, Director-Builder
Factory Method
Creacional
Método Fábrica, Virtual Constructor (Constructor Virtual)
Singleton
Creacional
Instancia Única, Solitario
Adapter
Estructural
Adaptador, Wrapper (Envoltorio)
Bridge
Estructural
Puente, Handle and Body (Manejador y Cuerpo)
Composite
Estructural
Objeto Compuesto, Componente
Decorator
Estructural
Decorador, Wrapper (Envoltorio), Smart Proxy
Facade
Estructural
Fachada, Front-end
Flyweight
Estructural
Peso Ligero, Cache-efficient object
Proxy
Estructural
Procurador, Representante, Surrogate (Sustituto)
Chain of Responsibility
Comportamiento
Cadena de Responsabilidad, CoR, Pasamanos
Command
Comportamiento
Comando, Action (Acción), Transaction, Token
Interpreter
Comportamiento
Intérprete
Iterator
Comportamiento
Iterador, Cursor
Mediator
Comportamiento
Mediador, Intermediario, Hub
Memento
Comportamiento
Recuerdo, Historial, Token, Snapshot (Instantánea)
Observer
Comportamiento
Observador, Dependents, Publish-Subscribe (Pub-Sub)
State
Comportamiento
Estado, Objects for States (Objetos para Estados)
Strategy
Comportamiento
Estrategia, Policy (Política)
Template Method
Comportamiento
Método Plantilla
Visitor
Comportamiento
Visitante



Ejercicio 5: ¿Qué son los antipatrones de diseño? Ejemplifique algunos casos. 
Los antipatrones de diseño son exactamente lo contrario de los patrones de diseño y pueden definirse como soluciones que, a primera vista, parecen buenas ideas para resolver el problema, pero que a mediano o largo plazo generan más problemas, caos y costos técnicos de los que solucionan. El término sirve para ponerle nombre a errores frecuentes que se cometen en el desarrollo de software.
Antipatrones de Desarrollo (En el Código)
A. The Blob o God Object (El Objeto Dios)
¿Qué es?: Es el enemigo natural del principio S de SOLID (Responsabilidad Única). Ocurre cuando una sola clase o módulo crece descontroladamente y asume casi toda la lógica del sistema.
El síntoma: Un archivo que tiene 5.000 líneas de código. Cada vez que alguien quiere tocar algo, termina modificando ese mismo archivo.
Por qué es malo: Es una pesadilla para el mantenimiento. Romper algo en una punta del archivo puede desactivar una funcionalidad completamente inconexa en la otra punta.
B. Spaghetti Code (Código Espagueti)
¿Qué es?: Es un código que carece de una estructura clara, donde el flujo del programa salta de un lado a otro de forma totalmente enredada.
El síntoma: Funciones gigantescas, saltos condicionales infinitos, variables globales que cambian de valor mágicamente a mitad de camino y una falta total de modularidad.
Por qué es malo: Nadie entiende cuál es el camino que sigue la ejecución de una punta a la otra.
Antipatrones de Arquitectura (En la Estructura)
A. Golden Hammer (El Martillo de Oro)
¿Qué es?: Ocurre cuando se intenta aplicar un patrón a absolutamente todo, incluso donde no tiene ningún sentido.
Ejemplo real: Usar una base de datos de Grafos hipercompleja solo para hacer un registro de usuarios simple.
Por qué es malo: Añade una complejidad innecesaria (sobreingeniería), aumenta los costos y ralentiza el desarrollo solo por usar una herramienta específica.
B. Lasagna Architecture (Arquitectura Lasaña)
¿Qué es?: Es el exceso de abstracción.
El síntoma: Para hacer un cambio simple, como agregar un campo "teléfono" a un usuario, es necesario modificar la capa de interfaz, la capa de control, la capa de servicio, la capa de mapeo, la capa de repositorio y la capa de base de datos.
Por qué es malo: Destruye el rendimiento del equipo y del software. El exceso de "pasamanos" entre capas vuelve al código rígido y lento.
Antipatrones Organizacionales o de Gestión
A. Analysis Paralysis (Parálisis por Análisis)
¿Qué es?: Ocurre cuando se pasa tanto tiempo planificando, modelando diagramas UML, analizando riesgos y buscando la "perfección arquitectónica" que nunca se empieza a escribir código real.
Por qué es malo: En el software, el mercado y los requerimientos cambian rápido. Para cuando el equipo termina de planificar la arquitectura perfecta, el problema original ya cambió.
B. Death By Planning (Muerte por Planificación) / Cargo Cult Programming
¿Qué es?: Copiar rituales o metodologías de desarrollo (como Scrum, Kanban o patrones de diseño) de forma ciega y superficial, esperando que "mágicamente" resuelvan los problema, sin entender la lógica subyacente de por qué se usan.
Ejemplo real: Pasar tres horas al día en reuniones de Daily Standup discutiendo minucias en lugar de sentarse a resolver la arquitectura trabada de la aplicación.

Ejercicio 6: Investigue el uso de otras buenas prácticas, como por ejemplo SOLID 
SOLID es un acrónimo que representa cinco principios fundamentales del diseño de software orientado a objetos, recopilados por Robert C. Martin, y cuyo objetivo principal es ayudar a escribir código limpio, flexible, fácil de mantener y de extender en el tiempo.
Significado de cada letra, explicado de forma simple:
S - Single Responsibility Principle (Principio de Responsabilidad Única)
"Una clase debería tener una única razón para cambiar."
La idea: Cada clase, módulo o función debe encargarse de una sola cosa. Si una clase hace demasiadas cosas, si es necesario modificar algo, se corre el riesgo de romper otra funcionalidad.
O - Open/Closed Principle (Principio de Abierto/Cerrado)
"El software debería estar abierto para la extensión, pero cerrado para la modificación."
La idea: Se debería poder agregar nuevas funcionalidades al código sin tener que modificar el código ya existente y que funciona. Esto se logra usando abstracciones (interfaces o herencia).
L - Liskov Substitution Principle (Principio de Sustitución de Liskov)
"Si una clase B hereda de una clase A, se debería poder usar B en cualquier lugar donde uses A sin que el sistema se rompa."
La idea: Las clases hijas deben respetar el comportamiento esperado de las clases padres. La subclase debe ser un sustituto perfecto de la superclase.
I - Interface Segregation Principle (Principio de Segregación de Interfaces)
"Es mejor tener muchas interfaces específicas que una sola interfaz de propósito general."
La idea: Ninguna clase debería ser obligada a implementar métodos o contratos que no necesita usar. Es mejor tener "contratos" pequeños y modulares.
D - Dependency Inversion Principle (Principio de Inversión de Dependencias)
"Depende de las abstracciones, no de las clases concretas."
La idea: Los módulos de alto nivel no deben depender de los detalles de bajo nivel (la base de datos, una librería externa, un sensor). Ambos deben depender de interfaces abstractas. Esto desacopla el código por completo.
¿Por qué importan?
Al principio, aplicar SOLID puede parecer que te hace escribir "más código" (más interfaces, más clases pequeñas), pero a mediano y largo plazo ahorra cientos de horas de trabajo innecesario. Un sistema diseñado con SOLID puede cambiar piezas sin necesidad de cambiar toda la estructura para que siga funcionando.

Ejemplo: el diseño de un motor de un vehículo para un videojuego de simulación de Carreras de Fórmula X-CAR.
En este universo, las escuderías pueden instalar componentes experimentales en sus vehículos: motores de fusión cuántica, propulsores de antimateria o escudos electromagnéticos que alteran las físicas en plena carrera.
Aplicando el diseño SOLID permite crear un ecosistema caótico y futurista de forma ultra-limpia en Python.
from abc import ABC, abstractmethod
import random
# 1. RESPONSABILIDAD ÚNICA (S)
# La clase VehiculoCarrera SOLO gestiona el estado físico actual del auto.
# No calcula el desgaste de los neumáticos ni sabe cómo renderizar los gráficos.
class VehiculoCarrera:
    def __init__(self, escuderia: str, piloto: str):
        self.escuderia = escuderia
        self.piloto = piloto
        self.velocidad_base = 180  # km/h base en un mundo cyberpunk
        self.energia_disponible = 100.0

    def obtener_estado_critico(self) -> dict:
        return {
            "piloto": self.piloto,
            "escuderia": self.escuderia,
            "energia": self.energia_disponible
        }
# 2. ABIERTO/CERRADO (O) e INVERSIÓN DE DEPENDENCIAS (D)
# Definimos la abstracción para cualquier "Módulo de Rendimiento" (Mod).
# El motor del juego está CERRADO a modificaciones, pero ABIERTO a que 
# inventemos cualquier Mod loco en el futuro.

class ModuloRendimiento(ABC):
    @abstractmethod
    def aplicar_efecto(self, vehiculo: VehiculoCarrera) -> float:
        """Devuelve el modificador de velocidad resultante."""
        pass

class ModuloTelemetria(ABC):
    @abstractmethod
    def reportar(self, datos: dict):
        pass

# 3. SUSTITUCIÓN DE LISKOV (L)
# Cualquier módulo experimental que herede de ModuloRendimiento debe poder
# usarse en el auto sin romper la simulación, respetando el contrato.

class PropulsorHiperducto(ModuloRendimiento):
    """Un mod tradicional: aumenta mucho la velocidad si hay energía."""
    def aplicar_efecto(self, vehiculo: VehiculoCarrera) -> float:
        if vehiculo.energia_disponible > 20:
            vehiculo.energia_disponible -= 15
            return vehiculo.velocidad_base * 1.5  # +50% de velocidad
        return vehiculo.velocidad_base

class MotorFusionCuantica(ModuloRendimiento):
    """Un mod inestable: velocidad altamente variable basado en física cuántica."""
    def aplicar_efecto(self, vehiculo: VehiculoCarrera) -> float:
        # Altera el estado de la energía de forma impredecible
        vehiculo.energia_disponible -= random.uniform(5, 25)
        factor_cuantico = random.choice([0.8, 1.2, 2.0])  # ¡Puede duplicar la velocidad o frenarlo!
        return vehiculo.velocidad_base * factor_cuantico

# 4. SEGREGACIÓN DE INTERFACES (I)
# En lugar de tener una interfaz gigante "SistemaDeCarreraUniversal", separamos
# los contratos. Las escuderías de IA pura no necesitan pantallas físicas.

class InterfazHolograficaPiloto(ModuloTelemetria):
    """Proyecta datos en el casco del piloto humano."""
    def reportar(self, datos: dict):
        print(f"🔮 [Holo-HUD] Piloto {datos['piloto']} -> Energía Sintética: {datos['energia']:.1f}%")

class TransmisorBoxesIA(ModuloTelemetria):
    """Envía ráfagas de datos binarios directamente a la IA de la escudería en boxes."""
    def reportar(self, datos: dict):
        print(f"🤖 [IA-Link] {datos['escuderia'].upper()} >> Telemetría procesada en la nube cuántica.")

# EL ORQUESTADOR: El Motor de Simulación (Physics Engine)
class MotorSimulacion:
    # Dependemos puramente de abstracciones (D). El motor no sabe qué tecnologías
    # inventaron los ingenieros de las escuderías, solo sabe cómo ejecutarlas.
    def __init__(self, mod_rendimiento: ModuloRendimiento, telemetria: ModuloTelemetria):
        self.mod_rendimiento = mod_rendimiento
        self.telemetria = telemetria

    def simular_vuelta(self, vehiculo: VehiculoCarrera):
        # 1. Calcula la velocidad combinando el estado del vehículo y su Mod experimental
        velocidad_final = self.mod_rendimiento.aplicar_efecto(vehiculo)
        
        print(f"🏎️  El auto de {vehiculo.piloto} cruza el sector de alta velocidad a {velocidad_final:.1f} km/h!")
        
        # 2. Despacha la telemetría a través del canal segregado correspondiente
        datos_actuales = vehiculo.obtener_estado_critico()
        self.telemetria.reportar(datos_actuales)

El Caos en Acción: Configurando la Parrilla de Salida
Podemos crear dos escuderías con filosofías tecnológicas radicalmente opuestas y el código las procesará de forma idéntica sin un solo if/else estructural.

# Creamos los corredores del año 2026
auto_lem = VehiculoCarrera(escuderia="Cyber-Oracle Racing", piloto="Lem Arregín")
auto_android = VehiculoCarrera(escuderia="Neural-Consult", piloto="T-800")

print("--- CONFIGURACIÓN ESCUDERÍA 1: HÍBRIDA HUMANA ---")
# El humano Lem usa un motor cuántico inestable pero una interfaz visual en su casco
simulador_humano = MotorSimulacion(
    mod_rendimiento=MotorFusionCuantica(),
    telemetria=InterfazHolograficaPiloto()
)
simulador_humano.simular_vuelta(auto_lem)

print("\n--- CONFIGURACIÓN ESCUDERÍA 2: IA PURA ---")
# El androide usa un propulsor lineal hiperducto y reporta directo a la colmena de IA
simulador_ia = MotorSimulacion(
    mod_rendimiento=PropulsorHiperducto(),
    telemetria=TransmisorBoxesIA()
)
simulador_ia.simular_vuelta(auto_android)
Si mapeamos los cinco principios de SOLID usando exactamente las piezas y los actores de nuestra simulación de carreras. Así es como cada regla domina el caos en la pista:
Single Responsibility Principle
En la pista: La clase VehiculoCarrera.
La lógica: El auto solo se encarga de conocer su estado físico actual: cuánta energía le queda, quién lo maneja y a qué escudería pertenece. El auto no sabe cómo calcular las complejas leyes de la física cuántica, ni tampoco sabe cómo transmitir los datos por radio a los boxes.
Por qué importa: Si el día de mañana el equipo de desarrollo decide cambiar la forma en que se transmite la telemetría (por ejemplo, encriptando los datos), el código del auto no se toca. Evitamos que un cambio en las comunicaciones arruine el motor del auto.
Open/Closed Principle
En la pista: La interfaz ModuloRendimiento.
La lógica: El motor de simulación está cerrado a modificaciones (no queremos tocar su código base cada vez que una escudería invente algo nuevo porque podríamos generar un bug que rompa todo el juego). Sin embargo, está abierto a la extensión a través de los módulos.
Por qué importa: Si los ingenieros de la escudería diseñan un componente ultra disruptivo como un Generador de Agujeros de Gusano, simplemente crean una nueva clase que herede de ModuloRendimiento. El simulador central lo aceptará en la pista sin haber tenido que modificar una sola línea de su propio código.
Liskov Substitution Principle
En la pista: PropulsorHiperducto y MotorFusionCuantica.
La lógica: Ambos son módulos de rendimiento y ambos pueden sustituir a la clase madre (ModuloRendimiento) sin que el simulador explote. El simulador espera que cualquier módulo reciba el auto, consuma energía y devuelva la velocidad final.
Por qué importa: El MotorFusionCuantica puede ser completamente caótico e impredecible por dentro (física cuántica, azar, etc.), pero respeta el contrato. No hace cosas raras como devolver un texto en lugar de un número o colgar la ejecución. El simulador los trata a ambos exactamente por igual, garantizando que la carrera continúe.
Interface Segregation Principle
En la pista: ModuloTelemetria separado de otras posibles interfaces complejas.
La lógica: No creamos una interfaz gigante llamada SistemaUniversalDelAuto que obligue a todos los componentes a implementar métodos de audio, video, telemetría y dirección al mismo tiempo. Separamos los contratos de forma atómica.
Por qué importa: Un androide que corre para la escudería Patán-Team no tiene ojos humanos, por lo que su auto no necesita procesar la InterfazHolograficaPiloto. Al estar las interfaces segregadas, el auto de la IA puede usar solo el TransmisorBoxesIA sin verse obligado a implementar funciones de renderizado visual que no necesita.
Dependency Inversion Principle
En la pista: El MotorSimulacion.
La lógica: El motor de físicas (un módulo de alto nivel) no depende de tecnologías concretas de bajo nivel. No dice: "Yo solo funciono si me das un motor de combustión tradicional". En su lugar, el motor dice: "Yo solo dependo de la abstracción ModuloRendimiento".
Por qué importa: Al "invertir" la dependencia y hacer que todo pase a través de un enchufe conceptual (la interfaz abstracta), logramos un desacoplamiento absoluto. El simulador se vuelve inmortal: es capaz de correr una carrera con autos antiguos con carburador, con naves espaciales o con motores de fusión cuántica, porque solo le interesan los contratos, no los cables internos de cada tecnología.

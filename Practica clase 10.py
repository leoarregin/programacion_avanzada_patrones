from __future__ import annotations
import os

def limpiar_pantalla():
    # Si es Windows usa 'cls', si es Linux/Mac usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()

# Acá va el resto de la ejecución de tus patrones...
# Patrón Creacional: Builder
# Desarrollando el backend de un simulador de carreras, será necesario 
# crear objetos complejos como AutoDeCarrera. Un auto tiene motor, neumáticos,
# alerones, configuraciones de suspensión, etc. 
# Al usar un constructor tradicional (__init__), tendríamos una lista 
# gigante de argumentos (de los cuales, muchos de ellos podrían ser opcionales). 
# El Builder permite armar el auto paso a paso de forma limpia.

class AutoDeCarrera:
    def __init__(self):
        self.motor = None
        self.neumaticos = None
        self.aleron_trasero = False
        self.configuracion_E_RS = "Estándar"

    def __str__(self):
        return f"Auto con: Motor {self.motor}, Ruedas {self.neumaticos}, Alerón: {self.aleron_trasero}, ERS: {self.configuracion_E_RS}"

# El Builder encapsula la construcción paso a paso
class AutoBuilder:
    def __init__(self):
        self.auto = AutoDeCarrera()
        
    def reset(self):
        self.auto = AutoDeCarrera()
        return self
        
    def configurar_motor(self, tipo_motor: str):
        self.auto.motor = tipo_motor
        return self  # Retornamos self para permitir encadenamiento de métodos
        
    def configurar_neumaticos(self, tipo_goma: str):
        self.auto.neumaticos = tipo_goma
        return self
        
    def añadir_aleron_alta_carga(self):
        self.auto.aleron_trasero = True
        return self
        
    def configurar_ers(self, modo: str):
        self.auto.configuracion_E_RS = modo
        return self
        
    def construir(self) -> AutoDeCarrera:
        auto_finalizado = self.auto
        self.reset()  # Dejamos listo el builder para el próximo auto
        return auto_finalizado

# --- Uso en la aplicación ---
builder = AutoBuilder()

# Configuración para un circuito de alta velocidad (ej. Monza): Poca carga aerodinámica
auto_monza = (builder.configurar_motor("V6 Turbo Híbrido")
                     .configurar_neumaticos("Blandos")
                     .configurar_ers("Hotlap")
                     .construir())

# Configuración para lluvia
auto_lluvia = (builder.configurar_motor("V6 Turbo Híbrido")
                     .configurar_neumaticos("Lluvia Extrema")
                     .añadir_aleron_alta_carga()
                     .construir())

print(auto_monza)
print(auto_lluvia)

input("\nPresione [ENTER] para continuar con los ejemplos de patrones estructurales y de comportamiento...")
limpiar_pantalla()

#Patrón Estructural: Adapter
#En una aplicación que procesa cobros, inicialmente se usaba una pasarela de pagos local
# (PagoLocal), que tiene un método llamado ejecutar_cobro(). Ahora el negocio necesita 
# integrar un SDK internacional (como Stripe), pero su clase viene con un método totalmente
# distinto: authorize_card() y capture_charge(). Para no cambiar todo el código existente 
# que ya sabe usar ejecutar_cobro, se crea un Adapter.
# Interfaz esperada por nuestra aplicación (Contrato)
class ProcesadorPagosTarget:
    def ejecutar_cobro(self, monto: float):
        raise NotImplementedError

# Servicio viejo o actual
class PagoLocal(ProcesadorPagosTarget):
    def ejecutar_cobro(self, monto: float):
        print(f"Cobrando ${monto} a través de la pasarela local.")

# Servicio nuevo/externo con interfaz incompatible (Adaptee)
class StripeSDK:
    def authorize_card(self, amount_in_cents: int):
        print(f"Stripe: Tarjeta autorizada por {amount_in_cents} centavos.")
        
    def capture_charge(self):
        print("Stripe: Cargo capturado con éxito.")

# El Adaptador une ambos mundos
class StripeAdapter(ProcesadorPagosTarget):
    def __init__(self, stripe_sdk: StripeSDK):
        self.stripe = stripe_sdk

    def ejecutar_cobro(self, monto: float):
        # El adaptador traduce el método y adapta los datos (pesos a centavos)
        centavos = int(monto * 100)
        self.stripe.authorize_card(centavos)
        self.stripe.capture_charge()

# --- Uso en la aplicación ---
def procesar_pedido_carrito(procesador: ProcesadorPagosTarget, total: float):
    # A la aplicación no le importa qué pasarela hay detrás, la interfaz es la misma
    procesador.ejecutar_cobro(total)

# Funciona con el sistema viejo
pasarela_vieja = PagoLocal()
procesar_pedido_carrito(pasarela_vieja, 150.50)

# Funciona con el sistema nuevo gracias al Adapter
sdk_stripe = StripeSDK()
pasarela_nueva = StripeAdapter(sdk_stripe)
procesar_pedido_carrito(pasarela_nueva, 150.50)

input("\nPresione [ENTER] para continuar con el ejemplo del patrón de comportamiento State...")
limpiar_pantalla()

# Patrón de Comportamiento: State
# En un sistema de turnos de una veterinaria, un turno tiene un ciclo de vida 
# que varía en el tiempo: empieza como Solicitado, puede pasar a Confirmado, luego 
# a En Consulta, y finalmente a Finalizado (o Cancelado). Al meter toda esta lógica 
# en una sola clase mediante condicionales, se termina con un código lleno de 
# if estado == "Solicitado" and accion == "cancelar": .... El patrón State encapsula }
# el comportamiento de cada estado en su propia clase.

# Interfaz base para los estados
class EstadoTurno:
    def confirmar(self, turno: Turno):
        raise NotImplementedError("Acción no permitida en este estado.")
        
    def iniciar_consulta(self, turno: Turno):
        raise NotImplementedError("Acción no permitida en este estado.")
        
    def finalizar(self, turno: Turno):
        raise NotImplementedError("Acción no permitida en este estado.")

# Concreción de Estados
class EstadoSolicitado(EstadoTurno):
    def confirmar(self, turno: Turno):
        print("Turno confirmado. Se envía WhatsApp de notificación al dueño de la mascota.")
        turno.set_estado(EstadoConfirmado())

class EstadoConfirmado(EstadoTurno):
    def iniciar_consulta(self, turno: Turno):
        print("El veterinario ha iniciado la atención de la mascota.")
        turno.set_estado(EstadoEnConsulta())

class EstadoEnConsulta(EstadoTurno):
    def finalizar(self, turno: Turno):
        print("Consulta finalizada. Se genera la orden de facturación e historial médico.")
        turno.set_estado(EstadoFinalizado())

class EstadoFinalizado(EstadoTurno):
    # Ya no se pueden realizar acciones sobre un estado finalizado
    pass

# La clase Contexto (el Turno)
class Turno:
    def __init__(self, paciente: str):
        self.paciente = paciente
        self._estado = EstadoSolicitado()  # Estado inicial

    def set_estado(self, estado: EstadoTurno):
        self._estado = estado

    # Delegación de comandos al estado actual
    def confirmar_turno(self):
        self._estado.confirmar(self)

    def iniciar_atencion(self):
        self._estado.iniciar_consulta(self)

    def finalizar_turno(self):
        self._estado.finalizar(self)

# --- Uso en la aplicación ---
turno_firulais = Turno("Firulais (Perro)")

# Flujo feliz
turno_firulais.confirmar_turno()
turno_firulais.iniciar_atencion()
turno_firulais.finalizar_turno()

print("\n--- Intento de romper las reglas de negocio ---")
# Si intentamos iniciar atención de un turno que ya finalizó, fallará limpiamente por diseño
try:
    turno_firulais.iniciar_atencion()
except NotImplementedError as e:
    print(f"Error esperado: {e}")

input("\nPresione [ENTER] para finalizar la práctica con ejemplo de solid...")
limpiar_pantalla()

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

# Creamos los corredores del año 2026
auto_lem = VehiculoCarrera(escuderia="Cyber-Oracle Racing", piloto="Lem Verstappen")
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

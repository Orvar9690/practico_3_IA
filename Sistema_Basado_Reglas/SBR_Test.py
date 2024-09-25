import time  # Importamos la librería de tiempo para medir el tiempo de respuesta


class SistemaDiagnosticoMedico:
    def __init__(self):
        # Inicializa las reglas del sistema y la estructura de datos para pacientes
        self.reglas = [
            ({"fiebre alta", "dolor de pecho", "tos persistente"}, "Neumonía", 3),
            ({"dificultad respiratoria", "sibilancias", "tos"}, "Asma", 3),
            ({"sed excesiva", "fatiga", "visión borrosa"}, "Diabetes", 2),
            ({"fiebre alta", "rigidez de nuca", "dolor de cabeza"}, "Meningitis", 3),
            ({"diarrea", "dolor abdominal", "fiebre leve"}, "Gastroenteritis", 2)
        ]
        self.pacientes = {}

    def agregar_paciente(self, nombre):
        # Agrega un nuevo paciente al sistema si aún no existe
        if nombre not in self.pacientes:
            self.pacientes[nombre] = {"síntomas": set(), "historial_diagnosticos": []}

    def agregar_sintoma(self, nombre, sintoma):
        # Añade un síntoma al registro de un paciente existente
        if nombre in self.pacientes:
            self.pacientes[nombre]["síntomas"].add(sintoma)

    def evaluar_reglas(self, nombre):
        # Evalúa las reglas del sistema contra los síntomas del paciente especificado
        start_time = time.time()  # Tiempo de inicio
        diagnosticos = set()
        if nombre in self.pacientes:
            for sintomas, diagnostico, urgencia in self.reglas:
                if sintomas.issubset(self.pacientes[nombre]["síntomas"]):
                    diagnosticos.add((diagnostico, urgencia))
            self.pacientes[nombre]["historial_diagnosticos"].append(diagnosticos)
        end_time = time.time()  # Tiempo de finalización
        tiempo_respuesta = end_time - start_time
        return diagnosticos, tiempo_respuesta

    def obtener_historial(self, nombre):
        # Devuelve el historial completo de diagnósticos de un paciente
        return self.pacientes[nombre]["historial_diagnosticos"] if nombre in self.pacientes else []


# Creación del sistema y prueba de funcionamiento
sistema = SistemaDiagnosticoMedico()
sistema.agregar_paciente("Test")
sistema.agregar_sintoma("Test", "fiebre alta")
sistema.agregar_sintoma("Test", "dolor de pecho")
sistema.agregar_sintoma("Test", "tos persistente")

# Evaluamos los síntomas y obtenemos diagnósticos junto con el tiempo de respuesta
diagnosticos, tiempo_respuesta = sistema.evaluar_reglas("Test")
print(f"Diagnósticos obtenidos: {diagnosticos}")
print(f"Tiempo de respuesta: {tiempo_respuesta:.4f} segundos")

# Para pruebas de precisión, se pueden definir casos de prueba adicionales
casos_prueba = [
    ("Test", {"fiebre alta", "dolor de pecho", "tos persistente"}, "Neumonía"),
    # Agregar más casos según sea necesario
]

# Ejecutamos pruebas de precisión
for nombre, sintomas, diagnostico_esperado in casos_prueba:
    sistema.agregar_paciente(nombre)
    for sintoma in sintomas:
        sistema.agregar_sintoma(nombre, sintoma)
    diagnosticos_obtenidos, _ = sistema.evaluar_reglas(nombre)
    es_correcto = diagnostico_esperado in [diag[0] for diag in diagnosticos_obtenidos]
    print(f"Caso {nombre} - Correcto: {es_correcto}")

import time
from datetime import datetime

class SistemaDiagnosticoMedico:
    def __init__(self):
        # Reglas para diagnósticos: cada elemento es una tupla que contiene un conjunto de síntomas,
        # el nombre del diagnóstico asociado y su nivel de urgencia.
        self.reglas = [
            ({"fiebre alta", "dolor de pecho", "tos persistente"}, "Neumonía", 3),
            ({"dificultad respiratoria", "sibilancias", "tos"}, "Asma", 3),
            ({"sed excesiva", "fatiga", "visión borrosa"}, "Diabetes", 2),
            ({"fiebre alta", "rigidez de nuca", "dolor de cabeza"}, "Meningitis", 3),
            ({"diarrea", "dolor abdominal", "fiebre leve"}, "Gastroenteritis", 2)
        ]
        self.pacientes = {}  # Diccionario para almacenar información sobre los pacientes.

    def agregar_paciente(self, nombre):
        # Añade un nuevo paciente al sistema con un conjunto vacío de síntomas y un historial de diagnósticos.
        if nombre not in self.pacientes:
            self.pacientes[nombre] = {"síntomas": set(), "historial_diagnosticos": []}

    def agregar_sintoma(self, nombre, sintoma):
        # Agrega un síntoma al conjunto de síntomas del paciente especificado.
        if nombre in self.pacientes:
            self.pacientes[nombre]["síntomas"].add(sintoma)

    def evaluar_reglas(self, nombre):
        # Evalúa los síntomas del paciente contra las reglas de diagnóstico y registra el resultado.
        start_time = time.time()  # Marca el inicio del proceso de evaluación.
        diagnosticos = set()
        if nombre in self.pacientes:
            for sintomas, diagnostico, urgencia in self.reglas:
                if sintomas.issubset(self.pacientes[nombre]["síntomas"]):
                    diagnosticos.add((diagnostico, urgencia))
            # Añade el diagnóstico y la fecha actual al historial del paciente.
            self.pacientes[nombre]["historial_diagnosticos"].append({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "diagnosticos": diagnosticos
            })
        end_time = time.time()  # Marca el fin del proceso de evaluación.
        tiempo_respuesta = end_time - start_time  # Calcula la duración del proceso de evaluación.
        return diagnosticos, tiempo_respuesta

sistema = SistemaDiagnosticoMedico()

# Procesa la simulación de diagnóstico para una lista de pacientes con síntomas específicos.
pacientes_prueba = [
    ("Paciente 1", {"fiebre alta", "dolor de pecho", "tos persistente"}),  # Probable caso de Neumonía
    ("Paciente 2", {"dificultad respiratoria", "sibilancias", "tos"}),      # Probable caso de Asma
    ("Paciente 3", {"sed excesiva", "fatiga", "visión borrosa"}),           # Probable caso de Diabetes
    ("Paciente 4", {"fiebre alta", "rigidez de nuca", "dolor de cabeza"}),  # Probable caso de Meningitis
    ("Paciente 5", {"diarrea", "dolor abdominal", "fiebre leve"}),          # Probable caso de Gastroenteritis
]

for nombre, sintomas in pacientes_prueba:
    sistema.agregar_paciente(nombre)  # Registra cada paciente en el sistema.
    for sintoma in sintomas:
        sistema.agregar_sintoma(nombre, sintoma)  # Añade los síntomas registrados para cada paciente.
    diagnosticos, tiempo_respuesta = sistema.evaluar_reglas(nombre)  # Evalúa los síntomas del paciente.
    print(f"{nombre} - Diagnósticos actuales: {diagnosticos}")  # Muestra los diagnósticos encontrados.
    print(f"Tiempo de respuesta: {tiempo_respuesta:.4f} segundos")  # Muestra el tiempo que tomó el diagnóstico.
    print(60*"-")  # Separador para mejorar la legibilidad de los resultados.

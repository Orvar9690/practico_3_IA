# Hechos sobre los síntomas del paciente
paciente = "ana"
hechos = {
    "dolor_estomacal": True,
    "acidez": True,
    "náuseas": True,
    "vómitos": False,
    "diarrea": False,
    "hinchazón": False
}


# Función para realizar el diagnóstico basado en los hechos
def diagnostico(hechos):
    if hechos["dolor_estomacal"] and hechos["acidez"] and hechos["náuseas"]:
        print(f"{paciente} podría tener gastritis.")
    elif hechos["dolor_estomacal"] and hechos["vómitos"]:
        print(f"{paciente} podría tener una úlcera gástrica.")
    elif hechos["náuseas"] and hechos["diarrea"] and hechos["vómitos"]:
        print(f"{paciente} podría tener gastroenteritis.")
    else:
        print(f"No se pudo determinar una enfermedad clara para {paciente}.")


# Aplicamos las reglas al conjunto de hechos del paciente
diagnostico(hechos)

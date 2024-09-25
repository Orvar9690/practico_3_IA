
# Sistema de Diagnóstico Médico Basado en Reglas

## Descripción General
Este sistema utiliza reglas basadas en síntomas para diagnosticar enfermedades. Maneja múltiples pacientes y mantiene un historial de sus diagnósticos.

## Clase `SistemaDiagnosticoMedico`

### Métodos

#### `__init__(self)`
Inicializa el sistema con un conjunto de reglas predefinidas y una estructura de datos para los pacientes.

#### `agregar_paciente(self, nombre)`
Añade un nuevo paciente al sistema si no existe, preparando un espacio para registrar sus síntomas y diagnósticos.

#### `agregar_sintoma(self, nombre, sintoma)`
Registra un síntoma para un paciente existente, actualizando la base de hechos que se usará para futuras inferencias.

#### `evaluar_reglas(self, nombre)`
Evalúa las reglas para un paciente basado en sus síntomas actuales y añade los diagnósticos al historial del paciente.

#### `obtener_historial(self, nombre)`
Recupera el historial completo de diagnósticos para un paciente, proporcionando una vista de todos los diagnósticos anteriores.

## Ejemplo de Uso

```python
sistema = SistemaDiagnosticoMedico()
sistema.agregar_paciente("Alice")
sistema.agregar_sintoma("Alice", "fiebre alta")
sistema.agregar_sintoma("Alice", "dolor de pecho")
sistema.agregar_sintoma("Alice", "tos persistente")
diagnosticos = sistema.evaluar_reglas("Alice")
print(f"Diagnósticos para Alice: {diagnosticos}")
historial = sistema.obtener_historial("Alice")
print(f"Historial de Alice: {historial}")
```

Este ejemplo muestra cómo configurar un paciente, registrar síntomas y obtener un diagnóstico utilizando el sistema.
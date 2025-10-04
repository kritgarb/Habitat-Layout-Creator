"""
Constantes e configurações NASA para o Habitat Layout Creator
"""

# Padrões NASA
MIN_NHV_PER_PERSON = 25  # m³ por pessoa
MIN_FLOOR_AREA_PER_PERSON = 10  # m² por pessoa
WATER_PER_DAY_PER_PERSON = 2.5  # litros

# Envelope de lançamento
SLS_MAX_DIAMETER = 8.4  # metros
STARSHIP_MAX_DIAMETER = 9.0  # metros

# Cores das zonas funcionais
ZONE_COLORS = {
    "sleep": "#667eea",
    "hygiene": "#48bb78",
    "kitchen": "#ed8936",
    "exercise": "#f56565",
    "storage": "#9f7aea",
    "work_leisure": "#4299e1"
}

# Nomes das zonas
ZONE_NAMES = {
    "sleep": "Sleep Quarters",
    "hygiene": "Hygiene Module",
    "kitchen": "Galley Station",
    "exercise": "Exercise Bay",
    "storage": "Storage Module",
    "work_leisure": "Work & Recreation"
}

# Área mínima por pessoa para cada zona (m²)
ZONE_MIN_AREA = {
    "sleep": 4.0,
    "hygiene": 2.0,
    "kitchen": 3.0,
    "exercise": 2.5,
    "storage": 3.0,
    "work_leisure": 5.0
}

# Zonas incompatíveis (não devem ser adjacentes)
INCOMPATIBLE_ZONES = [
    ("sleep", "exercise"),
    ("sleep", "kitchen"),
    ("sleep", "hygiene")
]

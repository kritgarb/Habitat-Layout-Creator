"""
Constantes e configurações NASA para o Habitat Layout Creator

Baseado em:
- Defining the Net Habitable Volume for Long Duration Exploration Missions
- Moon to Mars Architecture Definition Document
- Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)
- NASA's Moon to Mars Transit Habitat Refinement Point of Departure Design
"""

# ========================================
# PADRÕES NASA - VOLUME E ÁREA
# ========================================
# Referência: Defining the Net Habitable Volume for Long Duration Exploration Missions
MIN_NHV_PER_PERSON = 25  # m³ por pessoa (missões longas)
MIN_NHV_PER_PERSON_TRANSIT = 27  # m³ por pessoa (habitats de trânsito - maior devido ao estresse)
MIN_FLOOR_AREA_PER_PERSON = 10  # m² por pessoa
MIN_PRIVACY_VOLUME_PER_PERSON = 5.0  # m³ (área privada essencial)

# ========================================
# RECURSOS DE SUPORTE À VIDA (QUANTIFICADOS)
# ========================================
# Referência: NASA-STD-3001 e Human Integration Design Handbook (HIDH)
WATER_POTABLE_PER_DAY_PER_PERSON = 2.0  # kg (água potável)
WATER_FOOD_PREP_PER_DAY_PER_PERSON = 0.5  # kg (reidratação de alimentos)
WATER_HYGIENE_PER_DAY_PER_PERSON = 23.0  # litros (higiene, reciclável)
OXYGEN_CONSUMPTION_PER_DAY_PER_PERSON = 0.82  # kg (consumo metabólico)
CO2_PRODUCTION_PER_DAY_PER_PERSON = 1.04  # kg (produção metabólica)
FOOD_PER_DAY_PER_PERSON = 0.62  # kg (comida seca)
POWER_PER_PERSON = 2000  # Watts (média)

# Área de Biomass Production Chamber (BPC) para produção de O2
BPC_AREA_PER_PERSON = 22.5  # m² (20-25 m² de plantio para fornecer O2)

# ========================================
# ENVELOPE DE LANÇAMENTO
# ========================================
# Referência: Moon to Mars Architecture Definition Document
SLS_MAX_DIAMETER = 8.4  # metros (NASA Space Launch System)
SLS_MAX_HEIGHT = 27.4  # metros (compartimento de carga)
STARSHIP_MAX_DIAMETER = 9.0  # metros (SpaceX Starship)
STARSHIP_MAX_HEIGHT = 17.24  # metros (compartimento de carga)

# ========================================
# DIMENSÕES ERGONÔMICAS E ANTROPOMÉTRICAS
# ========================================
# Referência: Human Integration Design Handbook (HIDH) - Clearance e Reach
MIN_CEILING_HEIGHT = 2.1  # metros
MIN_CORRIDOR_WIDTH = 0.81  # metros (caminho de emergência mínimo)
MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC = 1.14  # metros (passagem dupla)
MIN_DOOR_WIDTH = 0.7  # metros
MIN_DOOR_HEIGHT = 1.9  # metros
MIN_WORKSTATION_AREA = 1.5  # m² por estação de trabalho

# Dimensões de clearance para trajes pressurizados
EVA_SUIT_WIDTH_CLEARANCE = 0.9  # metros (largura com traje EVA)
EVA_SUIT_HEIGHT_CLEARANCE = 2.3  # metros (altura com traje EVA)

# Dimensões mínimas de caminho de emergência (desobstruído)
EMERGENCY_PATH_WIDTH = 0.81  # metros
EMERGENCY_PATH_HEIGHT = 1.14  # metros

# ========================================
# PADRÕES AMBIENTAIS
# ========================================
# Referência: Deep Space Habitability Design Guidelines
TEMP_MIN = 18  # °C
TEMP_MAX = 27  # °C
HUMIDITY_MIN = 30  # %
HUMIDITY_MAX = 70  # %
MAX_CO2 = 5.3  # mmHg (0.7 kPa)
MAX_NOISE_SLEEP = 60  # dB (área de sono)
MAX_NOISE_WORK = 70  # dB (áreas de trabalho)

# ========================================
# ILUMINAÇÃO
# ========================================
# Referência: Deep Space Habitability Design Guidelines
MIN_LUX = 200  # lux
MAX_LUX = 500  # lux
COLOR_TEMP_MIN = 2700  # Kelvin (luz quente - noite)
COLOR_TEMP_MAX = 6500  # Kelvin (luz fria - dia)

# ========================================
# ZONAS FUNCIONAIS - CORES
# ========================================
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

# Área mínima e volume por pessoa para cada zona (m² e m³)
# Referência: Internal Layout Assessment of a Lunar Surface Habitat + HIDH
ZONE_MIN_AREA = {
    "sleep": 4.0,
    "hygiene": 2.0,
    "kitchen": 3.0,
    "exercise": 2.5,
    "storage": 3.0,
    "work_leisure": 5.0
}

# Volume operacional por zona (m³)
ZONE_VOLUMES = {
    "sleep": 2.69,  # Acomodação individual de sono
    "hygiene": 3.0,  # Inclui restraints para 0g
    "kitchen": 10.09,  # Área de refeição coletiva (4 pessoas)
    "exercise": 24.0,  # Volume operacional de equipamento + movimento
    "storage": 5.0,  # Distributed storage
    "work_leisure": 18.20  # Área coletiva para 4 pessoas
}

# ========================================
# INCOMPATIBILIDADES E ADJACÊNCIAS (MATRIZ DE CONFLITO)
# ========================================
# Referência: Internal Layout Assessment of a Lunar Surface Habitat + HIDH
# Zonas incompatíveis (não devem ser adjacentes) - com motivos
INCOMPATIBLE_ZONES = {
    ("sleep", "exercise"): "Ruído e vibração incompatíveis com descanso",
    ("sleep", "kitchen"): "Odores, ruído de preparação, atividade constante",
    ("hygiene", "kitchen"): "Razões sanitárias e psicológicas (odores)"
}

# Zonas que devem ser próximas (adjacências recomendadas)
ADJACENT_ZONES_RECOMMENDED = {
    ("hygiene", "sleep"): "Conveniência de acesso aos quartos",
    ("kitchen", "work_leisure"): "Área social integrada",
    ("storage", "kitchen"): "Acesso a insumos alimentares"
}

# Requisitos de isolamento por zona
ZONE_ISOLATION_REQUIREMENTS = {
    "sleep": {
        "acoustic": True,  # Isolamento acústico obrigatório
        "privacy_visual": True,  # Privacidade visual total
        "max_noise_db": 60
    },
    "hygiene": {
        "acoustic": False,
        "privacy_visual": True,  # Privacidade visual total
        "max_noise_db": 70
    },
    "exercise": {
        "acoustic": True,  # Deve ser isolado para não transmitir vibração
        "privacy_visual": False,
        "vibration_isolation": True  # Isolamento de vibração estrutural
    }
}

# ========================================
# PRODUÇÃO DE ALIMENTOS (OPCIONAL)
# ========================================
# Referência: Food Production on the Moon and in Remote Areas
FOOD_PRODUCTION_AREA_PER_PERSON = 6.0  # m² (hidroponia)
FOOD_PRODUCTION_HEIGHT = 2.0  # metros (crescimento de plantas)
FOOD_PRODUCTION_WATER_PER_DAY = 8.0  # litros por pessoa
FOOD_PRODUCTION_POWER = 200  # W/m² (iluminação LED)
FOOD_O2_PRODUCTION = 0.5  # kg/dia/pessoa (fotossíntese)

# ========================================
# TIPOS DE MISSÃO
# ========================================
# Referência: Moon to Mars Architecture Definition Document
MISSION_TYPES = {
    "transit": {
        "description": "Habitat de trânsito (Terra-Marte)",
        "duration_days": (180, 300),
        "min_nhv_per_person": 27,
        "gravity": "zero_or_artificial",
        "critical_zones": ["exercise", "work_leisure", "sleep"]
    },
    "lunar_surface": {
        "description": "Habitat de superfície lunar",
        "duration_days": (30, 365),
        "min_nhv_per_person": 25,
        "gravity": "1/6_earth",
        "radiation_shielding": "regolith_2m+"
    },
    "mars_surface": {
        "description": "Habitat de superfície marciana",
        "duration_days": (500, 900),
        "min_nhv_per_person": 25,
        "gravity": "3/8_earth",
        "radiation_shielding": "regolith_or_structure"
    }
}

# ========================================
# ESTRUTURA DE HABITAT
# ========================================
# Referência: Review of Habitable Softgoods Inflatable Design
HABITAT_TYPES = {
    "rigid": {
        "description": "Estrutura rígida (alumínio/compósito)",
        "volume_efficiency": 1.0,
        "mass_per_volume": 150,  # kg/m³
        "advantages": ["rigidez", "proteção MMOD", "montagem equipamentos"],
        "disadvantages": ["volume limitado", "peso elevado"]
    },
    "inflatable": {
        "description": "Estrutura inflável (softgoods)",
        "volume_efficiency": 3.5,  # 3-4x maior que rígido
        "mass_per_volume": 40,  # kg/m³
        "advantages": ["grande volume", "peso reduzido", "empacotamento"],
        "disadvantages": ["complexidade vedação", "rigidez limitada"]
    }
}

# ========================================
# FÓRMULAS DE CÁLCULO DE NHV
# ========================================
# Referência: Defining the Net Habitable Volume for Long Duration Exploration Missions
# Fórmula: NHV (m³/pessoa) = 6.67 × ln(duração_em_dias) - 7.79
def calculate_nhv_per_person(duration_days):
    """
    Calcula o Volume Habitável Líquido (NHV) mínimo por pessoa
    baseado na duração da missão.
    
    Args:
        duration_days: Duração da missão em dias
        
    Returns:
        NHV em m³ por pessoa
    """
    import math
    return 6.67 * math.log(duration_days) - 7.79

# Valores de referência calculados
NHV_REFERENCE = {
    30: round(calculate_nhv_per_person(30), 2),    # ~15.0 m³/pessoa
    90: round(calculate_nhv_per_person(90), 2),    # ~22.2 m³/pessoa
    180: round(calculate_nhv_per_person(180), 2),  # ~26.85 m³/pessoa
    365: round(calculate_nhv_per_person(365), 2),  # ~31.7 m³/pessoa
    500: round(calculate_nhv_per_person(500), 2),  # ~33.7 m³/pessoa
    900: round(calculate_nhv_per_person(900), 2)   # ~37.4 m³/pessoa
}

# ========================================
# ADAPTAÇÃO GRAVITACIONAL
# ========================================
# Referência: HIDH - Volume vs Área de Superfície Horizontal
GRAVITY_ENVIRONMENTS = {
    "microgravity": {
        "code": "0g",
        "description": "Microgravidade (órbita, trânsito)",
        "primary_metric": "volume",  # Volume é a métrica principal
        "use_ceiling_walls": True,   # Teto e paredes são utilizáveis
        "restraints_required": True,  # Restraints obrigatórios
        "area_weight": 0.3,
        "volume_weight": 0.7
    },
    "lunar": {
        "code": "1/6g",
        "description": "Gravidade lunar (1/6 da Terra)",
        "primary_metric": "area",  # Área horizontal é priorizada
        "use_ceiling_walls": False,
        "restraints_required": False,
        "area_weight": 0.7,
        "volume_weight": 0.3
    },
    "mars": {
        "code": "3/8g",
        "description": "Gravidade marciana (3/8 da Terra)",
        "primary_metric": "area",  # Área horizontal é priorizada
        "use_ceiling_walls": False,
        "restraints_required": False,
        "area_weight": 0.8,
        "volume_weight": 0.2
    }
}

# ========================================
# SEGURANÇA - ACELERAÇÃO TRANSITÓRIA
# ========================================
# Referência: HIDH - Launch and Landing Acceleration
ACCELERATION_SAFETY = {
    "launch_landing": {
        "description": "Requisitos para pouso e lançamento",
        "seating_type": "contoured_couch",  # Assentos contornados obrigatórios
        "restraint_system": "5_point_harness",  # Arnês de 5 pontos
        "orientation_preferred": "+Gx",  # Eyeballs-in (peito) - maior tolerância
        "max_acceleration_gs": 6.0,  # Aceleração máxima suportável
        "requirements": [
            "Assentos contornados para distribuição de carga",
            "Sistema de restrição de múltiplos pontos (5 pontos mínimo)",
            "Eliminação de elementos rígidos que causem point loading",
            "Proteção da coluna vertebral contra lesões",
            "Orientação preferencial +Gx (através do peito)"
        ]
    },
    "emergency_egress": {
        "description": "Requisitos de saída de emergência",
        "path_width_min": 0.81,  # metros
        "path_height_min": 1.14,  # metros
        "max_distance_to_exit": 30.0,  # metros
        "unobstructed": True  # Caminho deve ser completamente desobstruído
    }
}

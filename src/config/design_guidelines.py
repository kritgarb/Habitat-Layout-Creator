"""
Design Guidelines para Habitats Espaciais

Baseado em:
- Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)
- A Tool for Automated Design and Evaluation of Habitat Interior Layouts
- Multi-functionality in Space
- Internal Layout Assessment of a Lunar Surface Habitat
"""

# ========================================
# MÉTRICAS DE AVALIAÇÃO DE LAYOUT
# ========================================

class LayoutMetrics:
    """
    Métricas para avaliar a eficiência e qualidade do layout do habitat.
    Referência: A Tool for Automated Design and Evaluation of Habitat Interior Layouts
    """
    
    @staticmethod
    def calculate_space_efficiency(usable_area, total_area):
        """
        Calcula a eficiência de utilização do espaço.
        
        Args:
            usable_area (float): Área utilizável (soma das zonas funcionais)
            total_area (float): Área total do piso
            
        Returns:
            float: Eficiência em porcentagem (meta: ≥ 75%)
        """
        if total_area == 0:
            return 0.0
        efficiency = (usable_area / total_area) * 100
        return efficiency
    
    @staticmethod
    def calculate_circulation_index(circulation_area, total_area):
        """
        Calcula o índice de área de circulação.
        
        Args:
            circulation_area (float): Área dedicada à circulação (corredores)
            total_area (float): Área total do piso
            
        Returns:
            float: Índice de circulação em porcentagem (meta: 15-25%)
        """
        if total_area == 0:
            return 0.0
        index = (circulation_area / total_area) * 100
        return index
    
    @staticmethod
    def calculate_privacy_index(private_zones, crew_size):
        """
        Calcula o índice de privacidade.
        
        Args:
            private_zones (int): Número de zonas privadas adequadas
            crew_size (int): Tamanho da tripulação
            
        Returns:
            float: Índice de privacidade em porcentagem (meta: 100%)
        """
        if crew_size == 0:
            return 0.0
        index = (private_zones / crew_size) * 100
        return index
    
    @staticmethod
    def evaluate_layout_quality(zones, floor_area, crew_size):
        """
        Avalia a qualidade geral do layout.
        
        Args:
            zones (dict): Dicionário de zonas e suas áreas
            floor_area (float): Área total do piso
            crew_size (int): Tamanho da tripulação
            
        Returns:
            dict: Dicionário com métricas de qualidade e status
        """
        usable_area = sum(zone['area'] for zone in zones.values())
        space_efficiency = LayoutMetrics.calculate_space_efficiency(usable_area, floor_area)
        
        # Estimar área de circulação (não utilizada)
        circulation_area = floor_area - usable_area
        circulation_index = LayoutMetrics.calculate_circulation_index(circulation_area, floor_area)
        
        # Assumir que cada pessoa tem um quarto privado
        private_zones = crew_size if zones.get('sleep') else 0
        privacy_index = LayoutMetrics.calculate_privacy_index(private_zones, crew_size)
        
        return {
            "space_efficiency": {
                "value": space_efficiency,
                "target": 75.0,
                "status": "pass" if space_efficiency >= 75.0 else "warning",
                "unit": "%"
            },
            "circulation_index": {
                "value": circulation_index,
                "target_range": (15.0, 25.0),
                "status": "pass" if 15.0 <= circulation_index <= 25.0 else "warning",
                "unit": "%"
            },
            "privacy_index": {
                "value": privacy_index,
                "target": 100.0,
                "status": "pass" if privacy_index == 100.0 else "fail",
                "unit": "%"
            }
        }


# ========================================
# HABITABILIDADE - DIMENSÕES
# ========================================

HABITABILITY_DIMENSIONS = {
    "ceiling": {
        "min_height": 2.1,  # metros
        "optimal_height": 2.4,  # metros
        "description": "Altura mínima para movimentação confortável"
    },
    "corridors": {
        "min_width": 0.8,  # metros
        "optimal_width": 1.2,  # metros
        "description": "Largura mínima para passagem de 1 pessoa + equipamento"
    },
    "doors": {
        "min_width": 0.7,  # metros
        "min_height": 1.9,  # metros
        "optimal_width": 0.9,  # metros
        "description": "Dimensões mínimas para passagem com carga"
    },
    "workstations": {
        "min_area": 1.5,  # m² por estação
        "optimal_area": 2.0,  # m²
        "desk_height": 0.75,  # metros
        "description": "Área para trabalho confortável"
    },
    "sleeping_quarters": {
        "min_volume": 5.0,  # m³ por pessoa
        "min_area": 3.0,  # m²
        "bed_size": (2.0, 0.75),  # metros (comprimento, largura)
        "description": "Espaço privado mínimo para descanso"
    }
}


# ========================================
# HABITABILIDADE - AMBIENTE
# ========================================

ENVIRONMENTAL_STANDARDS = {
    "temperature": {
        "min": 18,  # °C
        "max": 27,  # °C
        "optimal": 22,  # °C
        "description": "Temperatura confortável para atividades"
    },
    "humidity": {
        "min": 30,  # %
        "max": 70,  # %
        "optimal": 50,  # %
        "description": "Umidade relativa do ar"
    },
    "co2": {
        "max": 5.3,  # mmHg (0.7 kPa)
        "optimal": 3.0,  # mmHg
        "unit": "mmHg",
        "description": "Concentração máxima de CO₂"
    },
    "noise": {
        "sleep_area_max": 60,  # dB
        "work_area_max": 70,  # dB
        "optimal": 50,  # dB
        "unit": "dB",
        "description": "Níveis de ruído aceitáveis"
    },
    "lighting": {
        "min_lux": 200,
        "max_lux": 500,
        "color_temp_day": 6500,  # Kelvin (luz fria)
        "color_temp_evening": 4000,  # Kelvin
        "color_temp_night": 2700,  # Kelvin (luz quente)
        "description": "Iluminação circadiana ajustável"
    },
    "air_velocity": {
        "min": 0.05,  # m/s
        "max": 0.25,  # m/s
        "description": "Velocidade do ar para conforto"
    }
}


# ========================================
# MULTI-FUNCIONALIDADE
# ========================================

MULTIFUNCTIONAL_SPACES = {
    "dining_meeting_recreation": {
        "functions": ["dining", "meetings", "recreation", "social"],
        "area_per_person": 2.0,  # m² (ao invés de 6.0 separado)
        "time_sharing": True,
        "equipment": ["mesa dobrável", "cadeiras empilháveis", "tela retrátil"],
        "efficiency_gain": 0.67,  # Economiza 67% do espaço
        "description": "Espaço central multi-uso com mobília transformável"
    },
    "work_communication": {
        "functions": ["workstation", "communication", "research"],
        "area_per_person": 1.5,  # m²
        "time_sharing": False,
        "equipment": ["mesa ajustável", "monitor retrátil", "armazenamento compacto"],
        "description": "Estação de trabalho individual"
    },
    "exercise_medical": {
        "functions": ["exercise", "medical_checkup"],
        "area_per_person": 3.0,  # m²
        "time_sharing": True,
        "equipment": ["esteira dobrável", "bicicleta ergométrica", "maca retrátil"],
        "description": "Área de exercício que também serve para exames médicos"
    },
    "storage_utility": {
        "functions": ["storage", "maintenance", "waste_processing"],
        "area_per_person": 3.5,  # m²
        "time_sharing": False,
        "equipment": ["prateleiras modulares", "bancada de manutenção"],
        "description": "Armazenamento integrado com área de utilidade"
    }
}


# ========================================
# ADJACÊNCIAS RECOMENDADAS
# ========================================

RECOMMENDED_ADJACENCIES = {
    # Zonas que devem estar próximas (peso de importância: 0-1)
    "high_priority": [
        {"zones": ("sleep", "hygiene"), "weight": 0.9, "reason": "Acesso rápido após despertar"},
        {"zones": ("kitchen", "dining"), "weight": 0.8, "reason": "Servir refeições"},
        {"zones": ("work", "communication"), "weight": 0.7, "reason": "Colaboração"},
        {"zones": ("storage", "kitchen"), "weight": 0.7, "reason": "Acesso a suprimentos"},
    ],
    "medium_priority": [
        {"zones": ("hygiene", "storage"), "weight": 0.5, "reason": "Toalhas e suprimentos"},
        {"zones": ("exercise", "medical"), "weight": 0.5, "reason": "Monitoramento de saúde"},
    ],
    # Zonas que NÃO devem estar próximas (peso negativo)
    "incompatible": [
        {"zones": ("sleep", "exercise"), "weight": -0.9, "reason": "Ruído e vibração"},
        {"zones": ("sleep", "kitchen"), "weight": -0.7, "reason": "Odores e atividade"},
        {"zones": ("sleep", "hygiene"), "weight": -0.6, "reason": "Ruído de água"},
        {"zones": ("work", "exercise"), "weight": -0.5, "reason": "Ruído e distração"},
    ]
}


# ========================================
# PRODUÇÃO DE ALIMENTOS
# ========================================

FOOD_PRODUCTION_CONFIG = {
    "hydroponics": {
        "area_per_person": 6.0,  # m²
        "height_requirement": 2.0,  # metros
        "water_per_day": 8.0,  # litros/pessoa
        "power_requirement": 200,  # W/m²
        "o2_production": 0.5,  # kg/dia/pessoa
        "food_yield": 0.3,  # kg/dia/pessoa (vegetais frescos)
        "crop_types": {
            "leafy_greens": {"days": 35, "yield_kg_m2": 25},
            "tomatoes": {"days": 90, "yield_kg_m2": 40},
            "potatoes": {"days": 70, "yield_kg_m2": 30},
            "strawberries": {"days": 120, "yield_kg_m2": 15}
        },
        "benefits": {
            "psychological": "Conexão com natureza, atividade terapêutica",
            "nutritional": "Vegetais frescos, variedade na dieta",
            "life_support": "Produção de O₂, consumo de CO₂"
        }
    },
    "aeroponics": {
        "area_per_person": 4.0,  # m² (mais eficiente)
        "height_requirement": 1.8,  # metros
        "water_per_day": 5.0,  # litros/pessoa (90% mais eficiente)
        "power_requirement": 150,  # W/m²
        "o2_production": 0.4,  # kg/dia/pessoa
        "food_yield": 0.25,  # kg/dia/pessoa
        "advantages": ["menor uso de água", "maior densidade de cultivo", "menos massa total"]
    }
}


# ========================================
# REGRAS DE VALIDAÇÃO DE DESIGN
# ========================================

DESIGN_VALIDATION_RULES = {
    "critical": [
        {
            "rule": "nhv_per_person",
            "min_value": 25,
            "description": "Volume habitável líquido mínimo por pessoa",
            "reference": "Defining the Net Habitable Volume"
        },
        {
            "rule": "ceiling_height",
            "min_value": 2.1,
            "description": "Altura mínima do teto",
            "reference": "Deep Space Habitability Guidelines"
        },
        {
            "rule": "emergency_exit",
            "requirement": "two_exits",
            "description": "Mínimo de duas saídas de emergência",
            "reference": "NASA Safety Standards"
        }
    ],
    "recommended": [
        {
            "rule": "space_efficiency",
            "target": 75,
            "description": "Eficiência de uso do espaço ≥ 75%",
            "reference": "Layout Assessment Tool"
        },
        {
            "rule": "privacy_quarters",
            "requirement": "one_per_person",
            "description": "Quarto privado para cada tripulante",
            "reference": "Transit Habitat Design"
        },
        {
            "rule": "circulation_area",
            "range": (15, 25),
            "description": "Área de circulação entre 15-25%",
            "reference": "Layout Assessment Tool"
        }
    ],
    "optional": [
        {
            "rule": "food_production",
            "area_per_person": 6.0,
            "description": "Área de cultivo de alimentos (hidroponia)",
            "reference": "Food Production on the Moon"
        },
        {
            "rule": "window_area",
            "min_per_person": 0.5,
            "description": "Área de janela/visor para saúde mental",
            "reference": "Transit Habitat Design"
        }
    ]
}


# ========================================
# FUNÇÕES DE VALIDAÇÃO
# ========================================

def validate_habitability_standards(dimensions, environment):
    """
    Valida se o habitat atende aos padrões de habitabilidade.
    
    Args:
        dimensions (dict): Dimensões do habitat
        environment (dict): Condições ambientais
        
    Returns:
        dict: Resultado da validação com issues e warnings
    """
    issues = []
    warnings = []
    
    # Validar dimensões
    if dimensions.get('ceiling_height', 0) < HABITABILITY_DIMENSIONS['ceiling']['min_height']:
        issues.append({
            "type": "critical",
            "category": "dimensions",
            "message": f"Altura do teto ({dimensions.get('ceiling_height')}m) abaixo do mínimo (2.1m)"
        })
    
    # Validar ambiente
    if environment.get('temperature'):
        temp = environment['temperature']
        if temp < ENVIRONMENTAL_STANDARDS['temperature']['min'] or temp > ENVIRONMENTAL_STANDARDS['temperature']['max']:
            warnings.append({
                "type": "environmental",
                "category": "temperature",
                "message": f"Temperatura ({temp}°C) fora da faixa recomendada (18-27°C)"
            })
    
    return {
        "is_valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings
    }


def calculate_adjacency_score(zone_layout):
    """
    Calcula a pontuação de adjacência do layout.
    
    Args:
        zone_layout (dict): Layout das zonas com posições
        
    Returns:
        float: Pontuação de adjacência (0-100)
    """
    # Implementação simplificada - pode ser expandida
    score = 75.0  # Pontuação base
    
    # Penalizar zonas incompatíveis adjacentes
    for incompatible in RECOMMENDED_ADJACENCIES['incompatible']:
        zone1, zone2 = incompatible['zones']
        if are_zones_adjacent(zone_layout, zone1, zone2):
            score += incompatible['weight'] * 10  # Peso negativo
    
    # Recompensar zonas recomendadas adjacentes
    for recommended in RECOMMENDED_ADJACENCIES['high_priority']:
        zone1, zone2 = recommended['zones']
        if are_zones_adjacent(zone_layout, zone1, zone2):
            score += recommended['weight'] * 5  # Peso positivo
    
    return max(0, min(100, score))


def are_zones_adjacent(zone_layout, zone1, zone2):
    """
    Verifica se duas zonas são adjacentes no layout.
    
    Args:
        zone_layout (dict): Layout das zonas
        zone1 (str): Nome da primeira zona
        zone2 (str): Nome da segunda zona
        
    Returns:
        bool: True se as zonas são adjacentes
    """
    # Implementação simplificada - necessita de lógica geométrica real
    return False  # Placeholder


# ========================================
# EXPORTAÇÃO
# ========================================

__all__ = [
    'LayoutMetrics',
    'HABITABILITY_DIMENSIONS',
    'ENVIRONMENTAL_STANDARDS',
    'MULTIFUNCTIONAL_SPACES',
    'RECOMMENDED_ADJACENCIES',
    'FOOD_PRODUCTION_CONFIG',
    'DESIGN_VALIDATION_RULES',
    'validate_habitability_standards',
    'calculate_adjacency_score'
]

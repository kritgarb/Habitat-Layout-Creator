"""
Cálculos e validações baseados em métricas quantitativas da NASA

Referências:
- Human Integration Design Handbook (HIDH)
- Defining the Net Habitable Volume for Long Duration Exploration Missions
- NASA-STD-3001 Volume 2
"""

import math
from typing import Dict, List, Tuple
from ..config.constants import (
    WATER_POTABLE_PER_DAY_PER_PERSON,
    WATER_FOOD_PREP_PER_DAY_PER_PERSON,
    OXYGEN_CONSUMPTION_PER_DAY_PER_PERSON,
    CO2_PRODUCTION_PER_DAY_PER_PERSON,
    BPC_AREA_PER_PERSON,
    FOOD_PER_DAY_PER_PERSON,
    INCOMPATIBLE_ZONES,
    ADJACENT_ZONES_RECOMMENDED,
    GRAVITY_ENVIRONMENTS,
    EMERGENCY_PATH_WIDTH,
    EMERGENCY_PATH_HEIGHT,
    MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC
)


def calculate_nhv_per_person(duration_days: int) -> float:
    """
    Calcula o Volume Habitável Líquido (NHV) mínimo por pessoa
    baseado na duração da missão usando a fórmula NASA.
    
    Fórmula: NHV (m³/pessoa) = 6.67 × ln(duração_em_dias) - 7.79
    
    Args:
        duration_days: Duração da missão em dias
        
    Returns:
        NHV em m³ por pessoa
        
    Referência: Defining the Net Habitable Volume for Long Duration Exploration Missions
    """
    if duration_days <= 0:
        raise ValueError("Duração da missão deve ser maior que zero")
    
    return 6.67 * math.log(duration_days) - 7.79


def calculate_mission_resources(crew_size: int, duration_days: int) -> Dict[str, Dict[str, float]]:
    """
    Calcula os recursos totais necessários para uma missão.
    
    Args:
        crew_size: Número de tripulantes
        duration_days: Duração da missão em dias
        
    Returns:
        Dicionário com recursos diários e totais da missão
    """
    return {
        "daily": {
            "water_potable_kg": WATER_POTABLE_PER_DAY_PER_PERSON * crew_size,
            "water_food_prep_kg": WATER_FOOD_PREP_PER_DAY_PER_PERSON * crew_size,
            "oxygen_kg": OXYGEN_CONSUMPTION_PER_DAY_PER_PERSON * crew_size,
            "co2_produced_kg": CO2_PRODUCTION_PER_DAY_PER_PERSON * crew_size,
            "food_kg": FOOD_PER_DAY_PER_PERSON * crew_size,
        },
        "total_mission": {
            "water_potable_kg": WATER_POTABLE_PER_DAY_PER_PERSON * crew_size * duration_days,
            "water_food_prep_kg": WATER_FOOD_PREP_PER_DAY_PER_PERSON * crew_size * duration_days,
            "oxygen_kg": OXYGEN_CONSUMPTION_PER_DAY_PER_PERSON * crew_size * duration_days,
            "co2_produced_kg": CO2_PRODUCTION_PER_DAY_PER_PERSON * crew_size * duration_days,
            "food_kg": FOOD_PER_DAY_PER_PERSON * crew_size * duration_days,
        },
        "bpc_requirements": {
            "area_m2": BPC_AREA_PER_PERSON * crew_size,
            "description": f"{BPC_AREA_PER_PERSON} m² de plantio por pessoa para produção de O2"
        }
    }


def validate_zone_compatibility(layout: Dict[str, Dict]) -> List[Dict[str, str]]:
    """
    Valida compatibilidade entre zonas adjacentes baseado na matriz de conflito.
    
    Args:
        layout: Dicionário com zonas e suas posições
        
    Returns:
        Lista de conflitos detectados
    """
    conflicts = []
    
    # Verifica incompatibilidades
    for (zone1, zone2), reason in INCOMPATIBLE_ZONES.items():
        if zone1 in layout and zone2 in layout:
            # Verifica se são adjacentes (simplificado - pode ser expandido)
            if are_zones_adjacent(layout[zone1], layout[zone2]):
                conflicts.append({
                    "type": "incompatibility",
                    "zone1": zone1,
                    "zone2": zone2,
                    "reason": reason,
                    "severity": "high"
                })
    
    return conflicts


def are_zones_adjacent(zone1: Dict, zone2: Dict, threshold: float = 1.0) -> bool:
    """
    Determina se duas zonas são adjacentes baseado em suas posições.
    
    Args:
        zone1: Dicionário com posição da zona 1 (x, y, width, height)
        zone2: Dicionário com posição da zona 2
        threshold: Distância máxima para considerar adjacente (metros)
        
    Returns:
        True se as zonas são adjacentes
    """
    # Simplificado - verifica distância entre centros
    if 'x' not in zone1 or 'x' not in zone2:
        return False
    
    x1, y1 = zone1['x'], zone1['y']
    x2, y2 = zone2['x'], zone2['y']
    
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return distance <= threshold


def calculate_gravity_adjusted_metrics(
    volume_m3: float,
    area_m2: float,
    gravity_env: str
) -> Dict[str, float]:
    """
    Calcula métricas ajustadas baseadas no ambiente gravitacional.
    
    Args:
        volume_m3: Volume total disponível
        area_m2: Área horizontal disponível
        gravity_env: Ambiente gravitacional ('microgravity', 'lunar', 'mars')
        
    Returns:
        Métricas ponderadas e score de habitabilidade
    """
    env = GRAVITY_ENVIRONMENTS.get(gravity_env, GRAVITY_ENVIRONMENTS['microgravity'])
    
    # Pondera volume e área baseado no ambiente
    weighted_volume = volume_m3 * env['volume_weight']
    weighted_area = area_m2 * env['area_weight']
    
    habitability_score = weighted_volume + (weighted_area * 2.5)  # Fator de conversão
    
    return {
        "volume_m3": volume_m3,
        "area_m2": area_m2,
        "weighted_volume": weighted_volume,
        "weighted_area": weighted_area,
        "habitability_score": habitability_score,
        "primary_metric": env['primary_metric'],
        "restraints_required": env['restraints_required'],
        "use_ceiling_walls": env['use_ceiling_walls']
    }


def validate_translation_paths(paths: List[Dict]) -> List[Dict[str, str]]:
    """
    Valida rotas de translação e caminhos de emergência.
    
    Args:
        paths: Lista de caminhos com suas dimensões
        
    Returns:
        Lista de validações e alertas
    """
    validations = []
    
    for path in paths:
        path_type = path.get('type', 'standard')
        width = path.get('width', 0)
        height = path.get('height', 0)
        
        if path_type == 'emergency':
            # Valida caminho de emergência
            if width < EMERGENCY_PATH_WIDTH:
                validations.append({
                    "type": "error",
                    "path_id": path.get('id', 'unknown'),
                    "message": f"Caminho de emergência muito estreito: {width}m < {EMERGENCY_PATH_WIDTH}m mínimo",
                    "requirement": "HIDH - Emergency Egress"
                })
            
            if height < EMERGENCY_PATH_HEIGHT:
                validations.append({
                    "type": "error",
                    "path_id": path.get('id', 'unknown'),
                    "message": f"Caminho de emergência muito baixo: {height}m < {EMERGENCY_PATH_HEIGHT}m mínimo",
                    "requirement": "HIDH - Emergency Egress"
                })
                
        elif path_type == 'high_traffic':
            # Valida caminho de alto tráfego (passagem dupla)
            if width < MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC:
                validations.append({
                    "type": "warning",
                    "path_id": path.get('id', 'unknown'),
                    "message": f"Caminho de alto tráfego estreito: {width}m < {MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC}m recomendado para passagem dupla",
                    "requirement": "HIDH - Translation Paths"
                })
    
    return validations


def calculate_storage_volume(crew_size: int, duration_days: int, margin: float = 0.2) -> Dict[str, float]:
    """
    Calcula volume de armazenamento necessário (distributed storage).
    
    Args:
        crew_size: Número de tripulantes
        duration_days: Duração da missão
        margin: Margem de segurança (padrão 20%)
        
    Returns:
        Volume de storage por categoria
    """
    resources = calculate_mission_resources(crew_size, duration_days)
    
    # Densidade estimada dos recursos
    water_density = 1.0  # kg/L = 1000 kg/m³
    food_density = 200  # kg/m³ (alimento desidratado empacotado)
    
    total_water = resources['total_mission']['water_potable_kg'] + \
                  resources['total_mission']['water_food_prep_kg']
    
    total_food = resources['total_mission']['food_kg']
    
    # Calcula volumes
    water_volume = (total_water / 1000) * (1 + margin)  # m³
    food_volume = (total_food / food_density) * (1 + margin)  # m³
    
    # Volume adicional para equipamentos e suprimentos
    equipment_volume = crew_size * 2.0 * (1 + margin)  # m³
    
    return {
        "water_storage_m3": round(water_volume, 2),
        "food_storage_m3": round(food_volume, 2),
        "equipment_storage_m3": round(equipment_volume, 2),
        "total_storage_m3": round(water_volume + food_volume + equipment_volume, 2),
        "distributed_locations": [
            "Próximo à galley (insumos alimentares)",
            "Próximo à higiene (água)",
            "Distribuído nas cabines (equipamentos pessoais)"
        ]
    }


def generate_layout_recommendations(
    crew_size: int,
    duration_days: int,
    gravity_env: str,
    structure_type: str
) -> Dict[str, any]:
    """
    Gera recomendações completas de layout baseadas em todos os parâmetros.
    
    Args:
        crew_size: Número de tripulantes
        duration_days: Duração da missão
        gravity_env: Ambiente gravitacional
        structure_type: Tipo de estrutura ('rigid' ou 'inflatable')
        
    Returns:
        Dicionário com todas as recomendações
    """
    nhv_per_person = calculate_nhv_per_person(duration_days)
    total_nhv = nhv_per_person * crew_size
    resources = calculate_mission_resources(crew_size, duration_days)
    storage = calculate_storage_volume(crew_size, duration_days)
    
    return {
        "volume_requirements": {
            "nhv_per_person_m3": round(nhv_per_person, 2),
            "total_nhv_m3": round(total_nhv, 2),
            "storage_m3": storage['total_storage_m3'],
            "total_required_m3": round(total_nhv + storage['total_storage_m3'], 2)
        },
        "resources": resources,
        "storage": storage,
        "gravity_considerations": GRAVITY_ENVIRONMENTS[gravity_env],
        "zone_recommendations": {
            "sleep": {
                "volume_m3": 2.69 * crew_size,
                "isolation": "Isolamento acústico obrigatório",
                "avoid_proximity": ["exercise", "kitchen"]
            },
            "exercise": {
                "volume_m3": 24.0,
                "isolation": "Isolamento de vibração estrutural",
                "location": "Separado de áreas de descanso"
            },
            "hygiene": {
                "volume_m3": 3.0 * crew_size,
                "privacy": "Visual total",
                "location": "Próximo a sleep, longe de galley",
                "restraints": GRAVITY_ENVIRONMENTS[gravity_env]['restraints_required']
            },
            "kitchen": {
                "volume_m3": 10.09,
                "adjacency": "Próximo a work_leisure (área social)",
                "storage_nearby": True
            },
            "work_leisure": {
                "volume_m3": 18.20,
                "type": "Área coletiva",
                "flexibility": "Espaço multifuncional"
            }
        },
        "critical_paths": {
            "emergency_egress": {
                "width_min_m": EMERGENCY_PATH_WIDTH,
                "height_min_m": EMERGENCY_PATH_HEIGHT,
                "unobstructed": True
            },
            "high_traffic": {
                "width_min_m": MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC,
                "description": "Passagem dupla"
            }
        }
    }

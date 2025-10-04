"""
Validações de acordo com padrões NASA

Baseado em:
- Defining the Net Habitable Volume for Long Duration Exploration Missions
- Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)
- Internal Layout Assessment of a Lunar Surface Habitat
- A Tool for Automated Design and Evaluation of Habitat Interior Layouts
"""
from typing import List, Tuple, Dict, Any


def validate_nasa_standards(
    nhv_per_person: float,
    floor_area_per_person: float,
    min_nhv: float,
    min_floor_area: float,
    mission_type: str = "surface"
) -> Tuple[bool, List[str]]:
    """
    Valida se o habitat atende aos padrões NASA.
    
    Args:
        nhv_per_person: NHV por pessoa (m³)
        floor_area_per_person: Área de piso por pessoa (m²)
        min_nhv: NHV mínimo requerido (m³)
        min_floor_area: Área mínima requerida (m²)
        mission_type: Tipo de missão ("transit", "surface", "lunar_surface", "mars_surface")
    
    Returns:
        Tupla (is_valid, issues) onde:
        - is_valid: True se todos os padrões são atendidos
        - issues: Lista de strings descrevendo problemas encontrados
    """
    issues = []
    
    # Ajustar requisitos mínimos baseado no tipo de missão
    if mission_type == "transit":
        min_nhv = max(min_nhv, 27)  # Habitats de trânsito precisam de mais volume
    
    if nhv_per_person < min_nhv:
        issues.append(
            f"⚠️ NHV per person ({nhv_per_person:.1f} m³) below minimum ({min_nhv} m³) for {mission_type} mission"
        )
    
    if floor_area_per_person < min_floor_area:
        issues.append(
            f"⚠️ Floor area per person ({floor_area_per_person:.1f} m²) below minimum ({min_floor_area} m²)"
        )
    
    is_valid = len(issues) == 0
    return is_valid, issues


def validate_dimensions(
    ceiling_height: float,
    corridor_width: float = None,
    door_dimensions: Tuple[float, float] = None
) -> Tuple[bool, List[str]]:
    """
    Valida dimensões ergonômicas do habitat.
    
    Referência: Deep Space Habitability Design Guidelines
    
    Args:
        ceiling_height: Altura do teto (metros)
        corridor_width: Largura de corredores (metros, opcional)
        door_dimensions: (largura, altura) da porta (metros, opcional)
    
    Returns:
        Tupla (is_valid, issues)
    """
    issues = []
    
    # Altura mínima do teto
    MIN_CEILING = 2.1
    if ceiling_height < MIN_CEILING:
        issues.append(
            f"🔴 CRITICAL: Ceiling height ({ceiling_height:.2f}m) below minimum ({MIN_CEILING}m)"
        )
    
    # Largura mínima de corredor
    if corridor_width is not None:
        MIN_CORRIDOR = 0.8
        if corridor_width < MIN_CORRIDOR:
            issues.append(
                f"⚠️ Corridor width ({corridor_width:.2f}m) below minimum ({MIN_CORRIDOR}m)"
            )
    
    # Dimensões de porta
    if door_dimensions is not None:
        door_width, door_height = door_dimensions
        MIN_DOOR_WIDTH = 0.7
        MIN_DOOR_HEIGHT = 1.9
        
        if door_width < MIN_DOOR_WIDTH:
            issues.append(
                f"⚠️ Door width ({door_width:.2f}m) below minimum ({MIN_DOOR_WIDTH}m)"
            )
        if door_height < MIN_DOOR_HEIGHT:
            issues.append(
                f"⚠️ Door height ({door_height:.2f}m) below minimum ({MIN_DOOR_HEIGHT}m)"
            )
    
    is_valid = len(issues) == 0
    return is_valid, issues


def validate_environmental_conditions(
    temperature: float = None,
    humidity: float = None,
    co2_level: float = None,
    noise_level: float = None,
    zone_type: str = "work"
) -> Tuple[bool, List[str]]:
    """
    Valida condições ambientais do habitat.
    
    Referência: Deep Space Habitability Design Guidelines
    
    Args:
        temperature: Temperatura (°C, opcional)
        humidity: Umidade relativa (%, opcional)
        co2_level: Nível de CO₂ (mmHg, opcional)
        noise_level: Nível de ruído (dB, opcional)
        zone_type: Tipo de zona ("sleep" ou "work")
    
    Returns:
        Tupla (is_valid, issues)
    """
    issues = []
    warnings = []
    
    # Temperatura
    if temperature is not None:
        TEMP_MIN, TEMP_MAX = 18, 27
        if not (TEMP_MIN <= temperature <= TEMP_MAX):
            issues.append(
                f"⚠️ Temperature ({temperature}°C) outside acceptable range ({TEMP_MIN}-{TEMP_MAX}°C)"
            )
    
    # Umidade
    if humidity is not None:
        HUM_MIN, HUM_MAX = 30, 70
        if not (HUM_MIN <= humidity <= HUM_MAX):
            issues.append(
                f"⚠️ Humidity ({humidity}%) outside acceptable range ({HUM_MIN}-{HUM_MAX}%)"
            )
    
    # CO₂
    if co2_level is not None:
        MAX_CO2 = 5.3
        if co2_level > MAX_CO2:
            issues.append(
                f"🔴 CRITICAL: CO₂ level ({co2_level} mmHg) exceeds maximum ({MAX_CO2} mmHg)"
            )
    
    # Ruído
    if noise_level is not None:
        MAX_NOISE = 60 if zone_type == "sleep" else 70
        if noise_level > MAX_NOISE:
            issues.append(
                f"⚠️ Noise level ({noise_level} dB) exceeds maximum for {zone_type} area ({MAX_NOISE} dB)"
            )
    
    is_valid = len(issues) == 0
    return is_valid, issues


def validate_zone_incompatibilities(zones: List[str], incompatible_zones: List[Tuple[str, str]]) -> List[str]:
    """
    Valida se existem zonas incompatíveis adjacentes.
    
    Referência: Internal Layout Assessment of a Lunar Surface Habitat
    
    Args:
        zones: Lista de zonas presentes
        incompatible_zones: Lista de pares de zonas incompatíveis
    
    Returns:
        Lista de avisos sobre incompatibilidades
    """
    warnings = []
    
    for zone1, zone2 in incompatible_zones:
        if zone1 in zones and zone2 in zones:
            warnings.append(
                f"⚠️ Incompatible zones present: {zone1} and {zone2} (should not be adjacent)"
            )
    
    return warnings


def calculate_layout_efficiency(zones: Dict[str, Any], floor_area: float) -> Dict[str, Any]:
    """
    Calcula métricas de eficiência do layout.
    
    Referência: A Tool for Automated Design and Evaluation of Habitat Interior Layouts
    
    Args:
        zones: Dicionário de zonas com suas áreas
        floor_area: Área total do piso
    
    Returns:
        Dicionário com métricas de eficiência
    """
    usable_area = sum(zone['area'] for zone in zones.values())
    circulation_area = floor_area - usable_area
    
    space_efficiency = (usable_area / floor_area * 100) if floor_area > 0 else 0
    circulation_index = (circulation_area / floor_area * 100) if floor_area > 0 else 0
    
    # Avaliação
    efficiency_status = "pass" if space_efficiency >= 75 else "warning"
    circulation_status = "pass" if 15 <= circulation_index <= 25 else "warning"
    
    return {
        "space_efficiency": {
            "value": space_efficiency,
            "target": 75.0,
            "status": efficiency_status,
            "unit": "%",
            "message": f"Space efficiency: {space_efficiency:.1f}% (target: ≥75%)"
        },
        "circulation_index": {
            "value": circulation_index,
            "target_range": (15.0, 25.0),
            "status": circulation_status,
            "unit": "%",
            "message": f"Circulation area: {circulation_index:.1f}% (target: 15-25%)"
        },
        "usable_area": usable_area,
        "circulation_area": circulation_area
    }


def validate_privacy_requirements(crew_size: int, private_zones: int) -> Tuple[bool, str]:
    """
    Valida se há áreas privadas suficientes para a tripulação.
    
    Referência: NASA's M2M Transit Habitat Refinement
    
    Args:
        crew_size: Tamanho da tripulação
        private_zones: Número de zonas privadas (quartos)
    
    Returns:
        Tupla (is_adequate, message)
    """
    privacy_index = (private_zones / crew_size * 100) if crew_size > 0 else 0
    is_adequate = privacy_index >= 100
    
    if is_adequate:
        message = f"✅ Privacy adequate: {private_zones} private quarters for {crew_size} crew members"
    else:
        message = f"⚠️ Privacy insufficient: {private_zones} private quarters for {crew_size} crew members (need {crew_size})"
    
    return is_adequate, message


def check_launch_vehicle_compatibility(diameter: float, sls_max: float, starship_max: float) -> dict:
    """
    Verifica compatibilidade com envelopes de veículos de lançamento.
    
    Args:
        diameter: Diâmetro do habitat (metros)
        sls_max: Diâmetro máximo do SLS (metros)
        starship_max: Diâmetro máximo do Starship (metros)
    
    Returns:
        Dicionário com compatibilidade de cada veículo
    """
    return {
        "sls": diameter <= sls_max,
        "starship": diameter <= starship_max
    }

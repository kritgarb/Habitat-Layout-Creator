"""
Validações de acordo com padrões NASA
"""
from typing import List, Tuple


def validate_nasa_standards(
    nhv_per_person: float,
    floor_area_per_person: float,
    min_nhv: float,
    min_floor_area: float
) -> Tuple[bool, List[str]]:
    """
    Valida se o habitat atende aos padrões NASA.
    
    Args:
        nhv_per_person: NHV por pessoa (m³)
        floor_area_per_person: Área de piso por pessoa (m²)
        min_nhv: NHV mínimo requerido (m³)
        min_floor_area: Área mínima requerida (m²)
    
    Returns:
        Tupla (is_valid, issues) onde:
        - is_valid: True se todos os padrões são atendidos
        - issues: Lista de strings descrevendo problemas encontrados
    """
    issues = []
    
    if nhv_per_person < min_nhv:
        issues.append(
            f"NHV per person ({nhv_per_person:.1f} m³) below minimum ({min_nhv} m³)"
        )
    
    if floor_area_per_person < min_floor_area:
        issues.append(
            f"Floor area per person ({floor_area_per_person:.1f} m²) below minimum ({min_floor_area} m²)"
        )
    
    is_valid = len(issues) == 0
    return is_valid, issues


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
